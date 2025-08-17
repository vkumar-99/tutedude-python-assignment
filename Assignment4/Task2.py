with open('output.txt', 'w') as write_file:
    user_input = input('Enter text to write to the file:')
    write_file.write(user_input)
with open('output.txt', 'a') as append_file:
    user_input = input('Enter additional text to append the file:')
    append_file.write('\n')
    append_file.write(user_input)
with open('output.txt', 'r') as read_file:
    file_data = read_file.read()
    print('Final content of output.txt:')
    print(file_data)