import random
import numpy as np

class ReinforcementLearnigAgent():
    
    def __init__(self, vehicle, nember_of_task_sizes, number_of_execution_times, max_queue_lenght):
        # RL hyperparameters
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilin = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.epsilon = 10000
        
        # Actions: 0 for local execution, 1 for offloading
        self.actions = [0, 1] # 0 for local execution and  for offloading and 
        state = ()
        reward = 0
        accumulate_reward = 0
        q_values = []
        
        self.vehicle = vehicle
        self.nember_of_task_sizes = nember_of_task_sizes
        self.number_of_execution_times = number_of_execution_times
        self.max_queue_lenght = max_queue_lenght
        
        self.q_table = np.zeros((nember_of_task_sizes, self.number_of_execution_times, self.max_queue_lenght, len(self.actions)))
        
        
    def discretize_task_size(self, task_size):
        if task_size == 0.5:
            return 0
        elif task_size == 5:
            return 1
        elif task_size == 50:
            return 2
        else:
            raise ValueError(f"Invalid task size: {task_size}")
        
    def discretize_execution_time(self, execution_time):
        if execution_time == 5:
            return 0
        elif execution_time == 50:
            return 1
        elif execution_time == 500:
            return 2
        else:
            raise ValueError(f"Invalid execution time: {execution_time}")

    def discretize_queue_length(self, queue_length):
        if 0 <= queue_length <= self.max_queue_length:
            return int(queue_length)
        else:
            raise ValueError(f"Invalid queue length: {queue_length}")

    def discretize_state(self, state_values):
        task_size_state = self.discretize_task_size(state_values['task_size'])
        execution_time_state = self.discretize_execution_time(state_values['execution_time'])
        queue_length_state = self.discretize_queue_length(state_values['queue_length'])
        return (task_size_state, execution_time_state, queue_length_state)

    def choose_action(self, state_indices):
        if np.random.rand() < self.epsilon:
            action = np.random.choice(self.actions)
        else:
            np.argmax(self.q_table[state_indices])
        return action
    
    def update_q_tabel(self, state_indices, action, reward, next_state_indices):
        current_q = self.q_table[state_indices][action]
        max_future_q = np.max(self.q_table[next_state_indices])
        new_q = current_q + self.alpha * (reward + self.gamma * max_future_q - current_q)
        self.q_table[state_indices][action] = new_q
    
    def train(self):
        # for episode in range(self.episodes):
        state_values = self.vehicle.reset()
        done = False
        while not done:
            state_indices = self.discretize_state(state_values)
            action = self.choose_action(state_indices)
            next_state_values, reward, done = self.vehicle.step(action)
            next_state_indices = self.discretize_state(next_state_values)
            self.update_q_table(state_indices, action, reward, next_state_indices)
            state_values = next_state_values
            # Decay epsilon
            if self.epsilon > self.epsilon_min:
                self.epsilon *= self.epsilon_decay
            # Optional: Print progress
            # if (episode + 1) % 100 == 0:
            #     print(f"Episode {episode + 1}/{self.episodes}, Epsilon: {self.epsilon:.3f}")
                
    # def find_inrange_edge_server(vehicle, edge_servers):
    #     edge_server = edge_servers[0]
    #     return edge_server    
    # def manage_offloading(vehicles, edge_servers, algorithm):
    #     if algorithm == "greedy_local":
    #         print ("Greedy Local Offloading Algorithm")
    #     elif algorithm == "random":
    #         print ("Random")
    #     elif algorithm == "greedy_offloading":
    #         print ("Greedy Offloading Algorithm")
    #     elif algorithm == "Q-learning":
    #         print ("Q-Learning")
    #         for vehicle in vehicles:
    #             edge_server = find_inrange_edge_server(vehicle, edge_servers)
    #             q_learning_algorithm(vehicles, edge_server)
