######## LinkedIN Scrapping by Oazed ######
## Requires Selenium
## Requires BeautifulSoup

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests

#import chrome webdriver
from selenium import webdriver
browser = webdriver.Chrome('C:/chromedriver_win32/chromedriver.exe')
#Open login page
browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
time.sleep(1)

#Enter login info:
elementID = browser.find_element_by_id('username')
elementID.send_keys('marketing@alphatrade.com.au')

elementID = browser.find_element_by_id('password')
elementID.send_keys('P@55w0rd')

elementID.submit()
time.sleep(2)
browser.get('https://www.linkedin.com/mynetwork/')
time.sleep(2)
browser.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')
time.sleep(2)
SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Clicking to see More
elem = browser.find_element_by_id("ember716")
elem.click()
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

## Making selenium Beautiful Soup readable object

src = browser.page_source
soup = BeautifulSoup(src, "lxml")
pepl = soup.find_all('a', attrs={"class":"ember-view mn-connection-card__picture"})
links =[]
for l in pepl:
#     print(l)
    links.append(str(l))

df = pd.DataFrame(list(zip(links)),columns = ['Links'])
df['Links']  = "https://linkedin.com" + df.Links.str[56:112]
df = df['Links'].str.split('"',expand=True)
df = df[[0]]
df = df.rename(columns={0:'links'})
df['links'] = df.links + "detail/contact-info/"

new_link =[]
name = []
# profile=[]
phone=[]
website = []
email = []
url = df.links
for link in url:
#     print(link)
    browser.get(link)
    time.sleep(3)
    new_src = browser.page_source
    new_soup = BeautifulSoup(new_src, "lxml")
    nm = new_soup.find('h1',attrs={'id':'pv-contact-info'})
#     pro = new_soup.find('a',attrs={'class':'pv-contact-info__contact-link link-without-visited-state t-14'})
    try:
        phn = new_soup.find('span',attrs={'class':'t-14 t-black t-normal'})
    except:
        phn = 'Phn not found'
    try:
        web = new_soup.find('a',attrs={'class':'pv-contact-info__contact-link link-without-visited-state'})
    except:
        web = 'Website Not Found'
    try:
        mail = new_soup.find('div',attrs={'class':'pv-profile-section__section-info section-info'})
    except:
        mail = 'Mail not found'
    name.append(str(nm))
    phone.append(str(phn))
    website.append(str(web))
    email.append(str(mail))

## Analysis

dfm = pd.DataFrame(list(zip(name,phone,website,email)),columns = ['name','phone','website','email'])
dfm['email']= dfm.email.str[-930:-850]
dfm['name'] = dfm.name.str[32:60]

dfm['phone']= dfm['phone'].str.lstrip('<span class="t-14 t-black t-normal">\n   ')
dfm['phone']= dfm['phone'].str.rstrip('\n  </span>')

dfm['name']= dfm['name'].str.lstrip("'")
dfm['name']= dfm['name'].str.rstrip("\n    </h1>'")
                                    
dfm['email']= dfm['email'].str.lstrip("""'rrer" target="_blank">\n  """)
dfm['email']= dfm['email'].str.rstrip("\n  </a>\n</div>\n</s'")

dfm['website']= dfm['website'].str.lstrip("""'<a class="pv-contact-info__contact-link link-without-visited-state"href=""")
dfm['website']= dfm['website'].str.rstrip("""rel="noopener noreferrer" target="_blank">\n  cryptotab162.webnode.com/\xa0\n</a>'""")
    
g = dfm['website'].str.split('"',expand=True)
g = g[[0]]
dfm['website'] = g[0]

def emailfu(x):
    email = x['email']
    if '@' not in email:
        return 0
    else:
        return email    
    
def websitefu(x):
    web = x['website']
    return 'https' + web
    lis = ['N',':']
    if lis in web:
        return 0
    else:
        return web

dfm['website'] = dfm.apply(websitefu,axis=1)

vals = dfm.apply(emailfu,axis=1)
dfm['email'] = vals

dfm['email']= dfm['email'].str.lstrip("""'ferrer" target="_blank">\n """)
dfm['email']= dfm['email'].str.rstrip("""</a>\n</div>\n</sec'""")
dfm['email']= dfm['email'].str.strip(" ")

dfm.to_csv('cust.csv',index=False)

