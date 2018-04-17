from selenium import webdriver

def getScreenShot(url):
    driver = webdriver.Chrome("D:\Users\M\Desktop\Synced Folder\Programming\Python\CoOpScrape\chromedriver.exe")
    driver.set_window_size(1920, 1080)
    driver.get("http://" + url)

    screenshot = driver.save_screenshot('D:\Users\M\Desktop\Synced Folder\Programming\Python\CoOpScrape\Screenshots\\' + url + '.png')
    driver.quit()
