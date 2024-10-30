from reinforcement_learning_agent import ReinforcementLearnigAgent

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
        
        
    def add_task(self, application):
        self.unfinished_tasks.append(application)
        
          
    def add_finished_task(self, application):
        self.finished_tasks.append(application)
        
    def get_new_task_id(self):
        self.new_task_id += 1
        return self.new_task_id
    
    def local_execuation_check(self, time):
        task = self.runnig_task
        is_finished = task.is_finished(time)
        if is_finished:
            finished_tasks.append(task)
            task.execution_location = 0
            self.runnig_task = None
         
    def print_vehicle_info(self):
        print(f"id: {self.id}, x: {self.x}, y: {self.y}, speed: {self.speed}, direction: {self.direction}")
        print(f"undecided tasks count: {len(self.undecided_tasks)}")
        
    

