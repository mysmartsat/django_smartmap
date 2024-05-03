import googlemaps
from datetime import datetime
from googlemaps.distance_matrix import distance_matrix
from django.conf import settings
import time

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed

from bus.models import Bus, BusRoute


def timeit(func):
    """Decorator function used to time the execution of functions."""

    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        ret = func(*args, **kwargs)
        finish = time.perf_counter()
        runtime = round(finish - start)
        print(f"{func.__name__} took {runtime} second(s)")
        return ret

    return wrapper


gmaps = googlemaps.Client(key=settings.GOOGLE_PYTHON_API_KEY)


def calc_duration(origin, dest):
    """
    Calculates transit duration between origin and dest. Meant for only one origin, one dest. Departure time default to current time.
    """
    response = distance_matrix(gmaps, origins=origin, destinations=dest,mode="transit",
                          transit_mode="bus", departure_time=datetime.now(), transit_routing_preference="less_walking")
    # res['rows'][0]['elements'][0]['duration']
    return response


# @timeit
def calc_est_arrival_times(bus_route,bus_latitude,bus_longitude, current_stop_index):
    """
    This method calculates the estimated arrival time from a bus's current position to every bus stop on its route from the last stop.
    Bypasses Distance Matrix API usage limit of 25 destinations by using multithreading.
    """
    origin = (bus_latitude, bus_longitude)

    stop_data = list(bus_route.busroutedetails_set.all())
    stop_data = stop_data[current_stop_index:]
    if len(stop_data) == 0:
        return

    result = {}

    # must preserve original array's indices for parallel computing because threads/processes can finish out of order
    stops_latlng = {index: (route_details.bus_stop.latitude, route_details.bus_stop.longitude) for index, route_details in enumerate(stop_data)}

    with ThreadPoolExecutor() as executor:
        # submit calc_duration to the thread pool
        futures = {index: executor.submit(calc_duration, origin, stop) for index, stop in stops_latlng.items()}

        # wait for the threads to complete
        for _ in as_completed(futures.values()):
            pass

        # get the results out of the futures
        responses = [futures[key].result() for key in sorted(futures.keys())]

    # update the result object
    for i in range(len(stop_data)):
        response = responses[i]
        result[stop_data[i].bus_stop.stop_id] = response

    # return the API call response to the caller as a dictionary. Bus Stop ID is used as the key.
    return result


def calc_est_arrival_times_opt(bus_route,bus_latitude,bus_longitude, current_stop_index, select_stop_id):
    """
    This method calculates the estimated arrival time from a bus's current position to every bus stop on its route from the last stop.
    Bypasses Distance Matrix API usage limit of 25 destinations by using multithreading.
    """
    origin = (bus_latitude, bus_longitude)

    stop_data = list(bus_route.busroutedetails_set.all())
    next_stop_coord = (stop_data[current_stop_index].bus_stop.latitude,stop_data[current_stop_index].bus_stop.longitude)
    select_stop_coord = (stop_data[select_stop_id-1].bus_stop.latitude,stop_data[select_stop_id-1].bus_stop.longitude)
    if len(stop_data) == 0:
        return

    result = {}
    """
    If user select stop is the next stop, then the estimated time is from the bus to the next stop, 
    else, we use google map api characteristic to calculate the next stop to the select stop by configuring mode=transit,
    transit_mode=bus, and add the time from the bus to the next stop.    
    """
    if select_stop_id - 1 < current_stop_index:
        return
    elif select_stop_id - 1 == current_stop_index:
        result[select_stop_id] = distance_matrix(gmaps, origin, next_stop_coord, mode="driving")
    else:
        result[select_stop_id] = distance_matrix(gmaps, origin, next_stop_coord, mode="driving")
        next_to_select_stop = calc_duration(next_stop_coord, select_stop_coord)
        duration_text_str = int(result[select_stop_id]["rows"][0]["elements"][0]["duration"]["text"].split()[0]) + \
                            int(next_to_select_stop["rows"][0]["elements"][0]["duration"]["text"].split()[0])
        duration_value_second = result[select_stop_id]["rows"][0]["elements"][0]["duration"]["value"] + \
                                next_to_select_stop["rows"][0]["elements"][0]["duration"]["value"]
        result[select_stop_id]["rows"][0]["elements"][0]["duration"]["text"] = str(duration_text_str) + " mins"
        result[select_stop_id]["rows"][0]["elements"][0]["duration"]["value"] = duration_value_second


    # return the API call response to the caller as a dictionary. Bus Stop ID is used as the key.
    return result


def main():
    pass


# The following prevents RuntimeError for 'spawn' and 'forkserver' start_methods:
if __name__ == "__main__":
    main()
