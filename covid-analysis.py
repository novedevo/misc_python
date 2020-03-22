import csv
from datetime import datetime, date
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

COUNTRY_OR_PROVINCE = 'Province'
Country = "Canada"
Province = "British Columbia"

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



    for row in myReader:
        #row={k: v for k, v in row.items() if v is not None}
        #pass
        if not row["Country/Region"] == Country:
            continue
        if COUNTRY_OR_PROVINCE == "Province":

            if row["Province/State"] == Province:

                if row["Province/State"]:
                    print(row["Province/State"], end = ", ")

                print(row["Country/Region"]+ ": ")
                newrow={k: v for k, v in row.items() if isinstance(k, date)}

                

                for iii, (k,v) in enumerate(newrow.items()):
                    #print(str(k), end=": ")
                    #print(v, end=": ")
                    #for i in range(0,int(int(v)/2.2)):
                    #    print("#", end="")
                    cases.append(int(v))
                    casesstr.append(v)
                    print()
                    #if not (i%7):
                    #    print(" ")
        elif COUNTRY_OR_PROVINCE == "Country":
            pass

#ax = plt.subplot(111)
#ax.bar(dates, cases, width=0.5)
#ax.xaxis_date()

plt.scatter(dates, cases)
plt.plot(dates, cases)
plt.grid()
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.title("Confirmed Cases in BC")
#plt.xlim(datetime.date.today)
plt.show()
        