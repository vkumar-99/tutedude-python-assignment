stu_mark_dict = {'Vimal':100,'Gaurav':98,'Sanjeev':96}
input_name = input("Enter the student's name.")
if input_name in stu_mark_dict.keys():
    print("{}'s marks: {}".format(input_name, stu_mark_dict.get(input_name)))
else:
    print("Student not found")