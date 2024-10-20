
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver



#PATH = "C:\Program Files (x86)\chromedriver.exe"
#Web driver
driver_manager = ChromeDriverManager()
service = Service(driver_manager.install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.com/s?bbn=11846801&rh=n%3A468642%2Cn%3A20972781011&dc&qid=1729400447&rnid=11846801&ref=lp_11846801_nr_n_0")