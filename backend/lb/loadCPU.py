import time
import multiprocessing

def cpu_load(duration):
    """Function to create CPU load."""
    end_time = time.time() + duration
    while time.time() < end_time:
        # Busy-waiting: perform a calculation to keep the CPU busy
        _ = sum(i * i for i in range(10**6))  # Adjust the range for more load

if __name__ == '__main__':
    # Number of processes to spawn (adjust according to your CPU cores)
    num_processes = multiprocessing.cpu_count()
    load_duration = 30  # Duration in seconds to keep the load

    print(f"Starting CPU load on {num_processes} cores for {load_duration} seconds.")
    
    # Create a list to hold the processes
    processes = []

    # Start the load processes
    for _ in range(num_processes):
        p = multiprocessing.Process(target=cpu_load, args=(load_duration,))
        processes.append(p)
        p.start()

    # Wait for all processes to complete
    for p in processes:
        p.join()

    print("CPU load test completed.")

