<br><br>
    ![Route51-64-93](readme-guide-images/Route30-64-93.gif)
    ![Route51](readme-guide-images/Route51-Lee.gif)
    ![Route93](readme-guide-images/Route93-A3.gif)
    ![Route64](readme-guide-images/Route64-D-1.gif)
<br><br>

# Instructions

# **Installation**

1. Download PyCharm Professional Edition
2. If you are a student or school faculty you can get educational license from: https://www.jetbrains.com/community/education/#students
3. Clone this repository in PyCharm and create your own branch for development
4. Open a terminal in PyCharm and execute the following
    1. pip install -r requirements.txt
5. Install Docker Desktop for your OS from https://www.docker.com/products/docker-desktop/
    1. On Windows, if the docker installation didn't prompt you to install
    the WSL 2 Kernel package update, Follow the instructions available at https://docs.microsoft.com/en-gb/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package
    to install and configure it. (Step 6 - Install your Linux distribution of choice is not required.)
    2. Create a basic docker account and sign in.
6. Before we start working with Docker, make sure that the Docker plugin is enabled.
The plugin is bundled with PyCharm and is activated by default.
If the plugin is not activated, enable it on the Plugins page of the IDE settings **Ctrl+Alt+S** as described in https://www.jetbrains.com/help/pycharm/managing-plugins.html.
7. Before you start, you need to have a Google Cloud account and enable Google Map API, then create a credentials, copy the API Key.

If you have trouble with any of these steps, please leave your issues.

# **Running/Debugging**

## **Setup Python Interpreter**

1. Press **Ctrl+Alt+S** to open the IDE settings and select **Build, Execution, Deployment | Docker**.
2. Click **+** to create a Docker server. Accept the suggested default values:

![Screenshot from 2023-12-21 01-32-54.png](readme-guide-images%2FScreenshot%20from%202023-12-21%2001-32-54.png)

3. Select **Project: smartmap | Python Interpreter**. Select Add interpreter:

**Interpreter 1**

4. Click **On Docker Compose** and select **smart_map** for the service option from the drop down. Click **Next** and wait for the installation finished. Then Click ********Next******** and choose the python interpreter and **create**.

![Screenshot from 2023-12-21 01-47-10.png](readme-guide-images%2FScreenshot%20from%202023-12-21%2001-47-10.png)
![Screenshot from 2023-12-21 01-48-17.png](readme-guide-images%2FScreenshot%20from%202023-12-21%2001-48-17.png)

### Interpreter 2

5. Add one more interpreter for the PROD settings by following the same steps except selecting the **smart_map_cloud** option for service this time. Click OK

![Screenshot from 2023-12-21 01-55-37.png](readme-guide-images%2FScreenshot%20from%202023-12-21%2001-55-37.png)

## **Setup Debug/Run Configuration**

1. Two django project configurations named **Django_DEV** and **Django_PROD** will be available with the project. Click the **Edit Configurations** in the top right corner of the IDE.

![Screenshot from 2023-12-21 01-58-17.png](readme-guide-images%2FScreenshot%20from%202023-12-21%2001-58-17.png)

2. Make sure to select the Python Interpreter you created in the previous section is selected against the interpreter option for both DEV (Interpreter-1) and PROD (Interpreter-2) settings. Make sure rest of the settings match same as shown below.

![Screenshot from 2023-12-21 02-04-52.png](readme-guide-images%2FScreenshot%20from%202023-12-21%2002-04-52.png)

![Screenshot from 2023-12-21 02-06-31.png](readme-guide-images%2FScreenshot%20from%202023-12-21%2002-06-31.png)

## **Debug/Run Application**

1. Click in a file's gutter to add a breakpoint.
2. Select an appropriate run setting (Django_DEV or Django_PROD). Click the green bug icon to run the server in debug mode. (You can use the green play button for regular mode.)
3. Make sure you select the correct interpreter from the right side corner of the IDE according to the runsettings you select.
4. Select Interpreter-1 for Django_DEV
5. Select Interpreter-2 for Django_PROD
6. By default, the manage.py in root folder are setting for production environment, if you want to run it locally, it needs to be changed to development,
7. Then edit the environment setting **local.env** file in **************************env folder************************** with your Google API key, set the value to `GOOGLE_MAP_API_KEY` **********and********** `GOOGLE_PYTHON_API_KEY`
8. Configure Task properties, use development settings for locally running.

![Screenshot from 2023-12-21 02-23-05.png](readme-guide-images%2FScreenshot%20from%202023-12-21%2002-23-05.png)

![Screenshot from 2023-12-21 15-10-43.png](readme-guide-images%2FScreenshot%20from%202023-12-21%2015-10-43.png)

9. Select **Run manage.py Task** from **Tools** menu.
10. Run **makemigrations** and **migrate** respectively in the window opened.

![Screenshot from 2023-12-21 15-14-16.png](readme-guide-images%2FScreenshot%20from%202023-12-21%2015-14-16.png)

![Screenshot from 2023-12-21 15-14-44.png](readme-guide-images%2FScreenshot%20from%202023-12-21%2015-14-44.png)

11. Click the link http://0.0.0.0:8000/ to access the application.

## **Debug Javascript code**

The easiest way right now is to open the server in Chrome.

1. Similar to the Python debug steps, run the server but open the URL in Chrome. You can right-click on the URL and select Chrome.
2. Navigate to the Sources tab.
3. Click the file in the Page pane.
4. Set breakpoints by clicking in the file's gutter.
5. Step through the code using the buttons at the top of the right-side pane.
6. Evaluate expressions in the Console window at the bottom.

# **Installing Android Device Emulator For Testing**

## **Method 1 Without Android Studio [Windows x64]**

1. Download and install [JDK](https://download.oracle.com/java/18/latest/jdk-18_windows-x64_bin.msi).
2. Set JAVA_HOME variable. Open Command Prompt (Win+R, type cmd and press Enter) or use any other terminal you like. For me path to JDK is `E:\Program Files\Java\jdk1.8.0_251.` Execute the following:`setx JAVA_HOME "E:\Program Files\Java\jdk1.8.0_251"`
3. Download and install [Intel Hardware Accelerated Execution Manager (HAXM)](https://github.com/intel/haxm/releases/download/v7.7.1/haxm-windows_v7_7_1.zip) if not already present in your system (you also need to switch off Hyper-V feature and enable Virtualization in BIOS for successful installation).
4. Download [Command-Line-Tools](https://dl.google.com/android/repository/commandlinetools-win-8512546_latest.zip)
5. Now create a folder to store the sdk files. This can be done in some drive were you have enough space. Mine is `D:\android-sdk`5.1 Extarct the contents of the file downloaded in step 4 in this directory. After this, the folder structure should look like this.
6. Set ANDROID_SDK_ROOT environment variable:`setx ANDROID_SDK_ROOT D:\android-sdk`
7. Create new entry in Path environment variable:`setx path "%PATH%;%ANDROID_SDK_ROOT%\cmdline-tools\tools\bin" /m`Note: you'll probably need to restart cmd in order the changes take effect.
8. Open CMD in directory **D:\android-sdk\cmdline-tools\tools\bin**8.1 Execute the below command. You can change the **android-29** with some other version which you want. You can see all the available versions [here](https://developer.android.com/studio/releases/platforms).`sdkmanager "platforms;android-29" "system-images;android-29;google_apis;x86_64" "platform-tools"`Note: This may take some time.8.2 Next we have to accept a bunch of licenses. Type the next command and answer y to each question:`sdkmanager --licenses`8.3 Now we are ready to create new virtual device:`avdmanager create avd -n test_avd_29 -k "system-images;android-29;google_apis;x86_64"`You can change the ADV name from **test_avd_29** to something else if you wish. Also make sure you use the same android sdk version you downloaded in the previous step in place of **android-29**.8.4 To see the list of virtual devices just type:`avdmanager list avd`
9. Go to emulator folder:`cd %ANDROID_SDK_ROOT%\emulator`
10. Last but not least thing is launching:`emulator -avd test_avd_29`Note: This may take sometime.

Reference : https://dev.to/andreisfedotov/how-to-install-android-emulator-without-installing-android-studio-3lce

## **Method 2 With Android Studio**

1. Download and install the latest android studio from https://developer.android.com/studio#downloads.
2. Launch Android Studio.
3. After the installation, Select the Virtual Device Manager Option.

![Screenshot from 2023-12-22 04-11-15.png](readme-guide-images%2FScreenshot%20from%202023-12-22%2004-11-15.png)

4. Select the default device and start it or create a new device.

![Screenshot from 2023-12-22 04-12-42.png](readme-guide-images%2FScreenshot%20from%202023-12-22%2004-12-42.png)

5. Once the device is created, it will be available at the window we saw in step 3. Click on the Play button available next to the device that you created in the previous step to boot it up.

## Launch the device

1. Once the device boots up, Click the 3 dots on the right bottom corner to open the settings.

![Screenshot from 2023-12-22 04-14-52.png](readme-guide-images%2FScreenshot%20from%202023-12-22%2004-14-52.png)

2. Select Location option on the left side. Select the routes tab on the right side. Add a source and destination as we do it Google Maps. Click Save Route.

![Screenshot from 2023-12-22 04-15-33.png](readme-guide-images%2FScreenshot%20from%202023-12-22%2004-15-33.png)

3. Select the route that you created in the previous step from the saved routes option and click the Play Route button on the right bottom corner. Make sure **Enable GPS Signal** toggle is ON.
4. Then create a bus driver user using admin account of django, the default password for the admin user is ‘`P@ssword1`’. Give the driver user permissions to access the driver page.

![Screenshot from 2023-12-22 04-27-44.png](readme-guide-images%2FScreenshot%20from%202023-12-22%2004-27-44.png)

5. Go back to the android device screen and open the web app URL/busdriver from the device. Login with the driver user and navigate to the map tab and select a route and click the start driving button. Now you can see the bus Moving on the map tab (In your browser window).

![Screenshot from 2023-12-22 04-30-55.png](readme-guide-images%2FScreenshot%20from%202023-12-22%2004-30-55.png)

6. Now it can simulate the bus movement and the code is running.

![Screenshot from 2023-12-22 04-34-31.png](readme-guide-images%2FScreenshot%20from%202023-12-22%2004-34-31.png)