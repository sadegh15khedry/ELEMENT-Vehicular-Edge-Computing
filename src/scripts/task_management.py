from task import Task

def generate_tasks(vehicle, time):
    task = Task(vehicle.get_new_task_id(), vehicle.id, time,10, 10)
    vehicle.undecided_tasks.append(task)
    task.print_task_info()
    
    
def vehicles_task_generation(vehicles, time):
    for vehicle in vehicles:
        generate_tasks(vehicle, time)


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
        vehicle.local_execuation_check(time)
        
        # assign_new_task_in_vehicle(vehicle, time)
        
    # for edge_server in edge_servers:
        # assign_new_task_to_edge_server(edge_server, time)

    for vehicle in vehicles:
        for tasks in vehicle.undecided_tasks:
            for task in tasks:
                action = vehicle.agent.decide(task)
                vehicle.undecided.remove(task)
                if(action == 0)
                    vehicle.local_execution_queue.append(task)
                elif(action == 1)
                    edge_server = get_inrange_edge_server(vehicle.x, vehicle.y)
                    edge.server.channel.append(task)
                    print('decided on offloading')
