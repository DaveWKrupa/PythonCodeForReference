import time


def time_this():
    """Print the latest tutorial from Real Python"""
    tic = time.perf_counter()
    time.sleep(5)
    toc = time.perf_counter()
    print(f"this took {toc - tic:0.4f} seconds")



time_this()
# this took 5.0070 seconds