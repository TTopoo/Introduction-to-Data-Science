def make_stu_list(num):
    i = 1
    student_list = []
    while i <= num:
        student = input("请输入学生姓名:")
        student_list.append(student)
        i += 1
    return student_list

def print_mess(a):
    student = make_stu_list(a)
    findstudent=input("请输入想找的学生姓名")
    for index in range(len(student)):
        if student[index]==findstudent :
            print("Yes")
            return 0
    print("No")
count=int(input("n="))
print_mess(count)
