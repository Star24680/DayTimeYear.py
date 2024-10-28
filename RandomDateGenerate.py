import random 
import time
def RandomeDate(startdate,enddate):
    print("Printing random date between ",startdate, "and" ,enddate)
    Randomgenerator=random.random()
    dateformat='%m/%d/%Y'
    starttime=time.mktime(time.strptime(startdate,dateformat))
    Endtime=time.mktime(time.strptime(enddate,dateformat))
    randomtime=starttime+Randomgenerator*(Endtime-starttime)
    randomDate=time.strftime(dateformat,time.localtime(randomtime))
    return randomDate
print("randomDate=",RandomeDate("1/1/2016","12/12/2018")) 
                             