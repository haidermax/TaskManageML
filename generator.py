import pandas as pd
import numpy as np
def generate_synthetic_data(num_tasks, num_nodes, node_params):
    np.random.seed(42)
    data = {
        'Task_ID': range(1, num_tasks + 1),
        'Task_Complexity': np.random.uniform(1, 10, num_tasks),
        'Processing_Time': np.random.uniform(5, 30, num_tasks),
        'Memory_Requirement': np.random.uniform(1, 5, num_tasks),
        'Node_ID': np.random.choice(range(1, num_nodes + 1), num_tasks)
    }

    for i in range(1, num_nodes + 1):
        # Use reciprocal of 'Load' values for an inverse relationship
        data[f'Node{i}_Load'] = 1 / np.random.uniform(*node_params[f'Node{i}_Load'], num_tasks)
        data[f'Node{i}_Power'] = np.random.uniform(*node_params[f'Node{i}_Power'], num_tasks)
        data[f'Node{i}_Speed'] = np.random.uniform(*node_params[f'Node{i}_Speed'], num_tasks)

    return pd.DataFrame(data)
