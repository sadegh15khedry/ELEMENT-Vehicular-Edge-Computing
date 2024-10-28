class Task:
    def __init__(self, id, vehicle_id, execution_time, size):
        self.id = id
        vehicle_id = vehicle_id
        self.size = size  # in MBs
        self.execution_time = execution_time
        self.start_time = None
        self.end_time = None
        self.execution_location = None

    def is_finished(self, time):
        if self.start_time + self.execution_time == time:
            self.end_time = time
            return True
        return False
            
    def print_task_info(self):
        print(f"Task ID: {self.id}, Execution Time: {self.execution_time} seconds")

