# Dropbox Python API
import dropbox

# Argument parsing, file path checking
import time
import argparse
import getpass
import os

# Browser CLick Automation
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_auth_url_using_selenium(USERNAME, PASSWORD, URL):
	driver = webdriver.Firefox()
	driver.get(URL)
	time.sleep(4)
	elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[2]/input")
	time.sleep(2)
	elem.send_keys(USERNAME)
	elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div[1]/form[1]/div[1]/div[2]/div[2]/input")
	time.sleep(2)
	elem.send_keys(PASSWORD)
	elem.send_keys(Keys.RETURN)
	time.sleep(6)
	driver.find_element_by_xpath("/html/body/div[2]/div[3]/form/button[2]").click()
	auth_value = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/input").get_attribute("value")
	driver.close()
	return auth_value


def perform_upload(USERNAME, PASSWORD, FILEPATH, DESTINATION):
	app_key = "YOUR_APP_KEY"
	app_secret = "YOUR_APP_SECRET"

	flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
	authorize_url = flow.start()
	code = get_auth_url_using_selenium(USERNAME, PASSWORD, authorize_url).strip()
	access_token, user_id = flow.finish(code)
	client = dropbox.client.DropboxClient(access_token)
	print 'linked account: ', client.account_info()

	if os.path.exists(FILEPATH):
		f = open(FILEPATH, 'rb')
		response = client.put_file(DESTINATION, f)
	else:
		response = "None. File Path is invalid."
	print "uploaded:", response

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("filepath", help="Enter absolute path of file to be uploaded", type=str)
	parser.add_argument("destinationpath", help="Enter Dropbox path where upload is to be performed", type=str)
	args = parser.parse_args()
	FILEPATH = args.filepath
	DESTINATION = args.destinationpath
	USERNAME = raw_input("Email ID: ")
	PASSWORD = getpass.getpass()
	perform_upload(USERNAME, PASSWORD, FILEPATH, DESTINATION)