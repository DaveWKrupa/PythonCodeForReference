filetoopen = open("filetoopen.txt", "r")

if filetoopen.readable():
    print(filetoopen.read())
    print("File Printed")
else:
    print("File not readable")
filetoopen.close()

filetoopen2 = open("filetoopen.txt", "r")
for line in filetoopen2.readlines():
    print(line)
print("File Printed")
filetoopen2.close()

filetoopen3 = open("filetoopen.txt", "a")  # append
filetoopen3.write("\nthis is a new line")
filetoopen3.close()

filetoopen4 = open("filetoopen.txt", "r")
for line in filetoopen4.readlines():
    print(line)
print("File Printed")
filetoopen4.close()
