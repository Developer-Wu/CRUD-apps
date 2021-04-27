from selenium import webdriver
import time
from random import randint
USERNAME = 'IG_USERNAME'
PASSWORD = 'IG_PASSWORD'
CHROME_DRIVER_PATH = '/Users/danwu/Desktop/Web Development Portfolio/instagram-follow-bot/chromedriver'
class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(10)
        username_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(USERNAME)
        password_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(PASSWORD)
        login_btn = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        login_btn.click()


    def find_followers(self):
        time.sleep(10)
        search_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_btn.send_keys('lifewithceramics')
        time.sleep(5)
        account_btn = self.driver.find_element_by_xpath('//a[contains(@href, "lifewithceramics")]')
        account_btn.click()
        time.sleep(3)
        followers_btn = self.driver.find_element_by_xpath('//a[contains(@href, "lifewithceramics/followers")]')
        followers_btn.click()
        time.sleep(3)

        while True:
            print('hi')
            target_element = self.driver.find_element_by_xpath("//div[@class='isgrP']")
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', target_element)
            time.sleep(3)
            self.follow()




    def follow(self):
        follow_btns = self.driver.find_elements_by_xpath('//button[text()="Follow"]')

        for follow in follow_btns:
            num = randint(5,10) # randomness in following times to avoid IG ban
            follow.click()
            time.sleep(num)

insta_follower = InstaFollower()
insta_follower.login()
insta_follower.find_followers()

