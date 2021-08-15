history=open("history.txt","r")
print_speed=open("print_speed.txt","w")

time=history.readlines()
time1=time[0].split(',')[1][:-2]
time2=time[-2].split(',')[1][:-2]

metrics=float(time2)-float(time1))/len(time))