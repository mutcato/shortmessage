from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from sheet import Sheet
import settings

url = "https://messages.google.com/web/conversations/new"
table = Sheet(settings.FILE_NAME,settings.SHEET_NAME)
table.row_count = len(table.worksheet.get_all_records())

def start_web_driver():
	options = Options()
	# options.add_argument(f"user-agent={user_agent}")
	options.add_argument('--disable-infobars')
	options.add_argument('--disable-extensions')
	options.add_argument('--incognito')
	options.add_argument('--profile-directory=Default')
	options.add_argument('--disable-plugins-dicovery')
	options.add_argument('--start-maximized')
	options.add_experimental_option('excludeSwitches', ['enable-automation'])
	driver = webdriver.Chrome(settings.CHROME_DRIVER, options=options)
	return driver

driver = start_web_driver()

driver.get(url)
time.sleep(30)

def send_short_message(driver, phone, text):
	driver.find_element_by_xpath("/html/body/mw-app/div/main/mw-main-container/div[1]/mw-main-nav/div/mw-fab-link/a/span").click()
	time.sleep(5)

	phone_field = driver.find_element_by_xpath('//div[@class="mat-chip-list-wrapper"]/input[@class="input"]')
	phone_field = driver.find_element_by_css_selector('input.input')
	phone_field.send_keys(phone)
	time.sleep(2)
	phone_button = driver.find_element_by_xpath("/html/body/mw-app/div/main/mw-main-container/div[1]/mw-new-conversation-container/div/mw-contact-selector-button/button/span")
	phone_button.click()
	time.sleep(10)
	# text_field = driver.find_element_by_css_selector('textarea.input')
	# text_field.send_keys(text)
	# time.sleep(2)

	text_field = driver.execute_script("document.querySelectorAll('textarea.input')[0].value='{text}'".format(text=text))
	time.sleep(5)
	element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//textarea[@class="input"]')))
	driver.execute_script("arguments[0].click();", element)
	time.sleep(2)
	actions = ActionChains(driver)
	actions.send_keys(Keys.SPACE).perform()
	actions.send_keys(Keys.SPACE).perform()

	print("space... 5")
	time.sleep(2)
	send_button = driver.find_element_by_xpath("/html/body/mw-app/div/main/mw-main-container/div[1]/mw-conversation-container/div/div/mws-message-compose/mws-message-send-button/button/span/span")	
	send_button.click()
	time.sleep(2)


for row_number in range(settings.starting_row, table.row_count):
	row = table.get_row(row_number)
	if row[3]!="" and int(row[3])!=1:
		send_short_message(driver, row[0], row[2])
		table.update_one_cell(row_number, "sent", 1)


driver.quit()