from selenium import webdriver
import time
import itertools
import random


# Initiate webdriver
driver = webdriver.Chrome()
driver.get('https://izone.sunway.edu.my/login')
time.sleep(5)

# Credentials --replace with name and password
student_id = ''
password = ''

# Logging in
login_username = driver.find_element('id', 'student_uid')
login_password = driver.find_element('id', 'password')
login_username.clear()
login_password.clear()
login_username.send_keys(student_id)
login_password.send_keys(password)
driver.find_element('id', 'submit').click()
time.sleep(5)

# Checkin
driver.find_element('id', 'iCheckInUrl').click()

# Generate all possible combinations of 5 digit code
combinations = list(itertools.product(range(10), repeat=5))
result = [''.join(map(str, combo)) for combo in combinations]
random.shuffle(result)

# Loop until checkin code found/successful
start = time.time()
for combination in result:
    driver.execute_script("window.scrollBy(0, 100);")
    checkin = driver.find_element('id', 'checkin_code')
    checkin.clear()
    checkin.send_keys(combination)
    driver.find_element('id', 'iCheckin').click()
    notif = driver.find_element('id', 'notification').get_attribute('class')
    if 'alert-success' in notif:
        print(f'Checkin Code: {combination}')
        print('Successfully Checkedin!!!')
        break

end = time.time()
time_taken = end - start
print(f'time taken: {time_taken}')

# Close the browser
driver.quit()
