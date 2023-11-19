import datetime as dt
busy=[{'start':'10:30','stop':'10:50'},{'start':'18:40','stop':'18:50'},{'start':'14:40','stop':'15:50'},{'start':'16:40','stop':'17:20'},{'start':'20:05','stop':'20:20'}]
start_free,stop_free=[],[]
def parcing(busy):
    start_t,stop_t=[],[]
    for i in range(len(busy)): 
        a=busy[i]
        start_t.append(a.get('start'))
        stop_t.append(a.get('stop'))
    start_time=[] 
    stop_time=[]
    for i in range(len(start_t)):  
        time_object_start=dt.datetime.strptime(start_t[i],'%H:%M')
        time_object_stop=dt.datetime.strptime(stop_t[i],'%H:%M')
        start_time.append(time_object_start)
        stop_time.append(time_object_stop)
    start_time.sort() 
    stop_time.sort() 
    return start_time,stop_time
def time_for_free(start_time,stop_time):
    start_work=dt.datetime.strptime('9:40','%H:%M')
    stop_work=dt.datetime.strptime('23:00','%H:%M')
    n=((stop_work.hour-start_work.hour)*60)//30
    for i in range(n):
        stop_work_1=start_work+dt.timedelta(minutes=30)
        for j in range(len(start_time)):
            if start_work<=start_time[j] and stop_work_1<=start_time[j] and stop_work_1<=stop_time[j] and stop_work_1<=stop_work:
                start_free.append(start_work)
                stop_free.append(stop_work_1)
                break
            elif start_work<=start_time[j] and stop_work_1>=start_time[j] and stop_work_1>=stop_time[j] and stop_work_1<=stop_work or start_work<=start_time[j] and stop_work_1>=start_time[j] and stop_work_1<=stop_time[j] and stop_work_1<=stop_work:
                start_work=stop_time[j]
                start_free.append(start_work)
                stop_work_1=start_work+dt.timedelta(minutes=30)
                stop_free.append(stop_work_1)
                break
            elif start_work>=start_time[-1] and stop_work_1<=stop_work:
                start_free.append(start_work)
                stop_free.append(stop_work_1)
                break
            
        start_work=start_work+dt.timedelta(minutes=30)
    return start_free,stop_free 
def lst_of_times(start,stop):
    for i in range(len(start)):
        print (f'''
            Время начала приема: {start[i].time()}
            Время окончания приема: {stop[i].time()}''')
start,stop=parcing(busy)
start_free_work,stop_free_work=time_for_free(start,stop)
lst_of_times(start_free_work,stop_free_work)
        
