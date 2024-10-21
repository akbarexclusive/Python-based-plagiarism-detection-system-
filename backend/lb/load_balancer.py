import psutil
import numpy as np
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import time

# Create a placeholder for the collected data
data = []

# Define servers
servers = ['Server 1', 'Server 2', 'Server 3']

def get_server_metrics():
    return {
        'cpu_usage': psutil.cpu_percent(),
        'memory_usage': psutil.virtual_memory().percent,
        'available_memory': psutil.virtual_memory().available,
    }

def choose_server(metrics):
    return servers[np.argmin(metrics['cpu_usage'])]  # Replace with your logic

def load_balance():
    metrics = get_server_metrics()
    server_to_send_load = choose_server(metrics)
    print(f'Sending load to: {server_to_send_load}')
    
    # Store the metrics and server choice for potential future training
    data.append((metrics['cpu_usage'], metrics['memory_usage'], server_to_send_load))

def train_model():
    if len(data) > 100:  # Example threshold to start training
        df = pd.DataFrame(data, columns=['cpu_usage', 'memory_usage', 'chosen_server'])
        df['chosen_server'] = df['chosen_server'].astype('category').cat.codes

        X = df[['cpu_usage', 'memory_usage']]
        y = df['chosen_server']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        joblib.dump(model, 'load_balancer_model.pkl')
        print("Model trained and saved.")

if __name__ == "__main__":
    while True:
        load_balance()
        if len(data) > 100:
            train_model()
            data.clear()
        time.sleep(10)  # Monitor every 10 seconds

