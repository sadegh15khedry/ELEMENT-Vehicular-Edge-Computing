class EdgeServer:
    def __init__(self, id, x, y):
        self.id = id
        self.runnig_task = None
        self.x = x
        self.y = y
        self.task_queue = []
        
    def print_edge_server_info(self):
        print(f"Edge server Id: {self.id}, x:{self.x}, y:{self.y}")

        
