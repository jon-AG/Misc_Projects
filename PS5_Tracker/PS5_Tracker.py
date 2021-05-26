from datetime import datetime, date
import requests
from TargetAPI import Target
import time
from twilio.rest import Client

while True:
    #Target
    s = requests.session()
    s.get('https://www.target.com')
    key = s.cookies['visitorId']

    target = Target(api_key=key)

    results = target.search(keyword="81114595")
    in_stock = results[0]._data['onlineInfo']['availabilityCode']
    price = results[0].price

    now = datetime.now()
    today = date.today()
    current_time = now.strftime("%H:%M:%S")
    print('Current Price: {}'.format(price.price))
    status = ('{} {}: {}\n'.format(today, current_time, in_stock))
    print(status)

    if in_stock != 'OUT_OF_STOCK':
        account_sid = "AC011c454b47137abbd07a26728657d70b"
        auth_token = 'abd82c4f43d2eea6efee3bc90bd0f99a'
        client = Client(account_sid, auth_token)
        message = client.messages .create(
                            body =  "Target{}".format(status),  #Message you send
                            from_ = "+14158535945",    #Provided phone number
                            to =    "+16262785462") #Your phone number
        message.sid

    time.sleep(5)
