#school administration program
import csv
def write_csv(info_list):
  with open('student_info.csv','a',newline=' ') as csv_file:
    writer = csv.writer(csv_file)
    if csvfile.tell() == 0:
      writer.writerow(["NAME","AGE","CONTACT NUMBER","E-MAIL ID"])
    writer.writerow(info_list)
if __name__ == '__main__':
  condition = True
  while(condition):
    student_info = input("ENTER STUDENT INFORMATION IN THE FOLLOWING FORMAT(NAME AGE CONTACT_NUMBER E-MAIL_ID:")
    print("ENTERED INFORMATION:"+student_info)
    student_info_list = student_info.split(' ')
    print("ENTERED SPLIT UP INFORMATION IS:"+str(student_info_list))
    print("\n THE ENTERED INFORMATION IS \nNAME :{}\nAGE: {}\nCONTACT_NUMBER: {}\nE-MAIL ID: {}"
          .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
    choice_check = input("IS THE ENTERED INFORMATION CORRECT?(yes/no:"))
    if choice_check == "yes":
      write_csv(student_info_list)
      condition_check = input("ENTER(yes/no) IF YOU WANT TO ENTER INFORMATION FOR ANOTHER STUDENTS:")
      if condition_check == "yes": 
        condition = True
        student_num = student_num+1
      elif condition_check == "no":
        condition = False 
      elif choice_check == "no":
        print("\nPLEASE RE-ENTER THE VALUES:")
