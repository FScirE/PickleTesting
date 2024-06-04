import platform


def get_python_version():
    return platform.python_version().lower()

def get_os_suffix():
    return platform.system().lower()

def write_python_version_file():
    file_name = f'{get_os_suffix()}{get_python_version()}.txt'
    with open(file_name, 'w') as f:
        f.write(get_python_version())

if __name__ == '__main__':
    write_python_version_file()