import os

print("Lets start the file handling program")

print("1.Create the file \n2. Read the file \n3.List the file \n4. Edit the program\n5.delete file\n6.end program")
while True:
    a=int(input("Enter the choice: "))
    
    def f():        
        print("1.Create the file")
        print("2.Read the file")
        print("3.List the file")
        print("4.Edit the file")
        print("5.Delete the file")
        print("6.Stop the program")  
    match a:
        case 1:
            print("\nCreating a file")
            name=input("Enter the file name: ")
            name=name+".txt"
            file=open(name, "w")
            file.write("Hello")
            print("File created successfully")
            print("______________________________________________________")
            f()
        case 2:
            print("\nReading a file")
            name=input("Enter the file name:")
            name=name+".txt"
            file=open(name, "r")
            print(file.read())
            print("______________________________________________________")
            f()
        case 3:
            print("\nListing a file")
            print("______________________________________________________")
            path="/"
            files=os.listdir (path)
            for file in files:
                print(file)
            print("______________________________________________________")
            f()
        case 4:
            print("\nediting a file")
            name=input("Enter the file name:")
            name=name+".txt"
            file=open(name+".txt", "w")
            print(file.write("mahalakshmi"))
            print("______________________________________________________")
            f()
        case 5:
            print("\ndeleting a file")
            name=input("Enter the file name:")
            name=name+".txt"
            os.remove(name)
            print("file",name,"deleted successfully")
            print("______________________________________________________")
            f()
        case 6:
            print("program end")
            print("**********************************************************")
