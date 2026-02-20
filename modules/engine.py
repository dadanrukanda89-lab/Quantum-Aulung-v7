import platform

def get_sys_info():
    info = {
        "Sistem": platform.system(),
        "Node": platform.node(),
        "Rilis": platform.release(),
        "Mesin": platform.machine(),
        "Python": platform.python_version()
    }
    return info

