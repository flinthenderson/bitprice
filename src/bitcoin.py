import requests
import datetime
import json
import csv
import pandas as pd
import time
import os

bitcoin_api_url = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"
w = csv.writer(open('records.csv', 'a'))

def speak_btc(price, previous_price):
    price = float(price)//1
    previous_price = int(float(previous_price))//1
    if previous_price != -1:
        if price > prev_price:
            os.system('say ' + f'Bitcoin is up {price - previous_price}')
        if price < prev_price:
            os.system('say ' + f'Bitcoin is down {previous_price - price}')
        else:
            pass
            #os.system('say ' + f'Bitcoin is unchanged')
    else:
        os.system('say ' + f'Bitcoin is now {price}')


def check_price():
    response = requests.get(bitcoin_api_url)
    response_json = response.json()
    current_price  = response_json[0]['price_usd']
    current_time = datetime.datetime.now()
    print(current_time, ' - ', current_price)
    return current_time, current_price

if __name__ == "__main__":
    history = {}
    prev_price = -1
    for i in range(1000): #5 hours
            time_c, price = check_price()
            price = int(float(price))
            history.update({time_c: price})
            speak_btc(price, prev_price)
            prev_price = price
            time.sleep(10) #60 seconds
    for time, price in history.items():
        w.writerow([time, price])
    print("Done!")
