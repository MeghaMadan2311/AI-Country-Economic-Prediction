import time


def measure_execution_time(function, *args, **kwargs):
    start_time = time.perf_counter()

    result = function(*args, **kwargs)

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    print(f"Execution time: {execution_time:.4f} seconds")

    return result, execution_time
