import csv
from datetime import datetime, date
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

USER = True

Province = None

if USER:
    Country = input("Please enter your country of choice in the formal style: ")

    Province = input("Specify a province or leave blank: ")
else:
    Country = "Canada"
    Province = "British Columbia"
    
#if not Province:
#    Province = None

path_to_data = "C:\\Users\\noved\\Documents\\Actual Documents\\Programming\\COVID-19\\csse_covid_19_data\\csse_covid_19_time_series\\time_series_19-covid-"
confirmedcsvpath = path_to_data + "Confirmed.csv"
deathscsvpath = path_to_data + "Deaths.csv"
recoveredcsvpath = path_to_data + "Recovered.csv"

topLine = "Province/State, Country/Region, Lat, Long, 1/22/20, 1/23/20, etc"

fig,ax = plt.subplots()

dates, cases, casesstr = [], [], []

with open(confirmedcsvpath, 'r') as confirmedcsv: # autocloses after it's finished
    myReader = csv.DictReader(confirmedcsv)
    
    fieldnamesasd = myReader.fieldnames

    for i,name in enumerate(myReader.fieldnames[4:]):
        fieldnamesasd[i+4] = datetime.strptime("0"+name, "%x").date()
        dates.append(datetime.strptime("0"+name, "%x").date())

    #dates = matplotlib.dates.date2num(fieldnamesasd)
    myReader.fieldnames = fieldnamesasd
    #print(myReader.fieldnames)


    firstRow = True
    for row in myReader:
        #row={k: v for k, v in row.items() if v is not None}
        #pass
        if not row["Country/Region"].lower() == Country.lower():
            continue
        if Province:
            Region = Province + ", " + Country
            if row["Province/State"] == Province:

                #if row["Province/State"]:
                    #print(row["Province/State"], end = ", ")

                #print(row["Country/Region"]+ ": ")
                newrow={k: v for k, v in row.items() if isinstance(k, date)}

                

                for iii, (k,v) in enumerate(newrow.items()):
                    #print(str(k), end=": ")
                    #print(v, end=": ")
                    #for i in range(0,int(int(v)/2.2)):
                    #    print("#", end="")
                    cases.append(int(v))
                    #print()
                    #if not (i%7):
                    #    print(" ")
        else:
            Region = Country
            #print(row["Country/Region"]+ ": ")
            newrow={k: v for k, v in row.items() if isinstance(k, date)}
            print(row)
            for iii, (k,v) in enumerate(newrow.items()):
                if firstRow:
                    cases.append(int(v))
                else:
                    cases[iii]+=int(v)
                
            firstRow = False
            

#ax = plt.subplot(111)
#ax.bar(dates, cases, width=0.5)
#ax.xaxis_date()

plt.scatter(dates, cases)
plt.plot(dates, cases)
plt.grid()
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.title("Confirmed Cases in %s" % Region)
#plt.xlim(datetime.date.today)
plt.show()
        