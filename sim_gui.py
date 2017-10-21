from appJar import gui
import scheduler
def num_tasks_press(btn):
    num_tasks=app.getEntry('num_tasks_entry')
    print(num_tasks)
    generate_task_details_column(int(num_tasks))

def task_details_press(btn):
    num_tasks=app.getEntry('num_tasks_entry')
    total_memory=app.getEntry('total_memory_entry')
    task_details=[]
    for i in range(0,int(num_tasks)):
        entry=app.getEntry('entry_time'+str(i)+"_entry")
        burst=app.getEntry('burst_time'+str(i)+"_entry")
        memory=app.getEntry('memory'+str(i)+"_entry")
        task_details.append(dict(name='Task '+str(i),entry=entry,burst=burst,memory=memory))
    print(task_details)
    scheduler.simple_scheduler(task_details)
    app.addImage("Simple Scheduler", "simple.png")
    app.zoomImage("Simple Scheduler", -2)


def generate_task_details_column(num_tasks):
    app.addLabel("total_memory_label","Enter total memory of system")
    app.addNumericEntry('total_memory_entry')
    for i in range(0,num_tasks):
        app.addLabel("task"+str(i)+"_label","TASK"+str(i))
        app.addLabel("entry"+str(i)+"_label","Enter entry time")
        app.addNumericEntry('entry_time'+str(i)+"_entry")
        app.addLabel("burst_time"+str(i)+"_label","Enter burst time")
        app.addNumericEntry('burst_time'+str(i)+"_entry")
        app.addLabel("memory"+str(i)+"_label","Enter memory")
        app.addNumericEntry('memory'+str(i)+"_entry")
    app.addNamedButton('Enter','task_details_btn',task_details_press)

app=gui()
app.addLabel("num_tasks_label","Number of tasks")
app.addNumericEntry('num_tasks_entry')
app.addNamedButton('Enter','num_task_btn',num_tasks_press)
app.go()