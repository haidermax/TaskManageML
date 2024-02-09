from distributer import distribute_tasks_to_nodes
from generator import generate_synthetic_data

#input Process:
num_tasks = int(input("Enter the number of tasks: "))
num_nodes = int(input("Enter the number of nodes: "))

node_params = {}
for i in range(1, num_nodes + 1):
    power_range = [float(x) for x in input(f"Enter power range for Node {i} (min max): ").split()]
    load_range = [float(x) for x in input(f"Enter load range for Node {i} (min max): ").split()]
    speed_range = [float(x) for x in input(f"Enter speed range for Node {i} (min max): ").split()]
    node_params[f'Node{i}_Power'] = power_range
    node_params[f'Node{i}_Load'] = load_range
    node_params[f'Node{i}_Speed'] = speed_range



# # Generate synthetic data
tasks_df = generate_synthetic_data(num_tasks, num_nodes,node_params )


# # Distribute tasks to nodes based on their abilities
task_distribution = distribute_tasks_to_nodes(tasks_df, num_nodes)

# # Display the task distribution
# print("\nTask Distribution:")
for node, tasks in task_distribution.items():
    print(f"Node {node}: {tasks} tasks")
   