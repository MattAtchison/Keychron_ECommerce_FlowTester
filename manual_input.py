from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


def manual_input(driver, wait):
    EMAIL = "dhdhdhdh@gmail.com"
    FIRST_NAME = "Frank"
    LAST = "Reynolds"
    ADDY = "Paddy's Pub"
    CITY = "Philly"
    ZIP = "34232"
    PHONE = "383838383"

    email_input = wait.until(ec.element_to_be_clickable((By.ID, "email")))
    email_input.send_keys(EMAIL)

    first_input = wait.until(ec.element_to_be_clickable((By.ID, "TextField0")))
    first_input.send_keys(FIRST_NAME)

    last_input = wait.until(ec.element_to_be_clickable((By.ID, "TextField1")))
    last_input.send_keys(LAST)

    addy_input = wait.until(ec.element_to_be_clickable((By.ID, "TextField2")))
    addy_input.send_keys(ADDY)

    city_input = wait.until(ec.element_to_be_clickable((By.ID, "TextField3")))
    city_input.send_keys(CITY)

    zip_input = wait.until(ec.element_to_be_clickable((By.ID, "TextField4")))
    zip_input.send_keys(ZIP)

    phone_input = wait.until(ec.element_to_be_clickable((By.ID, "TextField5")))
    phone_input.send_keys(PHONE)
