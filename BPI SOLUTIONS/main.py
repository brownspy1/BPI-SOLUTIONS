import id_genaretor
import os
import SMS

# crating a data class
class usardata:
    def Bangla(self):
        Name = input("Enter your Name:")
        Father_name = input("Enter your Father Name :")
        Mother_name = input("Enter your Mother Name :")
        Seson = input("Seson:")
        Tecnologi = input("Tecnologi:")
        ClassRoll = int(input("ClassRoll:"))
        Bord_roll = int(input("Bord roll:"))
        Rag_num = int(input("Rag Number:"))
        _Photo = input("Entar your Bord roll [In English]")
        image = f"photo/{_Photo}.jpg"
        Photo = id_genaretor.image_to_url(image)
        id_genaretor.make_png_id_bangla(Name, Father_name, Mother_name, Seson, Tecnologi,
                                        Bord_roll, Photo)
        id_genaretor.back_make_png_id_bangla(ClassRoll, Bord_roll, Rag_num)
        print(
            f"Congratulations! your id generated successfully! \nyour id path Id \nCard/font_{Bord_roll}.png\nCard/back_{Bord_roll}.png")

    def English(self):
        print("Please write all in English")
        Name = input("Enter your Name:")
        Father_name = input("Enter your Father Name :")
        Mother_name = input("Enter your Mother Name :")
        Seson = input("Seson:")
        Tecnologi = input("Tecnologi:")
        ClassRoll = int(input("ClassRoll:"))
        Bord_roll = int(input("Bord roll:"))
        Rag_num = int(input("Rag Number:"))
        image = f"photo/{Bord_roll}.jpg"
        Photo = id_genaretor.image_to_url(image)
        id_genaretor.make_png_id_english(Name, Father_name, Mother_name, Seson, Tecnologi,
                                         Bord_roll, Photo)
        id_genaretor.back_make_png_id_english(ClassRoll, Bord_roll, Rag_num)
        print(
            f"Congratulations! your id generated successfully!\ncheck:\nCard/English_font_{Bord_roll}.png\nCard/English_back_{Bord_roll}.png")

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')


data = usardata()
print('''
                ░░░░░░  ░░░░░░  ░░     ░░░░░░░  ░░░░░░  ░░      ░░    ░░ ░░░░░░░░ ░░  ░░░░░░  ░░░    ░░ ░░░░░░░ 
                ▒▒   ▒▒ ▒▒   ▒▒ ▒▒     ▒▒      ▒▒    ▒▒ ▒▒      ▒▒    ▒▒    ▒▒    ▒▒ ▒▒    ▒▒ ▒▒▒▒   ▒▒ ▒▒      
                ▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒     ▒▒▒▒▒▒▒ ▒▒    ▒▒ ▒▒      ▒▒    ▒▒    ▒▒    ▒▒ ▒▒    ▒▒ ▒▒ ▒▒  ▒▒ ▒▒▒▒▒▒▒ 
                ▓▓   ▓▓ ▓▓      ▓▓          ▓▓ ▓▓    ▓▓ ▓▓      ▓▓    ▓▓    ▓▓    ▓▓ ▓▓    ▓▓ ▓▓  ▓▓ ▓▓      ▓▓ 
                ██████  ██      ██     ███████  ██████  ███████  ██████     ██    ██  ██████  ██   ████ ███████ 
                                                                               
''')


def main():
    while True:
        Choise = input("\n1.ID GENERATOR "
                       "\n2.Student management system"
                       "\n3.Exit"
                       "\nEnter your choice (1-3):")

        if Choise == "1":
            Choi = input("\n1.Bangla ID"
                         "\n2.English ID"
                         "\n3.Main Menu"
                         "\nEnter your choice (1-3):")
            if Choi == '1':
                print("""
                ░░░░░░   ░░░░░  ░░░    ░░  ░░░░░░  ░░       ░░░░░  
                ▒▒   ▒▒ ▒▒   ▒▒ ▒▒▒▒   ▒▒ ▒▒       ▒▒      ▒▒   ▒▒ 
                ▒▒▒▒▒▒  ▒▒▒▒▒▒▒ ▒▒ ▒▒  ▒▒ ▒▒   ▒▒▒ ▒▒      ▒▒▒▒▒▒▒ 
                ▓▓   ▓▓ ▓▓   ▓▓ ▓▓  ▓▓ ▓▓ ▓▓    ▓▓ ▓▓      ▓▓   ▓▓ 
                ██████  ██   ██ ██   ████  ██████  ███████ ██   ██ 
                """)
                data.Bangla()
                data.clear_terminal()
            elif Choi == '2':
                print("""
                ░░░░░░░ ░░░    ░░  ░░░░░░  ░░      ░░ ░░░░░░░ ░░   ░░ 
                ▒▒      ▒▒▒▒   ▒▒ ▒▒       ▒▒      ▒▒ ▒▒      ▒▒   ▒▒ 
                ▒▒▒▒▒   ▒▒ ▒▒  ▒▒ ▒▒   ▒▒▒ ▒▒      ▒▒ ▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒ 
                ▓▓      ▓▓  ▓▓ ▓▓ ▓▓    ▓▓ ▓▓      ▓▓      ▓▓ ▓▓   ▓▓ 
                ███████ ██   ████  ██████  ███████ ██ ███████ ██   ██ 
""")
                data.English()
                data.clear_terminal()
            elif Choi == '3':
                data.clear_terminal()
                main()
        elif Choise == "2":
            student_list = SMS.read_from_csv()
            if SMS.login():
                while True:
                    print('''
                ░░░░░░  ░░░░░░  ░░ 
                ▒▒   ▒▒ ▒▒   ▒▒ ▒▒ 
                ▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒ 
                ▓▓   ▓▓ ▓▓      ▓▓ 
                ██████  ██      ██ 

            Barisal Polytechnic Institute                

                        ''')
                    choice = int(input('1. Add Student\n'
                                       '2. Show Student\n'
                                       '3. Edit Student\n'
                                       '4. Remove Student\n'
                                       '5. Search Student\n'
                                       '6. Log out\n'
                                       'Enter your choice (1-6): '))

                    if choice == 1:
                        name = input('Input Student Name:')
                        father_name = input('Input Student Father Name')
                        mother_name = input('Input Student Mother Name')
                        dep = input('Input Student Department:')
                        roll = input('Input Student Roll:')
                        email = input('Input Student Email')
                        session = input('Input Student Session:')
                        student_list[roll] = {'Name': name, 'Father': father_name, 'Mother': mother_name,
                                              'Department': dep, 'Session': session, 'Email': email}
                        SMS.save_to_csv(student_list)
                        data.clear_terminal()

                    elif choice == 2:
                        SMS.show_student(student_list)
                        data.clear_terminal()

                    elif choice == 3:
                        edit_roll = input("Which student's Roll to edit:")
                        if edit_roll in student_list:
                            name = input('Input Student Name:')
                            father_name = input('Input Student Father Name')
                            mother_name = input('Input Student Mother Name')
                            dep = input('Input Student Department:')
                            session = input('Input Student Session:')
                            email = input('Input Student Email')
                            student_list[edit_roll] = {'Name': name, 'Father': father_name, 'Mother': mother_name,
                                              'Department': dep, 'Session': session, 'Email': email}
                            SMS.save_to_csv(student_list)
                            data.clear_terminal()
                        else:
                            print('Student Roll not found!')
                            data.clear_terminal()

                    elif choice == 4:
                        remove_roll = input("Which student's Roll to remove:")
                        if remove_roll in student_list:
                            ask = input("Do you want to remove this student? (Y/N): ")
                            if ask.lower() == 'y':
                                student_list.pop(remove_roll)
                                print('Successfully removed the student!')
                                SMS.save_to_csv(student_list)
                                data.clear_terminal()
                            else:
                                print('No changes were made.')
                                data.clear_terminal()
                        else:
                            print('Student Roll not found!')
                            data.clear_terminal()

                    elif choice == 5:
                        search_roll = input('Enter Student Roll to search:')
                        if search_roll in student_list:
                            print(f"|%%%%%%%%%%%%%%% Student info %%%%%%%%%%%%%%%%%%|"
                                  f"\n\t\t\tStudent Name:{student_list[search_roll]['Name']}"
                                  f"\n\t\t\tRoll:{search_roll}"
                                  f"\n\t\t\tDepartment:{student_list[search_roll]['Department']}"
                                  f"\n\t\t\tSession:{student_list[search_roll]['Session']}\n"
                                  f"|%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|")
                            chois = input("Do you want to see more student data?[Y/N]")
                            if chois=='N' or chois=='n':
                                data.clear_terminal()
                                main()
                        else:
                            print('Student not found.')

                    elif choice == 6:
                        ask = input("Do you Really  Wan't to exit from this program Y/N: ")
                        if ask == 'Y' or ask == 'y':
                            data.clear_terminal()
                            main()
                        else:
                            print('Thank for using this program!')
                            SMS.clear_terminal()
                            break
                    else:
                        SMS.clear_terminal()
                        print('Invalid choice. Please choose a number between 1 and 6.')
            else:
                print('Sorry, you do not have access to this program!')
        elif Choise == "3":
            Choise = input("Do you want to exit? [Y/N]:")
            if Choise == "Y" or Choise == "y":
                data.clear_terminal()
                break
            else:
                main()

if __name__ == "__main__":
    main()