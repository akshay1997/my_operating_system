from appJar import gui
import scheduler
import random
import string

def id_generator(size=6, chars=string.ascii_lowercase): #generate the random string of n size and from given sentence
    return ''.join(random.choice(chars) for _ in range(size))

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
    try:
        app.destroySubWindow("gannt-chart")
    except Exception as ex:
        print(ex)
    app.startSubWindow("gannt-chart")
    image_window_name=id_generator()
    app.addImage(image_window_name, "simple.png")
    app.stopSubWindow()
    app.showSubWindow("gannt-chart")
    
    


def generate_task_details_column(num_tasks):
    app.addLabel("total_memory_label","Enter total memory of system",1,0)
    app.addNumericEntry('total_memory_entry',1,1)
    for i in range(0,num_tasks):
        app.addLabel("task"+str(i)+"_label","TASK"+str(i),i+2,0)
        app.addLabel("entry"+str(i)+"_label","Enter entry time",i+2,1)
        app.addNumericEntry('entry_time'+str(i)+"_entry",i+2,2)
        app.addLabel("burst_time"+str(i)+"_label","Enter burst time",i+2,3)
        app.addNumericEntry('burst_time'+str(i)+"_entry",i+2,4)
        app.addLabel("memory"+str(i)+"_label","Enter memory",i+2,5)
        app.addNumericEntry('memory'+str(i)+"_entry",i+2,6)
    app.addNamedButton('Enter','task_details_btn',task_details_press)

app=gui()
app.addLabel("num_tasks_label","Number of tasks",0,0)
app.addNumericEntry('num_tasks_entry',0,1)
app.addNamedButton('Enter','num_task_btn',num_tasks_press,0,2)
app.go()