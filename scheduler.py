import plot
def simple_scheduler(task_list):
	final_task_list=[]
	for task in task_list:
		final_task_list.append(dict(name=task['name'],start=task['entry'],finish=task['entry']+task['burst']))
	print(final_task_list)
	plot.plot_tasks(final_task_list)