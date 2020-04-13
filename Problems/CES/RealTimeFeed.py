import datetime

t = int(input())
data_dict_extra = dict()
for i in range(t):
    date_value, time_value, symbol, price = input().split(",")
    hour = time_value.split(':')[0]
    if datetime.datetime.strptime("09:30:00", "%H:%M:%S") <= \
            datetime.datetime.strptime(time_value, "%H:%M:%S") <= datetime.datetime.strptime("16:30:00", "%H:%M:%S"):

        if date_value in data_dict_extra:
            if hour not in data_dict_extra.keys():
                data_dict_extra[date_value]['hours'][hour] = 1
            else:
                data_dict_extra[date_value]['hours'][hour] += 1
            data_dict_extra[date_value]['count'] += 1
            if symbol not in data_dict_extra[date_value]['symbol']:
                data_dict_extra[date_value]['symbol'][symbol] = {'count': 1, 'max_price': price, 'min_price': price,
                                                                 'time': time_value}
            else:
                data_dict_extra[date_value]['symbol'][symbol]['count'] += 1
                data_dict_extra[date_value]['symbol'][symbol]['time'] = time_value
                if price > data_dict_extra[date_value]['symbol'][symbol]['max_price']:
                    data_dict_extra[date_value]['symbol'][symbol]['max_price'] = price
                if price < data_dict_extra[date_value]['symbol'][symbol]['min_price']:
                    data_dict_extra[date_value]['symbol'][symbol]['min_price'] = price

        else:

            data_dict_extra[date_value] = dict()
            data_dict_extra[date_value]['hours'] = dict()
            data_dict_extra[date_value]['symbol'] = dict()
            if hour not in data_dict_extra[date_value].keys():
                data_dict_extra[date_value]['count'] = 1
                data_dict_extra[date_value]['hours'][hour] = 1
                data_dict_extra[date_value]['symbol'][symbol] = {'count': 1, 'max_price': price, 'min_price': price,
                                                                 'time': time_value}
        data_dict_extra[date_value]['last'] = time_value

print(data_dict_extra)

for key, values in data_dict_extra.items():
    print('Trading Day = ', key)
    print('Last Quote Time = ', values['last'])
    print('Number of valid quotes = ', values['count'])
    print("Most active hour = ", max(values['hours'], key=values['hours'].get))
    most_active_symbol_value = None
    most_active_symbol = None

    for k, v in values['symbol'].items():
        if most_active_symbol_value is None:
            most_active_symbol, most_active_symbol_value = k, v['count']
        else:

            if v['count'] == most_active_symbol_value:
                if k < most_active_symbol:
                    most_active_symbol, most_active_symbol_value = k, v['count']
            elif v['count'] > most_active_symbol_value:
                most_active_symbol, most_active_symbol_value = k, v['count']

    print("Most active hour = ", most_active_symbol)
    for k, v in values['symbol'].items():
        print(key, '', v['time']+','+k+','+v['max_price']+','+v['min_price'])
