import pickle
from pprint import pprint

with open('load_balancer_model.pkl', 'rb') as file:
    data = pickle.load(file)

pprint(data)

