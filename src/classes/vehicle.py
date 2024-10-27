class Vehicle:
    def __init__(self, id, x, y, speed, direction):
        self.id = id
        self.x = x
        self.y = y
        self.new_task_id = 0
        self.speed = speed
        self.direction = direction
        self.runnig_task = None
        self.unfinished_tasks = []
        self.finished_tasks = []
        
    def add_task(self, application):
        self.unfinished_tasks.append(application)
        
          
    def add_finished_task(self, application):
        self.finished_tasks.append(application)
        
    def get_new_task_id(self):
        self.new_task_id += 1
        return self.new_task_id
         
    def print_vehicle_info(self):
        print(f"id: {self.id}, x: {self.x}, y: {self.y}, speed: {self.speed}, direction: {self.direction}")
    