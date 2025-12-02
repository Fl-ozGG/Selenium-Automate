# Selenium Form Automation

This project automates the workflow of a web form available at [Formy Project](https://formy-project.herokuapp.com/form).

The form includes multiple input types such as:

- Text fields  
- Dropdown selects  
- Date pickers  
- Checkboxes  

Once the form is filled and submitted:

- There is a time sleep before fullfilling the date field to allow the user to see the progress.
- The URL changes  
- A confirmation message is displayed  

If the automation runs successfully, the form submission will be confirmed, and you will be redirected to [the confirmation page](https://formy-project.herokuapp.com/thanks).

---

## Requirements

- VNC viewer (TigthVNC Viewer)
- [Docker](https://www.docker.com/)  
- [Docker Compose](https://docs.docker.com/compose/) (optional)  
- Python 3.14+

---

## Setting Up Selenium Grid

Start by running the Selenium Hub and nodes:

```bash
# Start Selenium Hub
docker run -d -p 4444:4444 --name selenium-hub selenium/hub:4.13.0

# Start Chrome Node
docker run -d --name chrome-node --link selenium-hub:hub selenium/node-chrome:4.13.0

# Start Firefox Node
docker run -d --name firefox-node --link selenium-hub:hub selenium/node-firefox:4.13.0
```


## Using VNC Viewer

1. Download and install [TightVNC Viewer](https://www.tightvnc.com/download.php).  
2. Launch the application (`TightVNC Viewer`).  
3. When prompted for the server, enter the address and port of the Selenium node:  
   - **Chrome Node:** `localhost:5901`  
   - **Firefox Node:** `localhost:5902`  
   *(These are the default ports if you didn’t change them.)*  
4. Click **Connect**. The VNC Viewer will display the browser running inside the Selenium node.  
5. Make sure your Selenium Hub and nodes are running before connecting.

> **Tip:** You can open multiple VNC Viewer windows to watch different browser nodes simultaneously.
