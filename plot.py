import plotly.plotly as py
import plotly.figure_factory as ff
import time_functions

def plot_tasks(task_list):  #task_list is a list of dictionaries containing name,start and finish in relative seconds
    now_seconds=time_functions.get_current_sec()
    df=[]
    for task in task_list:
        task_name=task['name']    
        start_time=time_functions.get_real_time(now_seconds+task['start'])
        finish_time=time_functions.get_real_time(now_seconds+task['finish'])
        df.append(dict(Task=task_name, Start=start_time, Finish=finish_time))
    print(df)
    fig = ff.create_gantt(df,group_tasks=True)
    url=py.plot(fig, filename='gantt-simple-gantt-chart', world_readable=True, auto_open=False)  
    url=url[30:]
    print(url)
    fig = py.get_figure('udayakumar97', url)
    py.image.save_as(fig,'simple.png')

