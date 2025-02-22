# from pympler import summary, muppy
import psutil
import os
import sys

def memory_usage_psutil():
    """Returns the memory usage in MB using psutil."""
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / (1024 ** 2)  # Convert bytes to MB
    return mem

print(f"Memory (Before) using psutil: {memory_usage_psutil():.2f} MB")

# def memory_usage_resource():
#     rusage_denom = 1024.
#     if sys.platform == 'darwin':
#         # ... it seems that in OSX the output is different units ...
#         rusage_denom = rusage_denom * rusage_denom
#     mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / rusage_denom
#     return mem
    