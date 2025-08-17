file_name = 'sample.txt'
try:
    open_file = open(file_name,'r')
    lines = open_file.readlines()
    counter = 1
    for line in lines:
        print("Line",counter,":",line)
        counter += 1
except FileNotFoundError:
    print("The file '",file_name,"' was not found")