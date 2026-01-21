## 🚀 Selenium Grid-Powered Form Automation

This project provides a robust, containerized solution for automating the submission of a sample web form using **Selenium Grid**. By leveraging Docker, we ensure consistent and parallel testing across multiple browser environments.

The target form, hosted at [Formy Project](https://formy-project.herokuapp.com/form), showcases various common web elements:

  * **Text Fields:** First Name, Last Name, Job Title
  * **Radio Buttons:** Education Level (e.g., Grad School)
  * **Checkboxes:** Gender (e.g., Male)
  * **Dropdown Selects:** Years of Experience
  * **Date Pickers**

Upon successful execution, the script fills out all fields, submits the form, and asserts the successful confirmation message on [the thank-you page](https://formy-project.herokuapp.com/thanks).

-----

### 🌟 Key Features

  * **Parallel Testing:** Automation script runs concurrently on both **Chrome** and **Firefox** nodes via Selenium Grid.
  * **Containerized Environment:** Uses Docker and `docker-compose.yml` for easy setup and isolation of the Selenium Hub and browser nodes.
  * **Visual Debugging (VNC):** Monitor the automation in real-time by connecting to the browser nodes using a VNC viewer.
  * **Robust Verification:** Utilizes `WebDriverWait` and `expected_conditions` to ensure the final success message is correctly displayed.

-----

### 📋 Prerequisites

Ensure you have the following tools installed and configured:

  * **[Docker](https://www.docker.com/):** For building and running containerized applications.
  * **[Docker Compose](https://docs.docker.com/compose/):** (Recommended) For managing the multi-container Selenium Grid setup.
  * **Python 3.14+:** To run the automation script.
  * **VNC Viewer:** ([TightVNC Viewer](https://www.tightvnc.com/download.php) recommended) For viewing the browser sessions graphically.

-----

### ⚙️ Setup and Execution

You have two primary ways to set up the Selenium Grid: using Docker Compose (Recommended) or running individual Docker commands.

#### 1\. Quick Setup with Docker Compose (Recommended)

This method uses the provided `docker-compose.yml` to set up the entire Selenium Grid network (Hub, Chrome Node, Firefox Node) with a single command.


# Start the Selenium Grid Hub and Nodes in detached mode
docker-compose up -d

#### 2\. Manual Setup with Docker Commands

If you prefer to run the containers manually:


# 1. Start Selenium Hub
docker run -d -p 4444:4444 --name selenium-hub selenium/hub:4.13.0

# 2. Start Chrome Node (linking to the hub)
docker run -d --name chrome-node --link selenium-hub:hub -p 5902:5900 selenium/node-chrome:4.13.0

# 3. Start Firefox Node (linking to the hub)
docker run -d --name firefox-node --link selenium-hub:hub -p 5901:5900 selenium/node-firefox:4.13.0

-----

### 🏃 Running the Automation Script

After the Selenium Grid is running, build the custom runner image and execute the script:


# 1. Build the Python runner image using the provided dockerfile
docker build -t form-automation-runner .

# 2. Run the automation script container
# Ensure the container can communicate with the selenium-hub on localhost:4444
docker run --network host form-automation-runner

-----

### 🖥️ Viewing the Browser with VNC

To visually observe the automation filling out the form, connect a VNC Viewer to the running node containers:

1.  Open your VNC Viewer application (e.g., TightVNC Viewer).
2.  Connect to the following addresses:
      * **Chrome Node:** `localhost:5902`
      * **Firefox Node:** `localhost:5901`

> **💡 Note:** The VNC ports (`5901` and `5902`) are mapped in the `docker-compose.yml` file. You can open multiple VNC windows to watch both browsers simultaneously\!

-----

