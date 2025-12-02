# Selenium Form Automation

This project automates the workflow of a web form available at [Formy Project](https://formy-project.herokuapp.com/form).

The form includes multiple input types such as:

- Text fields  
- Dropdown selects  
- Date pickers  
- Checkboxes  

Once the form is filled and submitted:

- The URL changes  
- A confirmation message is displayed  

If the automation runs successfully, the form submission will be confirmed, and you will be redirected to [the confirmation page](https://formy-project.herokuapp.com/thanks).

---

## Requirements

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
