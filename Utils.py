import os 

def get_fragment_size():
    return os.statvfs('.').f_frsize