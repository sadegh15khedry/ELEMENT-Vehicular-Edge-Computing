from vehicle import Vehicle
from edge_server import EdgeServer
import json
import pandas as pd


def load_config(config_file):
    with open(config_file) as file:
        return json.load(file)

    
def initialize_edge_servers(config):
    edge_servers = []
    for edge_server_config in config['edge_servers']:
        edge_server = EdgeServer(edge_server_config['id'], edge_server_config['x'],
                                     edge_server_config['y'],edge_server_config['frequency'])
            
        print(f"Edge Server id: {edge_server.id}, x: {edge_server.x} y: {edge_server.y}")

        edge_servers.append(edge_server)
    print(f"Initialized {len(edge_servers)} edge servers.")
    return edge_servers
    

    
def initialize_vehicles(config):
    vehicles = []
    for vehicle_config in config['vehicles']:
        vehicle = Vehicle(vehicle_config['id'], vehicle_config['x'], vehicle_config['y'],
                                vehicle_config['speed'], vehicle_config['direction'], vehicle_config['frequency'])
        print(f"vehicle id: {vehicle.id} x: {vehicle.x} y: {vehicle.y} speed: {vehicle.speed}, direction: {vehicle.direction}")
        vehicles.append(vehicle)

        print(f"Initialized {len(vehicles)} vehicles.")
        return vehicles
    
def load_mobility_csv(path):
    file = pd.read_csv(path)
    return file