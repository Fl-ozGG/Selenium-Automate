from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

GRID_URL = "http://localhost:4444/wd/hub"
WEB_URL  = "https://formy-project.herokuapp.com/form"
BROWSER_LIST = ["chrome", "firefox"]

def test(driver):
    
    driver.get(WEB_URL)
    
    first_name = driver.find_element(By.ID, "first-name")
    first_name.clear()
    first_name.send_keys("ignasi")
    
    last_name = driver.find_element(By.ID, "last-name")
    last_name.clear()
    last_name.send_keys("gurrea")
    
    job_tittle = driver.find_element(By.ID, "job-title")
    job_tittle.clear()
    job_tittle.send_keys("Entrepreneur")
    
    gradSchoolButton = driver.find_element(By.XPATH, "//input[@id='radio-button-3']/..")
    
    if "Grad School" in gradSchoolButton.text:
        driver.find_element(By.ID, "radio-button-3").click()
        print("button Grad School Found.")
    else: 
        print("The button u trying to check is not Grad School")
    
    gender = driver.find_element(By.XPATH, "//input[@id='checkbox-1']/..")

    if "Male" in gender.text:
        driver.find_element(By.ID, "checkbox-1").click()
        print("button Male found.")
    else: 
        print("The button u trying to check is not Male Button")
        
    select_menu = driver.find_element(By.ID, "select-menu")
    years_experience = Select(select_menu)
    years_experience.select_by_visible_text("2-4")    
    
    datepicker = driver.find_element(By.ID, "datepicker")
    datepicker.clear()
    time.sleep(10)
    datepicker.send_keys("12/25/2025")
    
    submit = driver.find_element(By.LINK_TEXT, "Submit")
    
    submit.click()
    
    wait = WebDriverWait(driver, 30)
    wait.until(EC.url_to_be("https://formy-project.herokuapp.com/thanks"))
    
    success_alert = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'alert-success')]"))
    )
      
    assert "The form was successfully submitted!" in success_alert.text, f"EXPECTED OUTPUT WAS: {success_alert.text}. BUT WAS NOT FOUND."
    print(f"Response: {success_alert.text}.")
    
    
    
    
    
def  get_driver(browser: str):
    match browser.lower():
        case "chrome":
            opts = ChromeOptions()
            opts.add_argument("--disable-gpu")
            opts.add_argument("--window-size=1280,1000")            
            opts.headless = False            
        case "firefox":
            opts = FirefoxOptions()
            opts.add_argument("--disable-gpu")
            opts.add_argument("--window-size=1280,1000")  
            opts.headless = False            
        case _:
            raise ValueError("Invalid Browser")
        
    return webdriver.Remote(command_executor=GRID_URL, options=opts)


for browser in BROWSER_LIST:
    driver = get_driver(browser)
    try:
        print(f"current browser runing: {browser}.")
        test(driver)
    finally: 
        driver.quit()