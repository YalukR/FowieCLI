import psutil

def cpu_usage():
    return psutil.cpu_percent(interval=1)

def ram_usage():
    return psutil.virtual_memory().percent
