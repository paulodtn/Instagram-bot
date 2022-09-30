
#print(20*'\033[44m-','VAMOS PROGRAMAR',20*'\033[44m-\033[m')

#navegador = webdriver.Firefox('D:\\VSCode\\Pyton\\BOT INSTA\\geckodriver.exe')

#navegador.get('https://www.instagram.com/')


#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver.get("https://www.google.com")

from time import sleep
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.google.com")
sleep(3)
login = driver.find_element(By.NAME, "name")
