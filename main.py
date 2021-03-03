from selenium import webdriver

chrome_driver = "C:\Projects\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("https://www.python.org/events/python-events")

# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))
#
# logo = driver.find_element_by_class_name("python-logo")
#
# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)
#
# bug_link = driver.find_element_by_xpath("//*[@id='site-map']/div[2]/div/ul/li[3]/a")
# print(bug_link.text)

event_times = driver.find_elements_by_css_selector(".most-recent-events time")
event_titles = driver.find_elements_by_css_selector(".most-recent-events li a")

event_dic = {}

for n in range(len(event_times)):
    event_dic[n] = {
        "time": event_times[n].text,
        "name": event_titles[n].text
    }

print(event_dic)


driver.quit()
# driver.close()