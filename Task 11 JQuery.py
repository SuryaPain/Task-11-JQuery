import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
driver = webdriver.Chrome() 
driver_path = r"\"C:\Users\jayasurya"
driver.get("http://jqueryui.com/droppable/")
time.sleep(3)
WebDriverWait(driver, 6).until(
    EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, ".demo-frame"))
)
drag_item = driver.find_element(By.ID, "draggable")
target_item = driver.find_element(By.ID, "droppable")
action_chains = ActionChains(driver)
action_chains.drag_and_drop(drag_item, target_item).perform()
driver.switch_to.default_content()
time.sleep(10)
driver.close()
