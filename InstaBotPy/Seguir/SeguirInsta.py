def seguirUser(driver, userNameArtista, sleep, numSeguidores, By):
    #Accedemos a intagram
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
        sleep(3)