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

driver.get("https://fitpeo.com/revenue-calculator")


sliderBallElement_xpath = "//input[@type='range']"
textBoxBySliderBoxElement_xpath = "//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1o6z5ng']"

textBoxBySlider = driver.find_element(By.XPATH,textBoxBySliderBoxElement_xpath)
sliderBall = driver.find_element(By.XPATH,sliderBallElement_xpath)

actions = ActionChains(driver)
actions.scroll_by_amount(0,400).perform()

#driver.execute_script("arguments[0].scrollIntoView(false);", sliderBall)

textBoxBySlider.click()

textBoxBySlider.send_keys(Keys.CONTROL, "a")
textBoxBySlider.send_keys(Keys.BACK_SPACE)

time.sleep(3)

enter_value = 0
while enter_value < 560:
    textBoxBySlider.send_keys(Keys.ARROW_UP)
    enter_value += 1

time.sleep(5)

sliderValueAfterEnterVlue = sliderBall.get_attribute("aria-valuenow")
textBoxBySliderValue = textBoxBySlider.get_attribute("value")

print("Slider current Value is " + sliderValueAfterEnterVlue)

assert (textBoxBySliderValue == sliderValueAfterEnterVlue)
print("run successfully ")

time.sleep(5)
driver.quit()
