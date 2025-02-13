myfile=open('hello.txt','r')

try:
    myfile.write("Hello")
except Exception as e:
    print(e)
finally:
    myfile.close()
    print("File closed.")