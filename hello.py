#! shebang for unix system
# comment

import platform

def main():
    version()

def version():
    print('Hello string {}'.format(platform.python_version()))
    print(platform.python_version())
if __name__ == "__main__":
    main()

