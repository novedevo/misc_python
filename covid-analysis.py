import csv
from datetime import datetime, date
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.optimize import curve_fit

USER = False

Province = None
Overarch = None
Country = None

if USER:
    Overarch = input("Please enter a continent, 'world', or leave blank for a country/province: ")
    Country = input("Please enter your country of choice in the formal style: ")
    Province = input("Specify a province or leave blank: ")
else:
    #Overarch = "World"
    Country = "Canada"
    Province = "British Columbia"
    
#if not Province:
#    Province = None

path_to_data = "C:\\Users\\noved\\Documents\\Actual Documents\\Programming\\COVID-19\\csse_covid_19_data\\csse_covid_19_time_series\\time_series_covid19_"
confirmedcsvpath = path_to_data + "confirmed_global.csv"
deathscsvpath = path_to_data + "deaths_global.csv"
recoveredcsvpath = path_to_data + "recovered_global.csv"

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
        if Overarch and Overarch.lower() == 'world':
            pass
        elif not row["Country/Region"].lower() == Country.lower():
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
            if Country:
                Region = Country
            else:
                Region = Overarch
            #print(row["Country/Region"]+ ": ")
            newrow={k: v for k, v in row.items() if isinstance(k, date)}
            #print(row)
            for iii, (k,v) in enumerate(newrow.items()):
                if firstRow:
                    cases.append(int(v))
                else:
                    cases[iii]+=int(v)
                
            firstRow = False
            

#ax = plt.subplot(111)
#ax.bar(dates, cases, width=0.5)
#ax.xaxis_date()

def func(x, a, b, c):
    return a * np.exp(b * x) + c

xlen = range(len(dates))
x=np.array(xlen)
y=np.array(cases)
yn=func(x,0,0,0)
#np.polyfit(np.log(x+1), y, 1)

popt, pcov = curve_fit(func, x, y)

plt.scatter(dates, cases)
plt.plot(dates, cases)
#plt.plot(dates, func(x, *popt), 'r-', label="Fitted Curve")
plt.grid()
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.title("Confirmed Cases in %s" % Region)
#plt.xlim(datetime.date.today)
plt.show()
        