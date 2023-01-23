from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
import time
from progress.bar import Bar
from selenium .webdriver.support.wait import WebDriverWait
from getpass import getpass
print('Hello, Welcome to CMS AutoEnroller:')
userName=input('Username/Gmail: ') #enter your username/gmail
passWord = getpass('Password: ')
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

driver= webdriver.Chrome() #open drive
driver.get('https://cms.bits-hyderabad.ac.in/my/') 
waiter = WebDriverWait(driver, timeout=1,poll_frequency=0.5).until(lambda d: d.find_element(By.LINK_TEXT,value='Google'))
gLink =driver.find_element(By.LINK_TEXT,value='Google') #click on sign in through Google
gLink.click()

usr = driver.find_element(By.ID,'identifierId').send_keys('f20211887@hyderabad.bits-pilani.ac.in',Keys.ENTER) 
waiter = WebDriverWait(driver, timeout=3,poll_frequency=0.5).until(lambda d: d.find_element(By.NAME,"password"))
time.sleep(5)# type in username and hit enter # wait for 1s to let the browser load
pwd = driver.find_element(By.NAME,"password").send_keys('madmonkeycitygym123#',Keys.ENTER) # type in password and hit enter
waiter = WebDriverWait(driver, timeout=3,poll_frequency=0.5).until(lambda d: d.find_element(By.LINK_TEXT,value="All courses"))

allCoursesClicker = driver.find_element(By.LINK_TEXT,value='All courses') #click on all courses link
allCoursesClicker.click()
for i in in_dict.keys():
    z=0
    try:
        waiter = WebDriverWait(driver, timeout=1,poll_frequency=0.5).until(lambda d: d.find_element(By.NAME,'search'))
        courseSearcher = driver.find_element(By.NAME,'search').send_keys(i,Keys.ENTER) #search for entered course
    except:
        waiter = WebDriverWait(driver, timeout=1,poll_frequency=0.5).until(lambda d: d.find_element(By.NAME,'q'))
        courseSearcher = driver.find_element(By.NAME,'q').send_keys(i,Keys.ENTER)#search for entered course
    try:
        waiter = WebDriverWait(driver, timeout=1,poll_frequency=0.5).until(lambda d: d.find_element(By.CLASS_NAME,'aalink'))
        L_section = driver.find_elements(By.CLASS_NAME,'aalink')  #click on Lsections
        L_section[0].click()
    except:
        print('\nCould not find course '+i+'\n')  
        waiter = WebDriverWait(driver, timeout=1,poll_frequency=0.5).until(lambda d: d.find_element(By.NAME,'q'))
        driver.find_element(By.NAME,'q').clear()
        continue
    else:
        try:
            waiter = WebDriverWait(driver, timeout=1,poll_frequency=0.5).until(lambda d: d.find_element(By.ID,'id_submitbutton'))
            enroller = driver.find_element(By.ID,'id_submitbutton') #click on enroll button
            enroller.click()
            z=1
        except:
            pass
    waiter = WebDriverWait(driver, timeout=1,poll_frequency=0.5).until(lambda d: d.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/div/div/ul/li[1]/div[2]/ul/li[1]/div/div[1]/div/div[1]/div/div[2]/div[2]'))
    handoutDownloader= driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/div/div/ul/li[1]/div[2]/ul/li[2]/div/div[1]/div/div[1]/div/div[2]/div[2]')
    handoutDownloader.click()
    print('Downloaded Handout for '+i)
    ann=driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/div/div/ul/li[1]/div[2]/ul/li[1]/div/div[1]/div/div[1]/div/div[2]/div[2]')
    ann.click()
    try:
        print('Announcements of '+i+' :')
        for j in range(1,500):
            waiter = WebDriverWait(driver, timeout=1,poll_frequency=0.5).until(lambda d: d.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[2]/div/section/div[2]/div[2]/div[2]/table/tbody/tr[1]/th/div/a'))
            annu=driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[2]/div/section/div[2]/div[2]/div[2]/table/tbody/tr[%s]/th/div/a'%str(j)).text
            print(annu)
    except:
        driver.back()
        driver.back()
        if z==1:
            driver.back()
    else:

        print('done')
        driver.back()
        driver.back()
    for k in range(len(in_dict[i])):
        x=0#for loop to access each course's sections
        if in_dict[i][k]!='SKIP': #incase user inputs skip then the loop is exited
            try:
                waiter = WebDriverWait(driver, timeout=1,poll_frequency=0.5).until(lambda d: d.find_element(By.PARTIAL_LINK_TEXT,in_dict[i][k]))
                sectionClicker= driver.find_element(By.PARTIAL_LINK_TEXT,in_dict[i][k]) #find section
                sectionClicker.click()
            except:
                continue
            else:
                try:
                    waiter = WebDriverWait(driver, timeout=1,poll_frequency=0.5).until(lambda d: d.find_element(By.ID,'id_submitbutton'))
                    enroller = driver.find_element(By.ID,'id_submitbutton') #click on enroll button
                    enroller.click()
                    x=1
                except:
                    pass

            waiter = WebDriverWait(driver, timeout=1,poll_frequency=0.5).until(lambda d: d.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/div/div/ul/li[1]/div[2]/ul/li[1]/div/div[1]/div/div[1]/div/div[2]/div[2]'))
            ann=driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[3]/div/section/div/div/div/ul/li[1]/div[2]/ul/li[1]/div/div[1]/div/div[1]/div/div[2]/div[2]')
            ann.click()
            
            try:
                print('Announcements of '+i+' '+in_dict[i][k]+' :')
                for m in range(1,500):
                    waiter = WebDriverWait(driver, timeout=1,poll_frequency=0.5).until(lambda d: d.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[2]/div/section/div[2]/div[2]/div[2]/table/tbody/tr[1]/th/div/a'))
                    annu=driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[2]/div/section/div[2]/div[2]/div[2]/table/tbody/tr[%s]/th/div/a'%str(m)).text
                    print(annu)
            except:
                
                driver.back()
                driver.back()
                if x==1 :
                    driver.back()
            else:
                print('done')
                driver.back()
                driver.back()
            
        else:
            continue
    print('\n')
    driver.find_element(By.NAME,'q').clear()
print('Finished!')
driver.quit()
