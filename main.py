from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from config import USER_EMAIL, USER_PASSWORD
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(
    'https://www.linkedin.com/jobs/search/?currentJobId=3913344364&distance=25&f_AL=true&geoId=102257491&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true')
sign_in_button = driver.find_element(by=By.CLASS_NAME, value="nav__button-secondary")
sign_in_button.click()
username = driver.find_element(by=By.ID, value="username")
password = driver.find_element(by=By.ID, value="password")
username.send_keys(USER_EMAIL)
password.send_keys(USER_PASSWORD)
time.sleep(3)
submit_button = driver.find_element(by=By.CSS_SELECTOR, value=".login__form_action_container button")
submit_button.click()
time.sleep(3)
job_list = driver.find_elements(by=By.CLASS_NAME, value="jobs-search-results__list-item")
for job in job_list:
    actions = ActionChains(driver)
    actions.move_to_element(job).perform()
    job.click()
    time.sleep(2)
    save_job_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-save-button span")
    if save_job_button.text == "Saved":
        continue
    else:
        save_job_button.click()
    time.sleep(2)
    dismiss_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-toast-item__dismiss")
    dismiss_button.click()
    time.sleep(2)


