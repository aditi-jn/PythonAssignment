filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
if f_extns[-1]=='jpg':
    print(f_extns[0],".pdf")