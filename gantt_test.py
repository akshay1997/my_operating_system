import plotly.plotly as py
import plotly.figure_factory as ff

df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
      dict(Task="Job B", Start='2009-03-05 05:00:00', Finish='2009-04-15 12:00:00'),
      dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30'),
      dict(Task="Job A", Start='2009-05-31', Finish='2009-07-28')]

fig = ff.create_gantt(df,group_tasks=True)
py.iplot(fig, filename='gantt-simple-gantt-chart', world_readable=True)
