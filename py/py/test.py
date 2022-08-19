import os
from time import thread_time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select



username = os.getenv("sahamarjita")
# accessToken:  AccessToken can be genarated from automation dashboard or profile section
accessToken = os.getenv("NpzKJwnxxZnMCOisdWyPCvCKTwHlpy9NdQjhWSU5wGUOTiwp6z")
# gridUrl: gridUrl can be found at automation dashboard
gridUrl = "hub.lambdatest.com/wd/hub"


capabilities = {
    'LT:Options': {
        "build": "Python",
        "name": "Test1",
        "platformName": "Windows 10"
    },
    # "browserName": "Chrome",
    # "browserVersion": "88.0",
    "browserName": "Chrome",
    "browserVersion": "88.0",

}
url = "https://sahamarjita:NpzKJwnxxZnMCOisdWyPCvCKTwHlpy9NdQjhWSU5wGUOTiwp6z@hub.lambdatest.com/wd/hub"
#url = "https://"+username+":"+accessToken+"@"+gridUrl


"""
    ----------
    platformName : Supported platfrom - (Windows 10, Windows 8.1, Windows 8, Windows 7,  macOS High Sierra, macOS Sierra, OS X El Capitan, OS X Yosemite, OS X Mavericks)
    browserName : Supported platfrom - (chrome, firefox, Internet Explorer, MicrosoftEdge)
    browserVersion :  Supported list of version can be found at https://www.lambdatest.com/capabilities-generator/

    Result
    -------
"""

driver = webdriver.Remote(
    command_executor=url,
    desired_capabilities=capabilities
)

#1
driver.maximize_window()
driver.set_page_load_timeout(20)
driver.get("https://www.lambdatest.com/selenium-playground")

driver.find_element(By.XPATH, "//a[normalize-space()='Simple Form Demo']").click()
url = driver.current_url
print(str(url))
word = "simple-form-demo"
if word in url:
    print("Validated")
else:
    print("Not validated")


driver.find_element(By.XPATH, "//input[@id='user-message']").send_keys("Welcome To LambdaTest")
#send input
#l.send_keys("Welcome To LambdaTest")
time.sleep(5)
driver.find_element(By.ID, "showInput").click()
time.sleep(4)
wrdFound = driver.find_element(By.CSS_SELECTOR, "#message").text
if wrdFound == "Welcome To LambdaTest":
    print("Message validated")
else:
    print("Message not validated")

#2
driver.get("https://www.lambdatest.com/selenium-playground")
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Drag & Drop Sliders").click();
slider = driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/section[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/input[1]")
ActionChains(driver).drag_and_drop_by_offset(slider, 120, 0).perform()
time.sleep(4)
val = driver.find_element(By.CSS_SELECTOR, "#rangeSuccess").text
if(val == "95"):
    print("verified sucessfully")
else:
    print("not verified")



#3
driver.get("https://www.lambdatest.com/selenium-playground")
driver.find_element(By.XPATH, "//a[normalize-space()='Input Form Submit']").click()
driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()

mes = driver.find_element(By.ID, "name").get_attribute("validationMessage")
try:
    assert mes == "Please fill in the fields"
except AssertionError:
    print("Assertion failed. Actual value is",  mes)

driver.find_element(By.NAME, "name").send_keys("Main hoon Ghatotkach")
driver.find_element(By.CSS_SELECTOR, "#inputEmail4").send_keys("ghattu@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#inputPassword4").send_keys("gha!0!ku")
driver.find_element(By.CSS_SELECTOR, "#company").send_keys("ghattuStocks")
driver.find_element(By.CSS_SELECTOR, "#websitename").send_keys("www.ghattu.org")

select = Select(driver.find_element(By.XPATH, "/html/body/div[1]/div/section[3]/div/div/div[2]/div/form/div[3]/div[1]/select"))
select.select_by_visible_text("United States")

driver.find_element(By.CSS_SELECTOR, "#inputCity").send_keys("jungle")
driver.find_element(By.CSS_SELECTOR, "#inputAddress1").send_keys("12s, tree no. 5,")
driver.find_element(By.CSS_SELECTOR, "#inputAddress2").send_keys("aryavarth")
driver.find_element(By.CSS_SELECTOR, "#inputState").send_keys("bhumi")
driver.find_element(By.CSS_SELECTOR, "#inputZip").send_keys("674")
time.sleep(3)
driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
message = driver.find_element(By.XPATH, "//p[contains(text(),'Thanks for contacting us, we will get back to you ')]").text
time.sleep(4)
try:
    assert message == "Thanks for contacting us, we will get back to you shortly."
    print("Sucess messsage verified successfully")
except AssertionError:
    print("\nAssertion failed. Actual message value is",  message)
    time.sleep(3)
driver.close()

