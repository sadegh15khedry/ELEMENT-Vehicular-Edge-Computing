import sys
import os
import time

from vehicle import Vehicle
from edge_server import EdgeServer
from vehicle_movement import load_mobility_csv, vehicle_movement_funciton
# from task_management import manage_runnig_task
from task_management import vehicles_task_generation
import json

class Simulation:
    def __init__(self, config_file, algorithm, time_step, max_iterations, mobility_file_path):
        self.config = self.load_config(config_file)
        self.edge_servers = self.initialize_edge_servers()
        self.vehicles = self.initialize_vehicles()
        self.start_time = 0
        self.finish_time = 0
        self.algorithm = algorithm
        self.iteration_count = 0
        self.time_step = time_step
        self.max_iterations = max_iterations
        self.mobilty_file = load_mobility_csv(mobility_file_path)
        
    def load_config(self, config_file):
        with open(config_file) as file:
            return json.load(file)

    
    def initialize_edge_servers(self):
        edge_servers = []
        for edge_server_config in self.config['edge_servers']:
            edge_server = EdgeServer(edge_server_config['id'], edge_server_config['x'],
                                     edge_server_config['y'])
            
            print(f"Edge Server id: {edge_server.id}, x: {edge_server.x} y: {edge_server.y}")

            edge_servers.append(edge_server)
        print(f"Initialized {len(edge_servers)} edge servers.")
        return edge_servers
    

    
    def initialize_vehicles(self):
        vehicles = []
        for vehicle_config in self.config['vehicles']:
            vehicle = Vehicle(vehicle_config['id'], vehicle_config['x'], vehicle_config['y'],
                                    vehicle_config['speed'], vehicle_config['direction'])
            print(f"vehicle id: {vehicle.id} x: {vehicle.x} y: {vehicle.y} speed: {vehicle.speed}, direction: {vehicle.direction}")
            vehicles.append(vehicle)

        print(f"Initialized {len(vehicles)} vehicles.")
        return vehicles
    
    # def initialize_vehicles(self):
    def run(self):
        print("Running simulation stated!")
        self.start_time = time.time()

        while self.iteration_count <= self.max_iterations:
            iteration_start_time = time.time()
            self.iteration_count += 1
            print(f"Iteration: {self.iteration_count} started at {iteration_start_time} ----------------------------------------------------------------")
            
            vehicles_task_generation(self.vehicles, self.iteration_count)
            vehicle_movement_funciton(self.vehicles, self.iteration_count, self.mobilty_file)
            # manage_runnig_task(self.vehicles, self.edge_servers, self.iteration_count)
            # manage_runnig_task(self.algorithm, self.vehicles, self.edge_servers)
            
            time.sleep(self.time_step)
            print(f"Iteration: {self.iteration_count} started at {iteration_start_time} ----------------------------------------------------------------")

        self.finish_time = time.time()
        print(f"Simulation finished! Total execution time: {self.finish_time - self.start_time} seconds.")
