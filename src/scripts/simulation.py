import sys
import os
import time

from vehicle_movement import vehicle_movement_funciton
from task_management import manage_tasks, generate_tasks
from initialization import load_config, initialize_edge_servers, initialize_vehicles, load_mobility_csv

class Simulation:
    def __init__(self, algorithm, time_step_length, max_iterations, mobility_file_path, mode, edge_file_path, vehicle_file_path):
        self.mode = mode
        self.edge_servers = initialize_edge_servers(edge_file_path)
        self.vehicles = initialize_vehicles(vehicle_file_path)
        self.start_time = 0
        self.finish_time = 0
        self.algorithm = algorithm
        self.iteration_count = 1
        self.time_step_length = time_step_length
        self.max_iterations = max_iterations
        self.mobilty_file = load_mobility_csv(mobility_file_path)
        
    
    
    # def initialize_vehicles(self):
    def run(self):
        print("Running simulation stated!")
        self.start_time = time.time()
        
        
        while self.iteration_count <= self.max_iterations:
            # iteration_start_time = time.time()
            print(f"Iteration: {self.iteration_count} started  ----------------------------------------------------------------")
            
            if(self.iteration_count % 20 == 1):
                generate_tasks(self.vehicles, self.iteration_count)
            vehicle_movement_funciton(self.vehicles, self.iteration_count, self.mobilty_file)
            manage_tasks(self.vehicles, self.edge_servers, self.iteration_count)

            
            time.sleep(self.time_step_length)
            print(f"Iteration: {self.iteration_count} ended ----------------------------------------------------------------")
            self.iteration_count += 1

        # self.finish_time = time.time()
        print(f"Simulation finished! Total iterations: {self.iteration_count}.")
