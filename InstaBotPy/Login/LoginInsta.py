from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

options = Options()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
options.add_argument("--incognito")

# inicializamos las variables INPUTS
isSeguir = True
isNoseguir = False
numSeguidores = 30
userNameArtista = "geramx1"
count = 0
userName = "JoseTest123Zam"
passWord = "12jose*uiII"


#creamos nuestro bot
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
#Accedemos a intagram
driver.get("https://www.instagram.com/accounts/login/")
sleep(5)


#Buscamos los campos de usuario y pass
username_input = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
password_input = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
login_button = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div')

#escribimos nombre y contrase;a
username_input.send_keys(userName)
password_input.send_keys(passWord)
sleep(2)

#hacemos clic en el boton login
login_button.click()
sleep(5)

# seguir usuarios nuevos
if isSeguir:
    #Accedemos a intagram del artista 
    driver.get("https://www.instagram.com/"+userNameArtista+"/")
    sleep(10)

    #Buscamos los campos de usuario y pass
    followers_button = driver.find_element(By.XPATH,'//div[contains(text(),"seguidores")]')
    followers_button.click()
    sleep(5)

    #follower_button = driver.find_element(By.XPATH,'//div[contains(text(),"Seguir")]')

    while count <= numSeguidores:
        follower_button = driver.find_element(By.XPATH,'//button/div/div[contains(text(),"Seguir")]')
        follower_button.click()
        count = count + 1
        sleep(60)
        if count == numSeguidores/2:
            sleep(120)

# dejar de seguir
if isNoseguir:
    #Accedemos a intagram
    driver.get("https://www.instagram.com/"+userNameArtista+"/")
    sleep(10)

    #Buscamos los campos de usuario y pass
    followers_button = driver.find_element(By.XPATH,'//div[contains(text(),"seguidores")]')
    followers_button.click()
    sleep(5)

    while count <= numSeguidores:
        follower_button = driver.find_element(By.XPATH,'//button/div/div[contains(text(),"Seguir")]')
        follower_button.click()
        count = count + 1
        sleep(60)
        if count == numSeguidores/2:
            sleep(120)