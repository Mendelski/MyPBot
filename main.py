import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

path = 'venv/Scripts/chromedriver.exe'
google_email = ''
google_password = ''
driver = webdriver.Chrome(path)
action = ActionChains(driver)
timeout = 15
wait = WebDriverWait(driver, timeout)
visible = EC.visibility_of_element_located


def open_page(url, size=None):
    if not size:
        size = [900, 900]

    driver.get(url)
    time.sleep(1)
    driver.set_window_size(size[0], size[1])
    print("Page Ok!")
    return driver


def find_video_on_youtube(title):
    youtube_search = driver.find_element_by_id('search')

    youtube_search.send_keys(title)
    youtube_search.send_keys(Keys.ENTER)

    print("Search Ok!")


def click_on_first_video():
    wait.until(visible((By.ID, "video-title")))
    driver.find_element_by_id("video-title").click()
    print("Click Ok!")


def login_gmail():
    # link when logged https://mail.google.com/mail/u/0/#inbox

    driver.get('https://gmail.com/')
    login_field = driver.find_element_by_name('identifier')
    login_field.send_keys(google_email)
    login_field.send_keys(Keys.ENTER)


def pre_navigation():
    try:
        open_page('https://www.youtube.com/')
        time.sleep(0.5)

        find_video_on_youtube("Best eletronic music")
        driver.refresh()
        time.sleep(1.5)

        click_on_first_video()
        print('Video Running')
        time.sleep(30)

    except Exception as e:
        driver.__exit__()
        print(f"Bot closes unexpectedly\nError: {e}")
        return
# In a highly scalable scenario, it is very necessary to ensure that all processes are completed and leave no trace.
# In some cases it may be necessary to save the PID to kill the process at the end of the run.


pre_navigation()
