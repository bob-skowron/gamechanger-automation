import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(2)

gc_url = "https://web.gc.com/"

user = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
team_id = os.getenv("TEAM_ID")
team_name = os.getenv("TEAM_NAME")

driver.get(gc_url)

# fill in the user name
email_box = driver.find_element(by=By.NAME, value="email")
email_box.send_keys(user)
next_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
next_button.click()

# takes you to the passowrd screen
# TODO: does this require a code on entry every time??
code_input = input("Please enter the code:")
code_box = driver.find_element(by=By.NAME, value="code")
code_box.clear()
code_box.send_keys(code_input)

password_box = driver.find_element(by=By.NAME, value="password")
password_box.send_keys(password)
login_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
login_button.click()


## On the team page
# TODO: figure out how to pick the right team. For now assume it's an input

# Got to the schedule page
driver.get(f"https://web.gc.com/teams/{team_id}/{team_name}/schedule")

# Read in the events from CSV

# Create the event
all_buttons = driver.find_elements(by=By.CSS_SELECTOR, value="button")

# TODO: error handle
add_event_button = [
    x for x in all_buttons if x.get_attribute("data-testid") == "add-event-button"
][0]
add_event_button.click()


all_event_buttons = driver.find_elements(by=By.CSS_SELECTOR, value="button")
is_scrimmage = False

event_type = "Game"  # Game, Practice, Other
event_type_button = [
    x
    for x in all_event_buttons
    if x.get_attribute("data-testid") == "event-type-practice"
][0]
event_type_button.click()

# have to get in and out of the date picker
date_field = driver.find_element(by=By.ID, value="start-time-field-date")
date_field.click()
date_field.send_keys("02/23/24")
date_field.send_keys(Keys.TAB)

time_field = driver.find_element(by=By.ID, value="start-time-field-time")
time_field.click()
time_field.send_keys("08:00 PM")

duration_field = driver.find_element(by=By.ID, value="Duration-field")
duration_field.click()
duration_field.send_keys("30 min")

arrive_field = driver.find_element(by=By.ID, value="Arrive-field")
arrive_field.click()
arrive_field.send_keys("30 min before")

# button click again
all_event_buttons = driver.find_elements(
    by=By.CSS_SELECTOR, value="button"
)  # need to refresh after button click
home_away = "home"  # Game, Practice, Other
home_away_button = [
    x for x in all_event_buttons if x.get_attribute("data-testid") == "game-side-home"
][0]
home_away_button.click()


# opponent is a drop-down...ignore for now
opponent_field = driver.find_element(by=By.ID, value="opponents-field")
opponent_field.click()
opponent_field.send_keys("test-124")
opponent_field.send_keys(Keys.TAB)

# location
location_field = driver.find_element(by=By.ID, value="location-field")
location_field.click()
location_field.send_keys("504 Cemetery Rd")
location_field.send_keys(Keys.ARROW_DOWN)
location_field.send_keys(Keys.RETURN)

notes_field = driver.find_element(by=By.ID, value="notes-field")
notes_field.send_keys("Field 4")

# if not last
all_event_buttons = driver.find_elements(
    by=By.CSS_SELECTOR, value="button"
)  # need to refresh after button click
save_and_add_button = [
    x
    for x in all_event_buttons
    if x.get_attribute("data-testid") == "add-event-modal-save-and-add-another"
][0]
save_and_add_button.click()


save_and_close_button = [
    x
    for x in all_event_buttons
    if x.get_attribute("data-testid") == "add-event-modal-save-and-close"
][0]
save_and_close_button.click()


driver.close()
