import plotly.plotly as py
import plotly.figure_factory as ff

df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
      dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')]

fig = ff.create_gantt(df)
py.iplot(fig, filename='gantt-simple-gantt-chart', world_readable=True)


def plot_tasks(task_list):
    df=[]
    for task in task_list:
        task_name=task['name']
        
        df.append()