from contextlib import contextmanager
# context managers

# the with statement is a context manager that handles the
# allocation and deallocation of the resource it is used with

# since it is using the with statement it will automatically close the file even if there is an error
# with open("notes.txt", "w") as file:
#     file.write("Some text")
#
# # this is equivalent to
# file = open("notes.txt", "w")
# try:
#     file.write("Some text")
# finally:
#     file.close()


# to create a context manager class we need to implement the enter and exit methods

class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("Enter")
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print("Exc:", exc_type, exc_value)
        print("exit")
        return True  # returning true will suppress the exception if there is one


with ManagedFile("notes.txt") as file:
    print("do some stuff")
    file.write("A new line")


# you can also use the contextmanager class to build a generator class that opens the file
# it needs to be decorated with the contextmanager class

@contextmanager
def open_managed_file(filename):
    f = open(filename, "w")
    try:
        yield f
    finally:
        f.close()


with open_managed_file("notes.txt") as file:
    file.write("Write something")
