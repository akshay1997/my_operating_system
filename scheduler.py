import plot
from operator import itemgetter
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
	return None
def sjf(task_list): #Non-preemtive
	return None