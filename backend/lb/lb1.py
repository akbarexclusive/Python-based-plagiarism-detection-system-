import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_request_rate():
    # Simulate request rate (e.g., requests per second)
    import random
    return random.randint(10, 100)  # Simulated traffic load

