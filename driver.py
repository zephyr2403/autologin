from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions, Chrome
import time

def find_element(driver,str):
    try:
        var = driver.find_elements_by_css_selector(str)
        return var
    except:
        return False

def find_visible(user):
    if user == False :
        return False
    else:
        for i in range(0,len(user)):
            if(user[i].is_displayed()==True):
                return user[i]
        return False
def link_text(driver,str):
    try:
        partial=driver.find_element_by_partial_link_text(str)
        return partial
    except:
        return False

def clickcheck(user):
    try:
        user.click()
        return True
    except:
        return False

def auto_login(url,username,password):
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = Chrome(chrome_options=opts)
    driver.get(url)
    i=0
    partial=link_text(driver,'already')
    if(not partial):
        partial=link_text(driver,'Already')
        if(not partial):
            partial=link_text(driver,'Log In')
            if(not partial):
                partial=link_text(driver,'Sign In')
    if(partial):
        partial.click()
        time.sleep(3)
    user = find_element(driver,"input[type='email']")
    user = find_visible(user)
    if(user==False or clickcheck(user) ==False):
        user = find_element(driver,"input[type='text']")
        user = find_visible(user)
    print user
    if(user):
        user.click()
        user.send_keys(username)
        passwd=find_element(driver,"input[type='password']")
        passwd = find_visible(passwd)
        if(not passwd):
            user.send_keys(Keys.ENTER)
            time.sleep(3)
            passwd=find_element(driver,"input[type='password']")
            passwd = find_visible(passwd)
        if(passwd):
            passwd.send_keys(password)
            passwd.send_keys(Keys.TAB)
            passwd.send_keys(Keys.ENTER)


use='https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
us='https://offcloud.com/#'
u='https://www.linkedin.com'
s='https://www.udemy.com'
auto_login(use,'ashutosh.extrimis.2403@gmail.com','ashutosh2403')
