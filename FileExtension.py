filename = input("Input the Filename: ")
extension=filename.split(".")
if filename[-3:]=='.py':
    print("The extension of the file is : 'Python'")
else:
    print("The extension of the file is : ."+extension[-1])
