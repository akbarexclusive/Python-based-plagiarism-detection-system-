import pickle
from flask import Flask, request
import psutil
import random

app = Flask(__name__)

# Load the pre-trained model
with open('load_balancer_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Get real-time metrics
def get_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    request_rate = random.randint(10, 100)  # Simulated traffic
    return [request_rate, cpu_usage]

# Load balancer logic
@app.route('/balance', methods=['GET'])
def load_balance():
    metrics = get_metrics()
    
    # Predict which server to route traffic to
    server_id = model.predict([metrics])
    
    return f"Routing to server {int(server_id)}"

if __name__ == '__main__':
    app.run(port=8000)

