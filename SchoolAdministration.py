import csv
def write_into_a_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name", "Age", "Contact Number", "E-mail ID"])
        writer.writerow(info_list)
if __name__ == '__main__':
    condition=True
    student_no=1
    while(condition):
        student_info=input("Enter student {} information in the following format (Name Age Contact_Number E-mail_ID: ".format(student_no))
        student_info_list=student_info.split(' ')
        print("\nThe entered information is\nName: {}\nAge: {}\nContact Number: {}\nE-mail ID: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        info_check=input("Is the entered student information is correct? (yes/no): ")
        if info_check=='yes':
            write_into_a_csv(student_info_list)
            student_no+=1
            next=input("Enter (yes/no) if you want to enter information of another student: ")
            if next=='yes':
                condition=True
            elif next=='no':
                condition=False
        elif info_check=='no':
            print("re-enter the student information")
