import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Simulate data: traffic load, cpu usage, and server id
data = np.random.rand(1000, 2)  # (traffic load, cpu usage)
target = np.random.randint(0, 5, 1000)  # 5 servers

# Split the data
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)

# Train a simple model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model for later use
import pickle
with open('load_balancer_model.pkl', 'wb') as f:
    pickle.dump(model, f)

