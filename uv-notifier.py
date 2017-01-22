from twilio.rest import TwilioRestClient
from bs4 import BeautifulSoup
import urllib2
import time
import os
import decimal

city = 'Melbourne'
acceptable_uv = 5.0
dangerous_uv = 11.0

def sendSMS(message):
    client = TwilioRestClient(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
    client.messages.create(to=os.environ['USER_PHONE'], from_=os.environ['TWILIO_PHONE'], body=message)

def uvLevel(html):
    soup = BeautifulSoup(html, 'html.parser')
    global current_uv_rating
    global decimal_uv
    for cities in soup.find_all('td', text=city):
        current_uv_rating = cities.next_sibling.getText()
        decimal_uv = decimal.Decimal(current_uv_rating)
        if decimal_uv is None:
                return False
    return True

num_sms_sent = 0

url = 'http://www.arpansa.gov.au/uvindex/realtime/wml/uvl.htm'

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

while True:
    request = urllib2.Request(url, headers=hdr)
    response = urllib2.urlopen(request)
    html_doc = response.read()
    uvLevel(html_doc)
    if decimal_uv == acceptable_uv:
        print('The current UV rating is '+ current_uv_rating + '. This is safe! Have fun outside.')
        sendSMS('The current UV rating is '+ current_uv_rating + '. This is safe! Have fun outside.')
        num_sms_sent = num_sms_sent + 1
    elif decimal_uv <= acceptable_uv:
        print('The current UV rating is '+ current_uv_rating + '. UV has reached safe levels.')
    elif decimal_uv == dangerous_uv:
        print('The current UV rating is '+ current_uv_rating + '. Put on sunscreen and a hat or suffer the wrath of the hate orb.')
        sendSMS('The current UV rating is '+ current_uv_rating + '. Put on sunscreen and a hat or suffer the wrath of the hate orb.')
        num_sms_sent = num_sms_sent + 1
    elif decimal_uv == 15.0:
        print('The current UV rating is '+ current_uv_rating + '. Seriously, it can get this high. I was surprised too.')
        num_sms_sent = num_sms_sent + 1
    else:
        print('The current UV rating is '+ current_uv_rating + '. UV is not at safe levels.')
    if num_sms_sent > 4:
        break
    time.sleep(300)
