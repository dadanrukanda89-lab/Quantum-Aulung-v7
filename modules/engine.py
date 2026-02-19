import shutil

def cek_storage():
    total, used, free = shutil.disk_usage("/")
    return f"{free // (2**30)} GB"
