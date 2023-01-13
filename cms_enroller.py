#python 3 
#Python Script to enroll in the Course Management System courses and download handouts of BITS Pilani Hyd Campus
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Initial Data Entry
print('Hello, Welcome to CMS AutoEnroller:')
userName=input('Username: ') #enter your username/gmail
passWord = input('Password: ') # enter your password
in_dict = dict() # creating a dictionary to store course numbers and section numbers
flag=1 # variable used to decide when to quit the program
while flag:
  coDe= input('Enter your Course Code: ') #inputs for course codes and sections follows
  Sections = input('Enter Section names(L1,P1,T1): ')
  user_list = Sections.split(',')
  in_dict.update({coDe:user_list})
  doneorcont=input('Add another course?(Y/n): ')
  if doneorcont == 'n':
    flag=0
  elif doneorcont =='Y':
    flag=1
  else:
    print('Error')



driver= webdriver.Chrome('chrome.driver') #open driver
driver.get('https://cms.bits-hyderabad.ac.in/my/') 
gLink =driver.find_element(By.LINK_TEXT,value='Google') #click on sign in through Google
gLink.click()
driver.implicitly_wait(5) 
usr = driver.find_element(By.ID,'identifierId').send_keys(userName,Keys.ENTER) # type in username and hit enter
time.sleep(1) # wait for 1s to let the browser load
pwd = driver.find_element(By.NAME,"password").send_keys(passWord,Keys.ENTER) # type in password and hit enter
time.sleep(1)
allCoursesClicker = driver.find_element(By.LINK_TEXT,value='All courses') #click on all courses link
allCoursesClicker.click()
for i in in_dict.keys(): #for loop to run through each course
    time.sleep(1)
    coureSearcher = driver.find_element(By.NAME,'q').send_keys(i,Keys.ENTER)
    L_section = driver.find_elements(By.CLASS_NAME,'aalink') 
    L_section[0].click()
    time.sleep(1)
    enroller = driver.find_element(By.ID,'id_submitbutton')
    enroller.click()
    handoutDownloader = driver.find_elements(By.CLASS_NAME,'aalink')
    handoutDownloader[1].click()
    time.sleep(1)

    driver.back()
    driver.back()
    for j in range(len(in_dict[i])): #for loop to run through each section of each course
        time.sleep(1)
        sectionClicker= driver.find_element(By.PARTIAL_LINK_TEXT,in_dict[i][j]) #find section
        sectionClicker.click()
        time.sleep(1)
        enroller = driver.find_element(By.ID,'id_submitbutton') #click on enroll button
        enroller.click()
        driver.back() 
        driver.back()
        time.sleep(1)


    time.sleep(1)
    driver.find_element(By.NAME,'q').clear()

driver.find_element(By.CLASS_NAME,'media-body').click() #go back to dashboard
time.sleep(500)

