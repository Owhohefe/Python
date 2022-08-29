import csv

import datetime as dt

with open('sample.csv', encoding='utf-8', newline='') as f:
    reader = enumerate(csv.reader(f))
    for i, row in reader:
        if i > 0:
            try:
                fullname = row[0].split(",")
                lastname = fullname[0].strip()
                firstname = fullname[1].strip()
                date_joined = dt.datetime.strptime(row[2],'%m/%d/%Y').date()
                birthyear = int(row[1]or 0)
                is_active = bool(row[3])
                str_balance = (row[4].replace("$","").replace(",","")).strip()
                balance = float(str_balance or 0)
   
            except:
                fullname=lastname=firstname=""
                date_joined = None
                
            print(firstname,lastname,birthyear,date_joined,is_active,balance)
print("Done!")
                
            
            
