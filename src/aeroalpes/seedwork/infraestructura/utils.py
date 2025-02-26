import time
import os

def time_millis():
    return int(time.time() * 1000)

def broker_host():
    return os.getenv('PULSAR_ADDRESS', default="localhost")

