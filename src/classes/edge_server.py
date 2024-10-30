class EdgeServer:
    def __init__(self, id, x, y):
        self.id = id
        self.runnig_task = None
        self.x = x
        self.y = y
        self.task_queue = []
        self.channel = []
        self.bandwidth = 10 # ToDo update it !!!!!!!!!!!!!!
        
    def print_edge_server_info(self):
        print(f"Edge server Id: {self.id}, x:{self.x}, y:{self.y}")

    def channel_check(self, time):
        for task in self.channel:
            if time == task.release_time + int(task.size/task.bandwidth):
                self.channel.remove(task)
                self.task_queue.append(task)


        
