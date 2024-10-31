import random
import numpy as np

class ReinforcementLearnigAgent():
    
    def __init__(self, vehicle):
        # RL hyperparameters
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        
        self.state_indices = []
        self.tasks = []
        self.actions = None
        
        self.nember_of_task_sizes = 3
        self.number_of_execution_times = 3
        self.max_queue_length = 10
        self.vehicle = vehicle

        self.actions = [0, 1] # 0 for local execution and  for offloading and 
        self.q_table = np.zeros((self.nember_of_task_sizes, self.number_of_execution_times, self.max_queue_length, len(self.actions)))
        
        
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
        if 0 <= queue_length and  queue_length <= self.max_queue_length:
            return int(queue_length)
        else:
            raise ValueError(f"Invalid queue length: {queue_length}")

    def discretize_state(self, state_values):
        task_size_state = self.discretize_task_size(state_values['task_size'])
        execution_time_state = self.discretize_execution_time(state_values['execution_time'])
        queue_length_state = self.discretize_queue_length(state_values['queue_length'])
        return (task_size_state, execution_time_state, queue_length_state)

    def choose_action(self, task, queue_length):#state_indices
        
        state_indices = (self.discretize_task_size(task.size),
                         self.discretize_execution_time(task.execution_time),
                         self.discretize_queue_length(queue_length))
        self.current_state_indices = state_indices
        
        if self.prvious_state_indices is not None:
            self.update_q_tabel()
        self.prvious_state_indices = state_indices
            
        if np.random.rand() < self.epsilon:
            action = np.random.choice(self.actions)
        else:
            np.argmax(self.q_table[state_indices])
        self.previous_action = action #for update_q_table later
        return action
    
    def update_q_tabel(self):
        reward = -self.previous_task.execution_time  # negative reward for execution time
        current_q = self.q_table[self.prvious_state_indices][self.previous_action]
        max_future_q = np.max(self.q_table[self.current_state_indices])
        new_q = current_q + self.alpha * (reward + self.gamma * max_future_q - current_q)
        self.q_table[self.prvious_state_indices][self.previous_action] = new_q
        print(self.q_table)
    
    def store_previous_task(self, task):
        self.previous_task = task

    
