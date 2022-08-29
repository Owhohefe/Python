import json

import xlrd

import datetime as dt

filename = 'people_from_excel.json'

with open(filename,"r",encoding="utf-8",newline="") as f:
    people = json.load(f)

#print(people)

for p in people:

    name=p['Full Name']
    byear = p['Birth Year']
    
    try:
        y, m, d, h, i, s = xlrd.xldate_as_tuple(p['Date Joined'],0)
        joined = dt.date(y, m, d)
        
    except Exception as e:
        print(e)
        
    balance = '$' + f"{p['Balance']:,.2f}"
    print(f"{name:<22} {byear} {joined:%m/%d/%Y} {balance:>12}")
