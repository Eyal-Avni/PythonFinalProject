import Employees_moud
import ProjectsTool

def print_logo():
    print("   &%%%%%%%%      %%%      %%%%%%%%%.   %%%  %%%%%%%%%  %%%     %%%   /%%%%%%%%&")
    print(" %%%.            %%%%%     %%%     %%%% %%%  %%        *%%%%&   %%% %%%%        ")
    print(" %%%%%%%#       %%% %%% ,  %%%     %%%% %%%  %%%%%%%%  *%% %%%. %%% /%%%%%%%    ")
    print("       %%%%%,  %%& //////  %%%%%%%%%%   %%%  %%        *%%   %%%%%%       (%%%%%")
    print(" &%%%%%%%%%%. %%(/*   %%%  %%%          %%%  %%%%%%%%% *%%    #%%%% .%%%%%%%%%%%\n")

def show_main_menu():
    print("Welcom to Sapiens Information System!")
    print("1.Employees Managment Tool")
    print("2.Projects Managment Tool")

def main_menu_main():

    again = 'y'
    choice_list = ['y', 'yes', 'Y', 'YES']
    while again in choice_list:
        print_logo()
        show_main_menu()
        choice = input("Please Enter your selection from the menu:\n")
        if choice == '1':
            Employees_moud.employee_main()
        elif choice == '2':
            ProjectsTool.project_tool_main()
        else:
            print("Invalid input!")
        again = input("----------------------\nSapiens Information System:\nWould you like to preform another action?(Y/N)\n")

    print("Goodbye!")
    
main_menu_main()