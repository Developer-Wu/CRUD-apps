from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

chrome_driver_url = 'CHROME_DRIVER_PATH'
driver = webdriver.Chrome(executable_path=chrome_driver_url)
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=2493159051&f_AL=true&f_E=2&geoId=103291313&keywords=developer&location=Hong%20Kong%20SAR')

time.sleep(2)
sign_in_btn = driver.find_element_by_xpath('/html/body/header/nav/div/a[2]')
sign_in_btn.click()
time.sleep(3)
email_input = driver.find_element_by_xpath('//*[@id="username"]')
email_input.send_keys('EMAIL')
password_input = driver.find_element_by_xpath('//*[@id="password"]')
password_input.send_keys('PASSWORD')
submit_btn = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
submit_btn.click()
time.sleep(5)
job_btn = driver.find_elements_by_css_selector('.job-card-container')
for job in job_btn:
    job.click()
    time.sleep(3)
    try:
        apply_btn = driver.find_element_by_css_selector('.jobs-apply-button')
        apply_btn.click()
    except:
        continue
    #phone_num = driver.find_element_by_xpath(
       # '//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2491662318,23461813,phoneNumber~nationalNumber)"]')
    #phone_num.send_keys('95355691')
    time.sleep(2)
    try:
        submit_btn = driver.find_element_by_xpath("//span[contains(.,'Submit application')]")
        submit_btn.click()
    except NoSuchElementException:
        dismiss = driver.find_element_by_css_selector('.jobs-easy-apply-modal button')
        dismiss.click()

        discard_btn = driver.find_element_by_css_selector('.artdeco-modal__actionbar .artdeco-button--primary')
        discard_btn.click()




