from selenium import webdriver
import time
PROMISED_DOWN = 20
PROMISED_UP = 20
CHROME_DRIVER_PATH = '/Users/danwu/Desktop/Web Development Portfolio/internetSpeed/chromedriver'
TWITTER_EMAIL = 'TWITTER_LOGIN_EMAIL'
TWITTER_PASSWORD = 'TWITTER_PASSWORD'

class InternetSpeedTwitterBot:
    def __init__(self):
        self.up = PROMISED_UP
        self.down = PROMISED_DOWN
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def get_internet_speed(self):
        self.driver.get(url='https://www.speedtest.net/')
        time.sleep(5)
        go_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]')
        go_button.click()
        time.sleep(20)
        self.down_value = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        time.sleep(20)
        self.up_value = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)
        print(self.down_value)
        print(self.up_value)
    def tweet_at_provider(self):
        if self.down_value < PROMISED_DOWN or self.up_value < PROMISED_UP:
            self.driver.get('https://twitter.com/')
            time.sleep(5)
            log_in_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div')
            log_in_btn.click()
            user_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
            password_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
            user_input.send_keys(TWITTER_EMAIL)
            password_input.send_keys(TWITTER_PASSWORD)
            log_in_btn_2 = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
            log_in_btn_2.click()
            time.sleep(5)
            tweet_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div')
            tweet_input.send_keys(f'Hey Internet Provider why is my internet speed {self.down_value}down/{self.up_value}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up')
            tweet_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
            tweet_btn.click()
        else:
            print('Internet speed is normal!')

internet_speed_twitter_bot = InternetSpeedTwitterBot()

internet_speed_twitter_bot.get_internet_speed()
internet_speed_twitter_bot.tweet_at_provider()