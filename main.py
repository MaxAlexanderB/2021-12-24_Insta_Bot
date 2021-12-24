from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
import os

CHROME_DRIVER_PATH = r"C:\Users\maxal\PycharmProjects\chromedriver.exe"
SIMILAR_ACCOUNT = "buzzfeedtasty"
USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PW']


class InstaFollower:
    # -------initiate driver--------#
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    # -------login---------#
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    # --------Open up follower popup and scroll down---------#
    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        # ---------Scroll down---------#
        time.sleep(2)
        modal = self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[2]')  # hie geisch zum popup u när scrollsch ganz abe 5 mau.
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    # -------Followers-------#
    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()

