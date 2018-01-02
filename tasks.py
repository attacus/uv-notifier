from twilio.rest import Client
import os
import decimal
import xml.etree.ElementTree as eltree
import urllib.request
from invoke import task

def uv_level(city):
    url = 'https://uvdata.arpansa.gov.au/xml/uvvalues.xml'
    tree = eltree.parse(urllib.request.urlopen(url))
    root = tree.getroot()

    global decimal_uv
    global current_uv_rating

    for child in root.findall(".//location[@id='" + city + "']/index"):
        current_uv_rating = child.text
        decimal_uv = decimal.Decimal(current_uv_rating)
        if decimal_uv is None:
                print("No UV detected. Either the sun has vanished or there's something wrong with this program.")
    return decimal_uv, current_uv_rating

def send_sms(message):
    client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
    client.messages.create(to=os.environ['USER_PHONE'], from_= 'UV Notifier', body=message)

@task(help={'city': 'Name of the city to read UV levels in.'})
def notifier(ctx, city):
    uv_level(city)
    acceptable_uv = 4.0

    if decimal_uv <= acceptable_uv:
        print('The current UV rating is ' + current_uv_rating + '. Have fun outside.')
        send_sms('The current UV rating is ' + current_uv_rating + '. Have fun outside.')
    elif decimal_uv > acceptable_uv:
        print('The current UV rating is ' + current_uv_rating + '. Put on sunscreen and a hat or suffer the wrath of the hate orb.')
        send_sms('The current UV rating is ' + current_uv_rating + '. Put on sunscreen and a hat or suffer the wrath of the hate orb.')
    else:
        print('The current UV rating is ' + current_uv_rating + '.')
        send_sms('The current UV rating is ' + current_uv_rating + '.')
