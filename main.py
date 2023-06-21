from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import itertools


# Initiate webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://izone.sunway.edu.my/login')
time.sleep(5)

# Credentials
student_id = ''
password = ''

# Logging in
login_username = driver.find_element_by_id('student_uid')
login_password = driver.find_element_by_id('password')
login_username.clear()
login_password.clear()
login_username.send_keys(student_id)
login_password.send_keys(password)
driver.find_element_by_id('submit').click()

# Checkin
driver.find_element_by_id('icheckin').click()
checkin = driver.find_element_by_id('checkin_code')

combinations = list(itertools.permutations(range(10), 5))
for combination in combinations:
    checkin.send_keys(combination)
    driver.find_element_by_id('iCheckin').click()
    notif = driver.find_element_by_id('notification').get_attribute('class')
    if 'alert-success' in notif:
        print(f'Checkin Code: {combination}')
        break

print('Successfully Checkedin!!!')

# Close the browser
driver.quit()
