import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains, Keys

PATH = (r"C:\Users\Lenovo\Documents\sel_python\chromedriver-win64\chromedriver.exe")

service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://www.fitpeo.com/")
driver.maximize_window()
print("Home Page Opened")

driver.get("https://fitpeo.com/revenue-calculator")
print("Revenue Calculator Page Opened")

sliderBall = driver.find_element(By.XPATH,"//input[@type='range']")

textBoxBySlider = driver.find_element(By.XPATH,"//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1o6z5ng']")

actions = ActionChains(driver)
actions.scroll_by_amount(0,400).perform()

#Clean text input
textBoxBySlider.send_keys(Keys.CONTROL, "a")
textBoxBySlider.send_keys(Keys.BACK_SPACE)
textBoxBySlider.send_keys("820")

#Take the value of slider
sliderValueAfterEnterVlue = sliderBall.get_attribute("aria-valuenow")

textBoxBySliderValue = textBoxBySlider.get_attribute("value")

print("Slider current Value is " + sliderValueAfterEnterVlue)

assert textBoxBySliderValue == sliderValueAfterEnterVlue

actions.scroll_by_amount(0,600).perform()

check_box_list = [0, 1, 2,7]
xpath = "//*[@type='checkbox']"
checkbox_element = driver.find_elements(By.XPATH, xpath)
for i in check_box_list:
    checkbox_element[i].click()
    time.sleep(1)

actual_recurringAmount = "110700"
rembursment_xpath = "//p[@class='MuiTypography-root MuiTypography-body1 inter css-1bl0tdj'][normalize-space()='$110700']"
rembursment_amt = driver.find_element(By.XPATH,rembursment_xpath)

amount = rembursment_amt.text
amount = amount.replace("$", "")
assert actual_recurringAmount == amount, "amount does not match"
print(amount)
time.sleep(3)
driver.quit()
