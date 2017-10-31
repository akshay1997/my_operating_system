from appJar import gui
import scheduler
import random
import string
from memory import ff,bf,wf
from plot import plot_memory


def id_generator(size=6, chars=string.ascii_lowercase): #generate the random string of n size and from given sentence
    return ''.join(random.choice(chars) for _ in range(size))

def choice_press(btn):
    global choice
    choice=app.getRadioButton(btn)
    if choice=='Process Scheduler':
        process_scheduler()
    elif choice=='Memory Management':
        memory_management()
    else:
        process_and_memory_management()

def process_and_memory_management():
    app.removeAllWidgets()
    memory_management()

def memory_management():
    app.removeAllWidgets()
    app.addLabel("num_pages_label","Number of pages",0,0)
    app.addNumericEntry('num_pages_entry',0,1)
    app.addNamedButton('Enter','num_pages_btn',num_pages_memory_press,0,2)

def num_pages_memory_press(btn):
    num_pages=app.getEntry('num_pages_entry')
    print(num_pages)
    generate_page_details_column_memory(num_pages)

def generate_page_details_column_memory(num_pages):
    curr_row=app.getRow()
    for i in range(0,int(num_pages)):
        app.addLabel("page"+str(i)+"_label","PAGE"+str(i),curr_row+i,0)
        app.addLabel("page_memory"+str(i)+"_label","Enter memory",curr_row+i,1)
        app.addNumericEntry('page_memory'+str(i)+"_entry",curr_row+i,2)
    app.addNamedButton('Enter','page_details_btn',page_details_memory_press)

def page_details_memory_press(btn):
    curr_row=app.getRow()
    app.addLabel("num_tasks_label","Number of tasks",curr_row,0)
    app.addNumericEntry('num_tasks_entry',curr_row,1)
    app.addNamedButton('Enter','num_task_btn',num_tasks_scheduler_press,curr_row,2)


def process_scheduler():
    app.removeAllWidgets()
    app.addLabel("num_tasks_label","Number of tasks",0,0)
    app.addNumericEntry('num_tasks_entry',0,1)
    app.addNamedButton('Enter','num_task_btn',num_tasks_scheduler_press,0,2)

def num_tasks_scheduler_press(btn):
    num_tasks=app.getEntry('num_tasks_entry')
    print(num_tasks)
    global choice
    if choice=='Process Scheduler':
        generate_task_details_column(int(num_tasks),1)
    elif choice=='Memory Management':
        generate_task_details_column(int(num_tasks),2)
    else:
        generate_task_details_column(int(num_tasks),3)

def task_details_scheduler_press(btn):
    num_tasks=app.getEntry('num_tasks_entry')
    task_details=[]
    for i in range(0,int(num_tasks)):
        entry=app.getEntry('entry_time'+str(i)+"_entry")
        burst=app.getEntry('burst_time'+str(i)+"_entry")
        priority=app.getEntry('priority'+str(i)+"_entry")
        task_details.append(dict(name='Task '+str(i),entry=entry,burst=burst,priority=priority))
    print(task_details)
    scheduler.simple_scheduler(task_details)
    gannt_window_name=id_generator()
    gannt_image_name=id_generator()
    app.startSubWindow(gannt_window_name)
    app.addImage(gannt_image_name, "simple.png")
    app.stopSubWindow()
    app.showSubWindow(gannt_window_name)

def task_details_memory_press(btn):
    num_tasks=app.getEntry('num_tasks_entry')
    task_details=[]
    for i in range(0,int(num_tasks)):
        memory=app.getEntry('memory'+str(i)+"_entry")
        task_details.append(dict(name='Task '+str(i),memory=memory))
    print(task_details)
    num_pages=app.getEntry('num_pages_entry')
    page_details=[]
    for i in range(0,int(num_pages)):
        page_memory=app.getEntry('page_memory'+str(i)+"_entry")
        page_details.append(dict(name='Page '+str(i),memory=page_memory))
    print(page_details)
    curr_row=app.getRow()
    app.addLabel("mem_algo_label","Choose memory algorithm:",curr_row,0)
    app.addRadioButton("memory_algo","First Fit",curr_row,1)
    app.addRadioButton("memory_algo","Best Fit",curr_row,2)
    app.addRadioButton("memory_algo","Worst Fit",curr_row,3)
    app.setRadioButtonChangeFunction("memory_algo", memory_choice_press)

    task_list,mapping=ff(task_details,page_details)
    print(task_list)
    print(mapping)
    plot_memory(task_list,mapping)

    

    '''
    scheduler.simple_scheduler(task_details)
    gannt_window_name=id_generator()
    gannt_image_name=id_generator()
    app.startSubWindow(gannt_window_name)
    app.addImage(gannt_image_name, "simple.png")
    app.stopSubWindow()
    app.showSubWindow(gannt_window_name)
    '''
def memory_choice_press(btn):
    choice=app.getRadioButton(btn)
    if choice == 'First Fit':
        chart_window_name=id_generator()
        chart_image_name=id_generator()
        app.startSubWindow(chart_window_name)
        app.addImage(chart_image_name, "chart.png")
        app.stopSubWindow()
        app.showSubWindow(chart_window_name)

def task_details_both_press(btn):
    num_tasks=app.getEntry('num_tasks_entry')
    task_details=[]
    for i in range(0,int(num_tasks)):
        entry=app.getEntry('entry_time'+str(i)+"_entry")
        burst=app.getEntry('burst_time'+str(i)+"_entry")
        priority=app.getEntry('priority'+str(i)+"_entry")
        memory=app.getEntry('memory'+str(i)+"_entry")
        task_details.append(dict(name='Task '+str(i),memory=memory,entry=entry,burst=burst,priority=priority))
    print(task_details)
    num_pages=app.getEntry('num_pages_entry')
    page_details=[]
    for i in range(0,int(num_pages)):
        page_memory=app.getEntry('page_memory'+str(i)+"_entry")
        page_details.append(dict(name='Page '+str(i),memory=page_memory))
    print(page_details)
    '''
    scheduler.simple_scheduler(task_details)
    gannt_window_name=id_generator()
    gannt_image_name=id_generator()
    app.startSubWindow(gannt_window_name)
    app.addImage(gannt_image_name, "simple.png")
    app.stopSubWindow()
    app.showSubWindow(gannt_window_name)
    '''
    
    


def generate_task_details_column(num_tasks,event):
    curr_row=app.getRow()
    print(curr_row)
    for i in range(0,num_tasks):
        if event==1:
            app.addLabel("task"+str(i)+"_label","TASK"+str(i),curr_row+i,0)
            app.addLabel("entry"+str(i)+"_label","Enter entry time",curr_row+i,1)
            app.addNumericEntry('entry_time'+str(i)+"_entry",curr_row+i,2)
            app.addLabel("burst_time"+str(i)+"_label","Enter burst time",curr_row+i,3)
            app.addNumericEntry('burst_time'+str(i)+"_entry",curr_row+i,4)
            app.addLabel("priority"+str(i)+"_label","Enter priority",curr_row+i,5)
            app.addNumericEntry('priority'+str(i)+"_entry",curr_row+i,6)
        elif event==2:
            app.addLabel("task"+str(i)+"_label","TASK"+str(i),curr_row+i,0)
            app.addLabel("memory"+str(i)+"_label","Enter memory",curr_row+i,5)
            app.addNumericEntry('memory'+str(i)+"_entry",curr_row+i,6)
        else:
            app.addLabel("task"+str(i)+"_label","TASK"+str(i),curr_row+i,0)
            app.addLabel("entry"+str(i)+"_label","Enter entry time",curr_row+i,1)
            app.addNumericEntry('entry_time'+str(i)+"_entry",curr_row+i,2)
            app.addLabel("burst_time"+str(i)+"_label","Enter burst time",curr_row+i,3)
            app.addNumericEntry('burst_time'+str(i)+"_entry",curr_row+i,4)
            app.addLabel("priority"+str(i)+"_label","Enter priority",curr_row+i,5)
            app.addNumericEntry('priority'+str(i)+"_entry",curr_row+i,6)
            app.addLabel("memory"+str(i)+"_label","Enter memory",curr_row+i,7)
            app.addNumericEntry('memory'+str(i)+"_entry",curr_row+i,8)
            

    if event==1:
        app.addNamedButton('Enter','task_details_scheduler_btn',task_details_scheduler_press)
    elif event==2:
        app.addNamedButton('Enter','task_details_memory_btn',task_details_memory_press)
    else:
        app.addNamedButton('Enter','task_details_both_btn',task_details_both_press)

    

app=gui()
app.addLabel("choice_label","Choose operation:",0,0)
app.addRadioButton("choice_radio", "Process Scheduler",0,1)
app.addRadioButton("choice_radio", "Memory Management",0,2)
app.addRadioButton("choice_radio", "Process and Memory Management",0,3)
app.setRadioButtonChangeFunction("choice_radio", choice_press)


app.go()