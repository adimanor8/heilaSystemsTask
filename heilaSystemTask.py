from selenium import webdriver
import names
import time
import uuid
import random
from selenium.webdriver.support.ui import Select
newId = []
for x in range(9):

    newId.append(random.randint(0, 9))

newId = str(newId)


driver = webdriver.Chrome()
studentsWeb = driver.get("http://students-aid.org:9222/")  # Open the Webpage
driver.find_element_by_id('register').click()  # Press on join US
driver.find_element_by_id('firstname').send_keys(names.get_first_name())
driver.find_element_by_id('lastname').send_keys(names.get_last_name())
driver.find_element_by_id("personalId").send_keys(newId)
driver.find_element_by_id("phone").send_keys("0503726870")
driver.find_element_by_id("dateOfBirth").send_keys("08/11/1990")
el = driver.find_element_by_id('academicSchool')
for option in el.find_elements_by_tag_name('option'):
    option.click()

el = driver.find_element_by_id('studytrack')

for option in el.find_elements_by_tag_name('option'):
    option.click()

el = driver.find_element_by_id('academicYear')

for option in el.find_elements_by_tag_name('option'):
    option.click()


element = driver.find_element_by_id("medicalTrainedYes")
driver.execute_script("arguments[0].click();", element)

element = driver.find_element_by_id("riskGroupNo")
driver.execute_script("arguments[0].click();", element)
element = driver.find_element_by_id("validDriverLicenceYes")
driver.execute_script("arguments[0].click();", element)

element = driver.find_element_by_id("roleSamplerDriveInButton")
driver.execute_script("arguments[0].click();", element)
driver.find_element_by_id('email').send_keys("adiismn0071@hotmail.com")
driver.find_element_by_id('password').send_keys("D@arrow2")
driver.find_element_by_id('register-button').click()

time.sleep(6)
driver.close()
