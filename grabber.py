from selenium import webdriver

def getScreenShot(url):
    driver = webdriver.Chrome('D:/Users/chari/Desktop/Synced Folder/Programming/Python/CoOpScrape/chromedriver.exe')
    driver.get("http://" + url)
    screenshot = driver.save_screenshot('D:/Users/chari/Desktop/Synced Folder/Programming/Python/CoOpScrape/src/Screenshots/' + url + '.png')
    driver.quit()
