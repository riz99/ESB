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

driver.get('http://codepad.org')



# Select the Python language option

python_link = driver.find_elements_by_xpath("//input[@name='lang' and @value='Python']")[0]

python_link.click()



# Enter some text!

text_area = driver.find_element_by_id('textarea')

text_area.send_keys("print 'Hello,' + ' Test & Support Team!'")



# Submit the form!

submit_button = driver.find_element_by_name('submit')

submit_button.click()



# Make this an actual test. Isn't Python beautiful?

assert "Hello, Test & Support Team!" in driver.get_page_source()



# Close the browser!

#driver.quit()