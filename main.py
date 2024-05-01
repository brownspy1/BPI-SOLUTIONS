import id_genaretor
import os
import SMS


# crating a data class
class usardata:
    def Bangla(self):
        Name = input("\t\t\t\tEnter your Name:")
        Father_name = input("\t\t\t\tEnter your Father Name :")
        Mother_name = input("\t\t\t\tEnter your Mother Name :")
        Seson = input("\t\t\t\tSeson:")
        Tecnologi = input("\t\t\t\tTecnologi:")
        ClassRoll = int(input("\t\t\t\tClassRoll:"))
        Bord_roll = int(input("\t\t\t\tBord roll:"))
        Rag_num = int(input("\t\t\t\tRag Number:"))
        _Photo = input("\t\t\t\tEntar your Bord roll [In English]")
        image = f"photo/{_Photo}.jpg"
        Photo = id_genaretor.image_to_url(image)
        id_genaretor.make_png_id_bangla(Name, Father_name, Mother_name, Seson, Tecnologi,
                                        Bord_roll, Photo)
        id_genaretor.back_make_png_id_bangla(ClassRoll, Bord_roll, Rag_num)
        print(
            f"\t\t\t\tCongratulations! your id generated successfully! \n\t\t\t\tyour id path Id \n\t\t\t\tCard/font_{Bord_roll}.png\n\t\t\t\tCard/back_{Bord_roll}.png")

    def English(self):
        print("\t\t\t\tPlease write all in English")
        Name = input("\t\t\t\tEnter your Name:")
        Father_name = input("\t\t\t\tEnter your Father Name :")
        Mother_name = input("\t\t\t\tEnter your Mother Name :")
        Seson = input("\t\t\t\tSeson:")
        Tecnologi = input("\t\t\t\tTecnologi:")
        ClassRoll = int(input("\t\t\t\tClassRoll:"))
        Bord_roll = int(input("\t\t\t\tBord roll:"))
        Rag_num = int(input("\t\t\t\tRag Number:"))
        image = f"photo/{Bord_roll}.jpg"
        Photo = id_genaretor.image_to_url(image)
        id_genaretor.make_png_id_english(Name, Father_name, Mother_name, Seson, Tecnologi,
                                         Bord_roll, Photo)
        id_genaretor.back_make_png_id_english(ClassRoll, Bord_roll, Rag_num)
        print(
            f"\t\t\t\tCongratulations! your id generated successfully!\n\t\t\t\tcheck:\n\t\t\t\tCard/English_font_{Bord_roll}.png\n\t\t\t\tCard/English_back_{Bord_roll}.png")

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
        Choise = input("\n\t\t\t\t1.ID GENERATOR "
                       "\n\t\t\t\t2.Student management system"
                       "\n\t\t\t\t3.Exit"
                       "\n\t\t\t\tEnter your choice (1-3):")

        if Choise == "1":
            Choi = input("\n\t\t\t\t1.Bangla ID"
                         "\n\t\t\t\t2.English ID"
                         "\n\t\t\t\t3.Main Menu"
                         "\n\t\t\t\tEnter your choice (1-3):")
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
                    choice = int(input('\t\t\t\t1. Add Student\n'
                                       '\t\t\t\t2. Show Student\n'
                                       '\t\t\t\t3. Edit Student\n'
                                       '\t\t\t\t4. Remove Student\n'
                                       '\t\t\t\t5. Search Student\n'
                                       '\t\t\t\t6. Log out\n'
                                       '\t\t\t\tEnter your choice (1-6): '))

                    if choice == 1:
                        name = input('\t\t\t\tInput Student Name:')
                        father_name = input('\t\t\t\tInput Student Father Name')
                        mother_name = input('\t\t\t\tInput Student Mother Name')
                        dep = input('\t\t\t\tInput Student Department:')
                        roll = input('\t\t\t\tInput Student Roll:')
                        email = input('\t\t\t\tInput Student Email')
                        session = input('\t\t\t\tInput Student Session:')
                        student_list[roll] = {'Name': name, 'Father': father_name, 'Mother': mother_name,
                                              'Department': dep, 'Session': session, 'Email': email}
                        SMS.save_to_csv(student_list)
                        data.clear_terminal()

                    elif choice == 2:
                        SMS.show_student(student_list)
                        data.clear_terminal()

                    elif choice == 3:
                        edit_roll = input("\t\t\t\tWhich student's Roll to edit:")
                        if edit_roll in student_list:
                            name = input('\t\t\t\tInput Student Name:')
                            dep = input('\t\t\t\tInput Student Department:')
                            session = input('\t\t\t\tInput Student Session:')
                            student_list[edit_roll] = {'Name': name, 'Department': dep, 'Session': session}
                            SMS.save_to_csv(student_list)
                            data.clear_terminal()
                        else:
                            print('\t\t\t\tStudent Roll not found!')
                            data.clear_terminal()

                    elif choice == 4:
                        remove_roll = input("\t\t\t\tWhich student's Roll to remove:")
                        if remove_roll in student_list:
                            ask = input("\t\t\t\tDo you want to remove this student? (Y/N): ")
                            if ask.lower() == 'y':
                                student_list.pop(remove_roll)
                                print('\t\t\t\tSuccessfully removed the student!')
                                SMS.save_to_csv(student_list)
                                data.clear_terminal()
                            else:
                                print('\t\t\t\tNo changes were made.')
                                data.clear_terminal()
                        else:
                            print('\t\t\t\tStudent Roll not found!')
                            data.clear_terminal()

                    elif choice == 5:
                        search_roll = input('\t\t\t\tEnter Student Roll to search:')
                        if search_roll in student_list:
                            print(f"\t\t\t\t|%%%%%%%%%%%%%%% Student info %%%%%%%%%%%%%%%%%%|"
                                  f"\n\t\t\t\t\t\t\tStudent Name:{student_list[search_roll]['Name']}"
                                  f"\n\t\t\t\t\t\t\tRoll:{search_roll}"
                                  f"\n\t\t\t\t\t\t\tDepartment:{student_list[search_roll]['Department']}"
                                  f"\n\t\t\t\t\t\t\tSession:{student_list[search_roll]['Session']}\n"
                                  f"\t\t\t\t|%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|")
                            chois = input("\t\t\t\tDo you want to see more student data?[Y/N]")
                            if chois == 'N' or chois == 'n':
                                data.clear_terminal()
                                main()
                        else:
                            print('\t\t\t\tStudent not found.')

                    elif choice == 6:
                        ask = input("\t\t\t\tDo you Really  Wan't to exit from this program Y/N: ")
                        if ask == 'Y' or ask == 'y':
                            data.clear_terminal()
                            main()
                        else:
                            print('\t\t\t\tThank for using this program!')
                            SMS.clear_terminal()
                            break
                    else:
                        SMS.clear_terminal()
                        print('\t\t\t\tInvalid choice. Please choose a number between 1 and 6.')
            else:
                print('\t\t\t\tSorry, you do not have access to this program!')
        elif Choise == "3":
            Choise = input("\t\t\t\tDo you want to exit? [Y/N]:")
            if Choise == "Y" or Choise == "y":
                data.clear_terminal()
                break
            else:
                main()


if __name__ == "__main__":
    main()
