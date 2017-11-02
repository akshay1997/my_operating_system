import plot
from operator import itemgetter
from copy import deepcopy
def simple_scheduler(task_list):
	final_task_list=[]
	for task in task_list:
		final_task_list.append(dict(name=task['name'],start=task['entry'],finish=task['entry']+task['burst']))
	print(final_task_list)
	plot.plot_tasks(final_task_list)

def fcfs(task_list):
	final_task_list=[]
	newlist = sorted(task_list, key=itemgetter('entry')) 
	time=0
	for task in newlist:
		start_time=time
		finish_time=time+task['burst']
		final_task_list.append(dict(name=task['name'],start=start_time,finish=finish_time))
		time=finish_time
	print(final_task_list)
	plot.plot_tasks(final_task_list)

def srtf(task_list): #Preemtive
	final_task_list=[]
	task_list_temp=deepcopy(task_list)
	task_list_temp = sorted(task_list_temp, key=itemgetter('entry'))
	time=0
	while(len(task_list_temp)>0):
		min_task=None
		min_time=None
		for i in range(0,len(task_list_temp)):
			if task_list_temp[i]['entry']<=time:	
				if min_task==None:
					min_task=i
					min_time=task_list_temp[i]['burst']
				else:
					if task_list_temp[i]['burst']<min_time:
						min_time=task_list_temp[i]['burst']
						min_task=i
		if min_task==None:
			time+=1
			continue
		start_time=time
		finish_time=time+1
		final_task_list.append(dict(name=task_list_temp[min_task]['name'],start=start_time,finish=finish_time))
		time=finish_time
		task_list_temp[min_task]['burst']-=1
		if task_list_temp[min_task]['burst']==0:
			del task_list_temp[min_task]
	print(final_task_list)
	plot.plot_tasks(final_task_list)


def sjf(task_list): #Non-preemtive
	final_task_list=[]
	task_list_temp=deepcopy(task_list)
	task_list_temp = sorted(task_list_temp, key=itemgetter('entry'))
	time=0
	while(len(task_list_temp)>0):
		min_task=None
		min_time=None
		for i in range(0,len(task_list_temp)):
			if task_list_temp[i]['entry']<=time:
				if min_task==None:
					min_task=i
					min_time=task_list_temp[i]['burst']
				else:
					if task_list_temp[i]['burst']<min_time:
						min_time=task_list_temp[i]['burst']
						min_task=i
		if min_task==None:
			time+=1
			continue
		start_time=time
		finish_time=time+task_list_temp[min_task]['burst']
		final_task_list.append(dict(name=task_list_temp[min_task]['name'],start=start_time,finish=finish_time))
		time=finish_time
		del task_list_temp[min_task]

	print(final_task_list)
	plot.plot_tasks(final_task_list)