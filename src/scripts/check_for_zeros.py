import numpy as np
import pandas as pd

def find_zeros(q_table_path):
    q_table = np.load(q_table_path+'.npy')

    print(q_table)
    indices = np.argwhere(q_table==0)
    df = pd.DataFrame(indices, columns=['task sizes state', 'execution cycles state', 'queue state','distance state', 'action'])
    return df



print("-------Q table 45 ---------")
# q_table_path = "/home/hadi/MS/persian conference/code/Computer-Science-Paper/results/q_table/45_q_table_proposed"
q_table_path ='results/q_table/45_q_table_proposed'

print(find_zeros(q_table_path))

print("-------Q table 37 ---------")
# q_table_path = "/home/hadi/MS/persian conference/code/Computer-Science-Paper/results/q_table/37_q_table_proposed"
q_table_path = 'results/q_table/37_q_table_proposed'

print(find_zeros(q_table_path))

print("-------Q table 69 ---------")
# q_table_path = "/home/hadi/MS/persian conference/code/Computer-Science-Paper/results/q_table/69_q_table_proposed"
q_table_path = 'results/q_table/69_q_table_proposed'

print(find_zeros(q_table_path))

