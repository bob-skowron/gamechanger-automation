import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
import logging

gc_url = "https://web.gc.com/"

logger = logging.getLogger()


def login(driver):
    user = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    logger.info("Logging into gamechanger as %s", user)

    driver.get(gc_url)

    # fill in the user name
    email_box = driver.find_element(by=By.NAME, value="email")
    email_box.send_keys(user)
    next_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    next_button.click()

    # takes you to the passowrd screen
    # TODO: does this require a code on entry every time?? Need to review how to handle this
    code_input = input("Please enter the code:")
    code_box = driver.find_element(by=By.NAME, value="code")
    code_box.clear()
    code_box.send_keys(code_input)

    password_box = driver.find_element(by=By.NAME, value="password")
    password_box.send_keys(password)
    login_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    login_button.click()


driver = webdriver.Chrome()
driver.implicitly_wait(2)


login(driver)

team_id = os.getenv("TEAM_ID")
team_name = os.getenv("TEAM_NAME")

## On the team page
# TODO: figure out how to pick the right team. For now assume it's an input

# Got to the schedule page
driver.get(f"https://web.gc.com/teams/{team_id}/{team_name}/schedule")

# Read in the events from CSV
with open("inputs.csv", mode="r") as file:
    input_dictionary = csv.DictReader(file)

    schedule = list(input_dictionary)

logger.info("Found %s events to import", len(schedule))


# Create the events
all_buttons = driver.find_elements(by=By.CSS_SELECTOR, value="button")
# TODO: error handle
add_event_button = [
    x for x in all_buttons if x.get_attribute("data-testid") == "add-event-button"
][0]
add_event_button.click()

counter = 1
for i in range(0, len(schedule)):
    s = schedule[i]
    all_event_buttons = driver.find_elements(by=By.CSS_SELECTOR, value="button")
    is_scrimmage = False

    event_type = s["EventType"]  # Game, Practice, Other
    event_type_button = [
        x
        for x in all_event_buttons
        if x.get_attribute("data-testid") == f"event-type-{event_type}"
    ][0]
    event_type_button.click()

    # have to get in and out of the date picker
    date_field = driver.find_element(by=By.ID, value="start-time-field-date")
    date_field.click()
    date_field.send_keys(s["Date"])
    date_field.send_keys(Keys.TAB)

    time_field = driver.find_element(by=By.ID, value="start-time-field-time")
    for v in s["Time"]:  # send character by character...
        time_field.send_keys(v)
    time_field.send_keys(Keys.TAB)

    duration_field = driver.find_element(by=By.ID, value="Duration-field")
    duration_field.send_keys(s["Duration"])  # TODO: this isn't filling correctly

    arrive_field = driver.find_element(by=By.ID, value="Arrive-field")
    arrive_field.click()
    arrive_field.send_keys(s["Arrival"])

    # button click again
    all_event_buttons = driver.find_elements(
        by=By.CSS_SELECTOR, value="button"
    )  # need to refresh after button click
    home_away = s["Side"]  # TBD, home, away
    home_away_button = [
        x
        for x in all_event_buttons
        if x.get_attribute("data-testid") == f"game-side-{home_away}"
    ][0]
    home_away_button.click()

    # location
    location_field = driver.find_element(by=By.ID, value="location-field")
    location_field.click()
    location_field.send_keys(s["Location"])
    location_field.send_keys(Keys.ARROW_DOWN)  # TODO: Not filling in quite right
    location_field.send_keys(Keys.RETURN)

    notes_field = driver.find_element(by=By.ID, value="notes-field")
    notes_field.send_keys(s["Notes"])

    # opponent is a drop-down...ignore for now
    opponent_field = driver.find_element(by=By.ID, value="opponents-field")
    opponent_field.click()
    opponent_field.send_keys(s["Opponent"])  # TODO: This is super messy
    opponent_field.send_keys(Keys.TAB)

    i += 1

    # all_event_buttons = driver.find_elements(
    #     by=By.CSS_SELECTOR, value="button"
    # )  # need to refresh after button click

    # if i < len(schedule) - 1:
    #     save_and_add_button = [
    #         x
    #         for x in all_event_buttons
    #         if x.get_attribute("data-testid") == "add-event-modal-save-and-add-another"
    #     ][0]
    #     save_and_add_button.click()
    # else:
    #     save_and_close_button = [
    #         x
    #         for x in all_event_buttons
    #         if x.get_attribute("data-testid") == "add-event-modal-save-and-close"
    #     ][0]
    #     save_and_close_button.click()


driver.close()
