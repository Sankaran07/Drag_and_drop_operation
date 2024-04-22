from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains

# Initialize Chrome WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open a webpage with draggable elements
driver.get("https://jqueryui.com/droppable/")

# Switch to the iframe containing the draggable elements
iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
driver.switch_to.frame(iframe)
sleep(1)

# Find the draggable element
draggable_element = driver.find_element(By.ID, "draggable")
sleep(1)

# Find the droppable element
droppable_element = driver.find_element(By.ID, "droppable")
sleep(1)

# Perform drag and drop action
actions = ActionChains(driver)
actions.drag_and_drop(draggable_element, droppable_element).perform()
sleep(3)

# Verify if the drop was successful
if droppable_element.text == "Dropped!":
    print("Drag and drop successful!")
else:
    print("Drag and drop unsuccessful!")

# Close the WebDriver session
driver.quit()

