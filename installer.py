import os
import zipfile
import requests


path = r'C:\\Fraps\\MSLP_Updater-v2'
os.makedirs(path)
donwload = requests.get(
	'https://github.com/shiroamurha/MSLP_Updater-v2.0/raw/main/modskin_selenium.zip', 
	allow_redirects=True
)

open(path+'file.zip', 'wb').write(donwload.content)
with zipfile.ZipFile(path+'file.zip',"r") as zip_ref:

    zip_ref.extractall(path)

os.remove(f'{path}file.zip')

open('run.bat', 'w').write(f'{path}\\python MSLP_Updater.py')
