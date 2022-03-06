
import FileTwo


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print("File one __name__ is set to: {}".format(__name__))


# when the interpreter runs a module, the __name__ variable will be set as  __main__ if the module that is being run is the main program.
# But if the code is importing the module from another module, then the __name__  variable will be set to that module’s name.
def main():
    if __name__ == '__main__':
        print_hi(__name__)
        FileTwo.runprintstatement()



