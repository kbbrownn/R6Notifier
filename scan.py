def is_open():
    try:
        myfile = open("test.JPG", "r+") # or "a+", whatever you need
        print("File is not open")
    except IOError:
        print("Could not open file!")
