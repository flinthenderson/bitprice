import pandas as pd
from matplotlib import pyplot as plt
import datetime

with open('records.csv', 'r') as records:
    df = pd.read_csv(records)
    time_seq = df['time'].tolist()
    dt_list = []
    #print(time_seq)
    for string in time_seq:
        dt_obj = datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S.%f')
        dt_list.append(dt_obj)
    print(dt_list)
    price_seq = df['price'].tolist()
    print(price_seq)

    plt.plot(dt_list, price_seq)
    plt.show()
