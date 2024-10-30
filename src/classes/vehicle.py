from reinforcement_learning_agent import ReinforcementLearnigAgent
from task import Task
class Vehicle:
    def __init__(self, id, x, y, speed, direction):
        self.id = id
        self.x = x
        self.y = y
        self.new_task_id = 0
        self.speed = speed
        self.direction = direction
        self.runnig_task = None
        self.local_execution_queue = []
        self.unfinished_offload_tasks = []
        self.undecided_tasks = []
        self.finished_tasks = []
        self.agent = ReinforcementLearnigAgent(self)
        
 
    def generate_task(self, time):
        task = Task(self.get_new_task_id(), self.id, time, 5, 5)
        self.undecided_tasks.append(task)
        task.print_task_info()
           
        
        
    def get_new_task_id(self):
        self.new_task_id += 1
        return self.new_task_id
    
    def is_busy(self, time):
        task = self.runnig_task
        if task == None:
            return False
        
        is_finished = task.is_finished(time)
        if is_finished:
            self.finished_tasks.append(task)
            self.runnig_task = None
            return False
        return True
         
    def run_new_task(self, time):
        if self.local_execution_queue and self.runnig_task is None:
            task = self.local_execution_queue.pop(0)
            task.start_time = time
            self.runnig_task = task
    
    def print_vehicle_info(self):
        print(f"id: {self.id}, x: {self.x}, y: {self.y}, speed: {self.speed}, direction: {self.direction}")
        print(f"undecided tasks count: {len(self.undecided_tasks)}")
    
        
    def find_closest_edge_server(self, edge_servers):
        min_distance = float('inf')
        closest_server = None
        for server in edge_servers:
            distance = ((server.x - self.x)**2 + (server.y - self.y)**2)**0.5
            if distance < min_distance:
                min_distance = distance
                closest_server = server
        return closest_server
        
    

