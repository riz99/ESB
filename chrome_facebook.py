from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chromedriver = r"C:\Program Files\SeleniumDriver\chromedriver-v2.33_win32\chromedriver.exe"

options = Options()
#options.add_argument("start-maximized")
#options.add_argument("--disable-extensions")
options.binary_location = r"C:\Program Files\Chrome62.0.3202.62\Chrome62.0.3202.62\chrome.exe"

#driver = webdriver.Chrome()
#driver = webdriver.Chrome(chromedriver) #Optional, if not specified, WebDriver will search your path for chromedriver.
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
# Go to codepad.org

user = "changerizki@gmail.com"
pwd = "Mantab123"

driver.get("http://www.facebook.com")

assert "Facebook" in driver.title

elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)

elem.send_keys(Keys.RETURN)

#driver.quit()