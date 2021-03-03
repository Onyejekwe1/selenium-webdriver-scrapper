from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver = "C:\Projects\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("https://secure-retreat-92358.herokuapp.com/")

# article_count = driver.find_element_by_css_selector("#articlecount a")
# # article_count.click()
# # print(article_count.text)
# recent_deaths = driver.find_element_by_link_text("Recent deaths")
# # recent_deaths.click()

# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Ifeanyi")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Onyejekwe")

email_address = driver.find_element_by_name("email")
email_address.send_keys("ifeanyiwisdom25@yahoo.com")

submit = driver.find_element_by_class_name("btn")
submit.send_keys(Keys.ENTER)

# driver.quit()