from appJar import gui
import scheduler
import random
import string
from memory import ff,bf,wf
from plot import plot_memory
from scheduler import fcfs,srtf,sjf


def id_generator(size=6, chars=string.ascii_lowercase): #generate the random string of n size and from given sentence
    return ''.join(random.choice(chars) for _ in range(size))

def back_press(btn):
    begin()

def choice_press(btn):
    global choice
    choice=app.getRadioButton('choice_radio')
    app.removeAllWidgets()
    app.addNamedButton('Back','back_btn',back_press,0,0)
    if choice=='Process Scheduler':
        process_scheduler()
    elif choice=='Memory Management':
        memory_management()
    else:
        process_and_memory_management()

def process_and_memory_management():    
    memory_management()

def memory_management():
    app.addLabel("num_pages_label","Number of pages",1,0)
    app.addNumericEntry('num_pages_entry',1,1)
    app.addNamedButton('Enter','num_pages_btn',num_pages_memory_press,1,2)

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
    app.addLabel("num_tasks_label","Number of tasks",1,0)
    app.addNumericEntry('num_tasks_entry',1,1)
    app.addNamedButton('Enter','num_task_btn',num_tasks_scheduler_press,1,2)

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
    scheduler_algo=app.getRadioButton('scheduler_algo')
    task_details=[]
    for i in range(0,int(num_tasks)):
        entry=app.getEntry('entry_time'+str(i)+"_entry")
        burst=app.getEntry('burst_time'+str(i)+"_entry")
        #priority=app.getEntry('priority'+str(i)+"_entry")
        task_details.append(dict(name='Task '+str(i),entry=entry,burst=burst))
    print(task_details)
    if scheduler_algo=='FCFS':
        fcfs(task_details)
    elif scheduler_algo=='SRTF':
        srtf(task_details)
    else:
        sjf(task_details)
    gannt_window_name=id_generator()
    gannt_image_name=id_generator()
    app.startSubWindow(gannt_window_name)
    app.addImage(gannt_image_name, "simple.png")
    app.stopSubWindow()
    app.showSubWindow(gannt_window_name)

def task_details_memory_press(btn):
    num_tasks=app.getEntry('num_tasks_entry')
    global task_details
    task_details=[]
    for i in range(0,int(num_tasks)):
        memory=app.getEntry('memory'+str(i)+"_entry")
        task_details.append(dict(name='Task '+str(i),memory=memory))
    print(task_details)
    num_pages=app.getEntry('num_pages_entry')
    global page_details
    page_details=[]
    for i in range(0,int(num_pages)):
        page_memory=app.getEntry('page_memory'+str(i)+"_entry")
        page_details.append(dict(name='Page '+str(i),memory=page_memory))
    print(page_details)
    choice=app.getRadioButton('memory_algo')
    if choice == 'First Fit':
        print('Doing first fit')
        task_list,mapping=ff(task_details,page_details)
    elif choice =='Best Fit':
        print('Doing best fit')
        task_list,mapping=bf(task_details,page_details)
    else:
        print('Doing worst fit')
        task_list,mapping=wf(task_details,page_details)
    print(task_list)
    print (mapping)
    op=plot_memory(task_list,mapping)
    if op==True:
        chart_window_name=id_generator()
        chart_image_name=id_generator()
        app.startSubWindow(chart_window_name)
        app.addImage(chart_image_name, "bar.png")
        app.stopSubWindow()
        app.showSubWindow(chart_window_name)
    
    
    
    #app.setRadioButtonChangeFunction("memory_algo", memory_choice_press)

    

    '''
    scheduler.simple_scheduler(task_details)
    gannt_window_name=id_generator()
    gannt_image_name=id_generator()
    app.startSubWindow(gannt_window_name)
    app.addImage(gannt_image_name, "simple.png")
    app.stopSubWindow()
    app.showSubWindow(gannt_window_name)
    '''

def task_details_both_press(btn):
    num_tasks=app.getEntry('num_tasks_entry')
    global task_details
    task_details=[]
    for i in range(0,int(num_tasks)):
        entry=app.getEntry('entry_time'+str(i)+"_entry")
        burst=app.getEntry('burst_time'+str(i)+"_entry")
        memory=app.getEntry('memory'+str(i)+"_entry")
        task_details.append(dict(name='Task '+str(i),memory=memory,entry=entry,burst=burst))
    print(task_details)
    num_pages=app.getEntry('num_pages_entry')
    global page_details
    page_details=[]
    for i in range(0,int(num_pages)):
        page_memory=app.getEntry('page_memory'+str(i)+"_entry")
        page_details.append(dict(name='Page '+str(i),memory=page_memory))
    print(page_details)
    choice=app.getRadioButton('memory_algo')
    if choice == 'First Fit':
        print('Doing first fit')
        task_list,mapping=ff(task_details,page_details)
    elif choice =='Best Fit':
        print('Doing best fit')
        task_list,mapping=bf(task_details,page_details)
    else:
        print('Doing worst fit')
        task_list,mapping=wf(task_details,page_details)
    print(task_list)
    print (mapping)
    op=plot_memory(task_list,mapping)
    if op==True:
        chart_window_name=id_generator()
        chart_image_name=id_generator()
        app.startSubWindow(chart_window_name)
        app.addImage(chart_image_name, "bar.png")
        app.stopSubWindow()
        app.showSubWindow(chart_window_name)

        scheduler_algo=app.getRadioButton('scheduler_algo')
        if scheduler_algo=='FCFS':
            fcfs(task_list)
        elif scheduler_algo=='SRTF':
            srtf(task_list)
        else:
            sjf(task_list)
        gannt_window_name=id_generator()
        gannt_image_name=id_generator()
        app.startSubWindow(gannt_window_name)
        app.addImage(gannt_image_name, "simple.png")
        app.stopSubWindow()
        app.showSubWindow(gannt_window_name)
    else:
        print('Not enough memory to execute any task')
    
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
            #app.addLabel("priority"+str(i)+"_label","Enter priority",curr_row+i,5)
            #app.addNumericEntry('priority'+str(i)+"_entry",curr_row+i,6)
        elif event==2:
            app.addLabel("task"+str(i)+"_label","TASK"+str(i),curr_row+i,0)
            app.addLabel("memory"+str(i)+"_label","Enter memory",curr_row+i,1)
            app.addNumericEntry('memory'+str(i)+"_entry",curr_row+i,2)
        else:
            app.addLabel("task"+str(i)+"_label","TASK"+str(i),curr_row+i,0)
            app.addLabel("entry"+str(i)+"_label","Enter entry time",curr_row+i,1)
            app.addNumericEntry('entry_time'+str(i)+"_entry",curr_row+i,2)
            app.addLabel("burst_time"+str(i)+"_label","Enter burst time",curr_row+i,3)
            app.addNumericEntry('burst_time'+str(i)+"_entry",curr_row+i,4)
            #app.addLabel("priority"+str(i)+"_label","Enter priority",curr_row+i,5)
            #app.addNumericEntry('priority'+str(i)+"_entry",curr_row+i,6)
            app.addLabel("memory"+str(i)+"_label","Enter memory",curr_row+i,5)
            app.addNumericEntry('memory'+str(i)+"_entry",curr_row+i,6)
            

    if event==1:
        app.addLabel("choice_scheduler_label","Choose Scheduling Algorithm:",curr_row+num_tasks,0)
        app.addRadioButton("scheduler_algo", "FCFS",curr_row+num_tasks,1)
        app.addRadioButton("scheduler_algo", "SJF",curr_row+num_tasks,2)
        app.addRadioButton("scheduler_algo", "SRTF",curr_row+num_tasks,3)
        app.addNamedButton('Enter','task_details_scheduler_btn',task_details_scheduler_press,curr_row+num_tasks,4)
    elif event==2:
        app.addLabel("mem_algo_label","Choose memory algorithm:",curr_row,0)
        app.addRadioButton("memory_algo","First Fit",curr_row,1)
        app.addRadioButton("memory_algo","Best Fit",curr_row,2)
        app.addRadioButton("memory_algo","Worst Fit",curr_row,3)
        app.addNamedButton('Enter','task_details_memory_btn',task_details_memory_press,curr_row+num_tasks,0)
    else:
        app.addLabel("choice_scheduler_label","Choose Scheduling Algorithm:",curr_row+num_tasks,0)
        app.addRadioButton("scheduler_algo", "FCFS",curr_row+num_tasks,1)
        app.addRadioButton("scheduler_algo", "SJF",curr_row+num_tasks,2)
        app.addRadioButton("scheduler_algo", "SRTF",curr_row+num_tasks,3)
        app.addLabel("mem_algo_label","Choose memory algorithm:",curr_row+num_tasks+1,0)
        app.addRadioButton("memory_algo","First Fit",curr_row+num_tasks+1,1)
        app.addRadioButton("memory_algo","Best Fit",curr_row+num_tasks+1,2)
        app.addRadioButton("memory_algo","Worst Fit",curr_row+num_tasks+1,3)
        app.addNamedButton('Enter','task_details_both_btn',task_details_both_press,curr_row+num_tasks+1,4)


def begin():
    app.removeAllWidgets()
    app.addLabel("choice_label","Choose operation:",0,0)
    app.addRadioButton("choice_radio", "Process Scheduler",0,1)
    app.addRadioButton("choice_radio", "Memory Management",0,2)
    app.addRadioButton("choice_radio", "Process and Memory Management",0,3)
    app.addNamedButton('Enter','choice_btn',choice_press,0,4)



app=gui()
begin()
app.go()