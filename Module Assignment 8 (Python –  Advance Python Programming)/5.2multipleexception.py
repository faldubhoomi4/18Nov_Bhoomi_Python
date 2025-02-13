filename = input("Enter file name ")

try:
    myfile=open(filename,'r')
    myfile.write("Hello")
except Exception as e:
    print(e)