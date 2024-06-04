import platform


def get_python_version():
    return platform.python_version().lower()

def write_python_version_file():
    with open('python_version.txt', 'w') as f:
        f.write(get_python_version())

if __name__ == '__main__':
    write_python_version_file()