# Program to show various ways to read and
# write data in a file.
file1 = open("synt.txt", "r")
print("Output of Readline function is ")
print (file1.read())
print (file1.readlines())
print("")
file1.close()
