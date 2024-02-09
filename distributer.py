from sklearn.ensemble import RandomForestClassifier
# Function to distribute tasks to nodes based on their abilities
def distribute_tasks_to_nodes(task_df, num_nodes):
    # Extract node-specific columns for each node
    node_columns = [f'Node{i}_Power' for i in range(1, num_nodes + 1)] + \
                   [f'Node{i}_Load' for i in range(1, num_nodes + 1)] + \
                   [f'Node{i}_Speed' for i in range(1, num_nodes + 1)]
    node_columns = [col for col in node_columns if col in task_df.columns]

    X = task_df[['Task_Complexity', 'Processing_Time', 'Memory_Requirement'] + node_columns]
    y = task_df['Node_ID']

    # Model Training
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)

    # Predict nodes for the entire dataset
    task_df['Predicted_Node'] = model.predict(X)

    # Count the number of tasks assigned to each predicted node
    task_distribution = task_df['Predicted_Node'].value_counts().sort_index()
    return task_distribution


