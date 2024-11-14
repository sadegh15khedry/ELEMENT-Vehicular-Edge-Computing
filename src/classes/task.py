import math
class Task:
    v1=10**-3
    v2=4
    noise= 1.6*(10**-11)
    def __init__(self, id, vehicle, release_time, execution_cycles, size):
        self.id = id
        self.vehicle = vehicle
        self.release_time = release_time
        self.response_time = None
        self.transmission_time = None
        self.size = size  # in MBs
        self.execution_time = None
        self.execution_cycles = execution_cycles
        self.start_time = None
        self.end_time = None
        self.energy = 0
        self.execution_location = None

    def is_finished(self, time):
        if self.start_time + self.execution_time == time:
            self.end_time = time
            self.response_time = self.end_time - self.release_time
            return True
        return False
            
    # def print_task_info(self):
        # print(f"Task ID: {self.id}, Execution Time: {self.execution_time} seconds")

    def set_execution_time(self, frequency):
        self.execution_time = (self.execution_cycles  / frequency) * 1000
        self.execution_time = math.ceil(self.execution_time)# in milicseconds
        # print(f"Execution Time: {self.execution_time} miliseconds")
        
    def add_execution_energy(self, frequency):
        self.energy += (10**-28)*(frequency ** 2)*(self.execution_cycles) # in Joules    
    
    
    def add_transmission_energy(self, trasmission_power, bandwidth, distance):
        
        self.energy += (trasmission_power * self.size) / self.calc_transfer_rate(bandwidth,distance)  # in Joules
        
    
    def set_transmission_time(self, bandwidth, distance):
        self.transmission_time = self.size / self.calc_transfer_rate(bandwidth, distance)

    def calc_transfer_rate(self,bandwidth, distance):
        return bandwidth* math.log2(1+(Task.v1*(distance**Task.v2))/Task.noise)