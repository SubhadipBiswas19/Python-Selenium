from asyncio import wait_for

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


test_url = "https://www.makemytrip.com/"
driver = webdriver.Chrome()
driver.get(test_url)
driver.maximize_window()

wait = WebDriverWait(driver, 10)


# Close the pop-up window.
wait_for (EC.element_to_be_clickable((By.XPATH, "//*[@class='commonModal__close']"))).click()


# #Click on the Service menu – Hotels.
# driver.find_element(By.XPATH, "//span[text()='Hotels']").click()
#
#
# # Select City, Property Name, or Location.
# driver.find_element(By.XPATH, "//input[@id='city']").click()
#
# driver.find_element(By.XPATH, "//input[@title='Where do you want to stay?']").send_keys("Kolkata")
#
# city_option = driver.find_element(By.XPATH, "//span[@class='blackText'='Kolkata']")
# city_option.click()
#
# #Select Check-In & Check-Out dates
# driver.find_element(By.XPATH, "//span[@aria-label='Next Month']").click()
