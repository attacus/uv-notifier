from twilio.rest import Client
import xml.etree.ElementTree as eltree
from invoke import task
import urllib.request
import os
import time
import datetime
import decimal

def uv_level(city):
    url = 'https://uvdata.arpansa.gov.au/xml/uvvalues.xml'
    tree = eltree.parse(urllib.request.urlopen(url))
    root = tree.getroot()

    for child in root.findall(".//location[@id='" + city + "']/index"):
        current_uv = decimal.Decimal(child.text)
        if current_uv is None:
                print("No UV detected. Either the sun has vanished or there's something wrong with this program.")
    return current_uv


def send_sms(message):
    client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
    client.messages.create(to=os.environ['USER_PHONE'], from_= 'UV Notifier', body=message)


@task(help={'city': 'Name of the city to read UV levels in.'})
def notifier(ctx, city):
    """
    Notify the recipient when the UV levels reach a threshold in the ☀️ morning and 🌙 afternoon.
    """

    num_sms_sent = 0
    dt = datetime.datetime.now()

    while num_sms_sent == 0:
        current_uv = uv_level(city)
        print(str(current_uv))
        time.sleep(10)

        if 3.0 < current_uv < 3.5 and dt.hour < 12:
            print('🌅 It has just hit' + str(current_uv) + ' in ' + city + '. Put on some sunscreen before going outside.')
            send_sms('🌅 It has just hit' + str(current_uv) + ' in ' + city + '. Put on some sunscreen before going outside.')
            num_sms_sent = num_sms_sent + 1

        if 3.0 < current_uv < 3.5 and dt.hour > 12:
            print('☀️ The current UV rating in ' + city + ' is ' + str(current_uv) + '. Have fun outside.')
            send_sms('☀️ The current UV rating in ' + city + ' is ' + str(current_uv) + '. Have fun outside.')
            num_sms_sent = num_sms_sent + 1
