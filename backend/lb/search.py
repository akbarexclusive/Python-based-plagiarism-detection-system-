import psutil
import numpy as np
import pickle
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define search algorithms
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Load your AI model or use a simple decision function
def choose_algorithm(cpu_usage):
    if cpu_usage < 50:  # Low load
        return 'binary_search'
    else:  # High load
        return 'linear_search'

# Main function to perform search
def search(arr, target):
    cpu_usage = psutil.cpu_percent(interval=1)
    logging.info(f'Current CPU Usage: {cpu_usage}%')

    algorithm = choose_algorithm(cpu_usage)
    logging.info(f'Using {algorithm} algorithm.')

    if algorithm == 'binary_search':
        # Ensure the array is sorted for binary search
        arr.sort()
        result = binary_search(arr, target)
    else:
        result = linear_search(arr, target)

    return result

# Example usage
if __name__ == '__main__':
    array = np.random.randint(0, 10000, size=1000)
    target_value = 5000
    index = search(array, target_value)

    if index != -1:
        logging.info(f'Target {target_value} found at index {index}.')
    else:
        logging.info(f'Target {target_value} not found.')

