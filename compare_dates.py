time=[]
dt = datetime.datetime.now()
time1 = datetime.datetime(2019, 11, 1)
time2 = datetime.datetime(2020, 3, 30)
time.append(time1)
time.append(time2)
print(time1)
print(time2)
print(time2 - (datetime.timedelta(30)))
past_thirty = time2 - (datetime.timedelta(30))

for x in time:

  if(x <= time2 and x >= past_thirty):
    print(str(x) + " this time is in range")
  else:
    print(str(x) + " this time not in range")