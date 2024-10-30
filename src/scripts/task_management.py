    
    
def vehicles_task_generation(vehicles, time):
    for vehicle in vehicles:
        vehicle.generate_task(time)



def manage_runnig_task(vehicles, edge_servers, time):


    for vehicle in vehicles:
        vehicle.local_execuation_check(time)
        
        for tasks in vehicle.undecided_tasks:
            for task in tasks:
                action = vehicle.agent.decide(task)
                vehicle.undecided.remove(task)
                if(action == 0):
                    vehicle.local_execution_queue.append(task)
                elif(action == 1):
                    # edge_server = get_inrange_edge_server(vehicle.x, vehicle.y)
                    # edge_server.server.channel.append(task)
                    print('decided on offloading')

    # for edge_server in edge_servers:
    #     edge_server.check_channel(time)
    #     edge_server.
        