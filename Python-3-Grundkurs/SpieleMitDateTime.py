import time
import datetime

print("Module time")
'''anzahl der sekunden die seit dem 1.1.1970 verstrichen sind'''
t=time.time()
print(t)

'''aktuelles datum als string'''
t=time.asctime()
print(t)

'''aktuelles datum als structime'''
t=time.localtime()
print(t)

'''datum mit aktuellen tag als structime'''
t=time.localtime()
print(t.tm_mday)
print(t.tm_mon)
print(t.tm_year)

'''datum zusammengebaut als structime'''
t=time.localtime()
print("{0:02d}.{1:02d}.{2:02d}".format(t.tm_mday,t.tm_mon,t.tm_year))

print("Module Datetime")

'''ami datum'''
datum=datetime.date.today()
print(datum)

'''deutsches datum'''
datum=datetime.date.today()
print(str(datum.day)+"."+str(datum.month)+"."+str(datum.year))

'''datum manuell setzen'''
datum=datetime.date(2020,4,1)
print(str(datum.day)+"."+str(datum.month)+"."+str(datum.year))

'''datum umschreiben'''
datum=datetime.date(2020,4,1)
datum=datum.replace(month=5)
print(str(datum.day)+"."+str(datum.month)+"."+str(datum.year))

'''uhrzeit verhält sich gleich'''
zeit=datetime.time(10,20,00)
print(zeit)
zeit=zeit.replace(hour=15)
print(zeit)

'''zeitstempel erstellen und abziehen'''
zeitstempel1=datetime.datetime(2020,6,1,10,15,0)
print(zeitstempel1)
zeitstempel2=datetime.datetime.now()
print(zeitstempel2)
print(zeitstempel2-zeitstempel1)

