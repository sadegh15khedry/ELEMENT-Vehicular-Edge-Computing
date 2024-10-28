from task import Task

def generate_tasks(vehicle):
    task = Task(vehicle.get_new_task_id(), vehicle.id, 10, 10)
    task.print_task_info()
    
    
def vehicles_task_generation(vehicles):
    for vehicle in vehicles:
        generate_tasks(vehicle)


def assign_new_task_to_edge_server(edge_server, time):
    if edge_server.task_queue and edge_server.runnig_task is None:
        task = edge_server.task_queue.pop(0)
        task.start_time = time
        edge_server.runnig_task = task
    
    
def assign_new_task_in_vehicle(vehicle, time):
    if vehicle.unfinished_tasks and vehicle.unfinished_tasks is None:
        task = vehicle.unfinished_tasks.pop(0)
        task.start_time = time
        vehicle.runnig_task = task

def manage_runnig_task(vehicles, edge_servers, time):
    for vehicle in vehicles:
        assign_new_task_in_vehicle(vehicle, time)
        
    for edge_server in edge_servers:
        assign_new_task_to_edge_server(edge_server, time)
