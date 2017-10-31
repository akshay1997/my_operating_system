from copy import deepcopy
def ff(task_details,page_details):
    task_details_temp=deepcopy(task_details)
    page_details_temp=deepcopy(page_details)
    mapping={}
    task_list=[]
    for task in task_details_temp:
        for page in page_details_temp:
            if page['memory']>=task['memory']:
                mapping[task['name']]=page
                page['memory']-=task['memory']
                task_list.append(task)
                break
    return task_list,mapping

def bf(task_details,page_details):
    task_details_temp=deepcopy(task_details)
    page_details_temp=deepcopy(page_details)
    mapping={}
    task_list=[]
    for task in task_details_temp:
        save_page=None
        min_memory=None
        for page in page_details_temp:
            if page['memory']>=task['memory']:
                if min_memory==None or page['memory']-task['memory']<min_memory:
                    min_memory=page['memory']-task['memory']
                    save_page=page

        mapping[task['name']]=save_page
        save_page['memory']-=task['memory']
        task_list.append(task)
                
    return task_list,mapping

def wf(task_details,page_details):
    task_details_temp=deepcopy(task_details)
    page_details_temp=deepcopy(page_details)
    mapping={}
    task_list=[]
    for task in task_details_temp:
        save_page=None
        max_memory=None
        for page in page_details_temp:
            if page['memory']>=task['memory']:
                if max_memory==None or page['memory']-task['memory']>max_memory:
                    max_memory=page['memory']-task['memory']
                    save_page=page
        if save_page!=None:
            mapping[task['name']]=save_page
            save_page['memory']-=task['memory']
            task_list.append(task)
                
    return task_list,mapping

