#python 3 
#Python Script to enroll in the Course Management System courses and download handouts of BITS Pilani Hyd Campus
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
import time
from progress.bar import Bar
from getpass import getpass



#Initial Data Entry
print('Hello, Welcome to CMS AutoEnroller:')
userName=input('Username/Gmail: ') #enter your username/gmail
passWord = input('Password: ') # enter your password
in_dict = {} #initialze a dictionary called in_dict
flag =1 #to run while until user doesnot want to add more courses
while flag:
  coDe= input('Enter your Course Code: ') #inputs for course codes and sections follows
  Sections = input('Enter Section names(in the format L1,P1,T1) or Enter skip(to register in L section only): ') 
  user_list = Sections.split(',')
  for i in range(len(user_list)): 
    user_list[i]=user_list[i].upper()
  in_dict.update({coDe:user_list})
  while True:
    doneorcont = input('Add another course?(y/n): ')
    if doneorcont =='y':
      flag=1
      break
    elif doneorcont =='n':
      flag=0
      break
    else :
      print('Error: enter y(for yes)/n(for no)')



print('Your request is being processed...\n')
driver= webdriver.Chrome() #open driver
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
print("Don't exit the application or poweroff your computer.....")

bar = Bar('Processing',max=len(in_dict))
for i in in_dict.keys(): #for loop to run through each course
  time.sleep(1)
  try:
    courseSearcher = driver.find_element(By.NAME,'search').send_keys(i,Keys.ENTER) #search for entered course
  except:
    courseSearcher = driver.find_element(By.NAME,'q').send_keys(i,Keys.ENTER)#search for entered course
  try:
    L_section = driver.find_elements(By.CLASS_NAME,'aalink')  #click on Lsections
    L_section[0].click()
    time.sleep(1)
  except:
    print('\nCould not find course '+i+'\n')  
    driver.find_element(By.NAME,'q').clear()
    continue 
  else:
    try:
      enroller = driver.find_element(By.ID,'id_submitbutton') 
      enroller.click()
    except:
      driver.back()
    else :
      try:
        handoutDownloader = driver.find_elements(By.CLASS_NAME,'instancename')
        handoutDownloader[1].click()
      except :
        print('\nNo Handout available for '+i+'\n')
        driver.back()
        driver.back()
      else:
          driver.back()
          driver.back()
  time.sleep(1)
  bar.next()
  
    
  for j in range(len(in_dict[i])):
    time.sleep(1)
    if in_dict[i][j]!='SKIP':
      try:
        sectionClicker= driver.find_element(By.PARTIAL_LINK_TEXT,in_dict[i][j]) #find section
        sectionClicker.click()
      except:
        continue
      else:
        time.sleep(1)
        try:
          enroller = driver.find_element(By.ID,'id_submitbutton') #click on enroll button
          enroller.click()
        except:
          driver.back()
        else:
          driver.back() 
          driver.back()
          time.sleep(1)
    else:
      continue
  time.sleep(1)
  
  driver.find_element(By.NAME,'q').clear()
bar.finish()
print('\nEnrollement completed!\n')

time.sleep(1)
driver.quit()

