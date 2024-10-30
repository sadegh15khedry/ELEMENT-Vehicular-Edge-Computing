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
        self.undecided_tasks = []
        self.finished_tasks = []
        self.agent = ReinforcementLearnigAgent(self)
        
 
    def generate_task(self, time):
        task = Task(self.get_new_task_id(), self.id, time,10, 10)
        self.undecided_tasks.append(task)
        task.print_task_info()
           
    def add_task(self, application):
        self.unfinished_tasks.append(application)
        
          
    def add_finished_task(self, application):
        self.finished_tasks.append(application)
        
    def get_new_task_id(self):
        self.new_task_id += 1
        return self.new_task_id
    
    def execuation_check(self, time):
        task = self.runnig_task
        is_finished = task.is_finished(time)
        if is_finished:
            self.finished_tasks.append(task)
            task.execution_location = 0
            self.runnig_task = None
         
    def assign_new_task_in_vehicle(self, time):
        if self.unfinished_tasks and self.runnig_task is None:
            task = self.unfinished_tasks.pop(0)
            task.start_time = time
            self.runnig_task = task
    
    def print_vehicle_info(self):
        print(f"id: {self.id}, x: {self.x}, y: {self.y}, speed: {self.speed}, direction: {self.direction}")
        print(f"undecided tasks count: {len(self.undecided_tasks)}")
        
    

