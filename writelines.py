# Open a file in read/write mode
fo = open(r"C:\Users\oekpom\Desktop\Python\foo.txt", "r+")
print ("Name of the file: ", fo.name)
seq = ["\nThis is 6th line\n", "This is 7th line"]
# Write sequence of lines at the end of the file.
fo.seek(0, 2)
fo.writelines(seq)
fo.seek(0,0)
for index in range(7):
    line = next(fo)
    print ("Line No %d - %s" % (index, line))
# Close opened file
fo.close()
