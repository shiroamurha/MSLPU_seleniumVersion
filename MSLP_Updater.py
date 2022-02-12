from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import shutil
import os
import requests
import zipfile
import pyautogui




def window():

	pyautogui.alert(
		text='Updating Modskin LOLPRO...',
		title='Modskin Updater'
	)

def get_download_specs():

	local_path = rf'{os.path.dirname(os.path.realpath(__file__))}\\chromedriver.exe'

	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
	options.add_argument('--no-sandbox')
	options.add_argument('--disable-dev-shm-usage')

	driver = webdriver.Chrome(
		executable_path=local_path, 
		chrome_options=options
	)

	driver.get('http://leagueskin.net/p/download-mod-skin-2020-chn')

	link = driver.find_element(By.ID, 'link_download3').get_attribute('href')
	patchname = driver.find_element(By.ID, 'link_download3').text
	patchname = patchname.split(' ')
	patchname = patchname[3]

	driver.close()

	return [str(link), str(patchname)]

def update():
	
	path = r'C:\\Fraps\\temp\\'

	try:
		shutil.rmtree(path)
	except:
		os.makedirs(path)
		dir_path = True
	else:
		dir_path = False

	if not dir_path:
		os.makedirs(path)

	window()
	
	download_specs = get_download_specs()
	donwload = requests.get(download_specs[0], allow_redirects=True)

	open(path+'file.zip', 'wb').write(donwload.content)
	with zipfile.ZipFile(path+'file.zip',"r") as zip_ref:

	    zip_ref.extractall(path)

	os.remove(f'{path}file.zip')
	try:
		os.startfile(f'{path}LOLPRO {download_specs[1]}.exe')
	except:
		pass



############ run

update()

############