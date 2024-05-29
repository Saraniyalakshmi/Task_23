
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.common.action_chains import ActionChains
paths = r"C:\Users\MageSaran\OneDrive\Desktop\Saraniya_GUVI\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
time.sleep(2)
driver.maximize_window()
# launch URL
driver.get("https://jqueryui.com/droppable/")
time.sleep(5)
driver.switch_to.frame(0)
# drag and drop
s1=driver.find_element(By.ID,"draggable")
d1=driver.find_element(By.ID,"droppable")
time.sleep(3)
actions = ActionChains(driver)
time.sleep(5)
actions. drag_and_drop(s1,d1)
actions. perform()
time. sleep(5)