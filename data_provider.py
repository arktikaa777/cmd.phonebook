file_name = "phonebook.txt"
file1 = open(file_name, "a+")
file1.close


def show_main_menu():
    ''' Show main menu for Phone Book Program '''
    print("\n   *** Phone Book Menu ***\n"+
        
          "------------------------------------------\n"+
          "Enter from 1 to 6:\n"+
          "Enter 1 To Display Your Contacts Records\n" +
          "Enter 2 To Add a New Contact Record\n"+
          "Enter 3 To Search your contacts\n"+
          "Enter 4 To download your file to PhoneBook\n"+
          "Enter 5 To download data from PhoneBook to your file\n"+
          "Enter 6 To Quit\n**********************")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        file1 = open(file_name, "r+")
        file_contents = file1.read()
        if len(file_contents) == 0:
            print("Phone Book is empty")
        else:
            print (file_contents)
        file1.close
        ent = input("Press Enter to continue ...")
        show_main_menu()
    elif choice == "2":
        enter_contact_record()
        ent = input("Press Enter to continue ...")
        show_main_menu()
    elif choice == "3":
        search_contact_record()
        ent = input("Press Enter to continue ...")
        show_main_menu()
    elif choice == "4": 
        import_data()
        ent = input("Press Enter to continue ...")
        show_main_menu()  
    elif choice == "5": 
        export_data()
        ent = input("Press Enter to continue ...")
        show_main_menu()      
         
    elif choice== "6":
        print("Thanks for using our Phone Book Program:")
              
    else:
        print("Wrong choice, Please Enter [1 to 6]\n")
        ent = input("Press Enter to continue ...")
        show_main_menu()
        
def search_contact_record():
    ''' This function is used to searches a specific contact record '''
    search_name = input("Enter First name for Searching contact record: ")

    search_name = search_name.title()
    file1 = open(file_name, "r+")
    file_contents = file1.readlines()
     
    found = False   
    for line in file_contents:
        if search_name in line:
            print("Your Required Contact Record is:", end=" ")
            print (line)
            found=True
            break
    if  found == False:
        print("There's no contact Record in Phone Book with name = " + search_name )

def enter_contact_record():
    ''' It  collects contact info firstname, last name, email and phone '''
   
    first = input('Enter First Name: ')
    first = first.title()
    last = input('Enter Last Name: ')
    last = last.title()
    phone = input('Enter Phone number: ')
    email = input('Enter E-mail: ')
    contact = ("[" + first + " " + last + ", " + phone + ", " + email +  "]\n")
    file1 = open(file_name, "a")
    file1.write(contact)
    print( "This contact\n " + contact + "has been added successfully!")
    
def import_data():
    file_to_read = input('Enter file name with extension: ')
    write_to_file = "phonebook.txt"
    
    file = open(file_to_read, "r")
    data = file.read()
    file.close()

    with open(write_to_file, "a") as file:
        file.write(data)
        print("New database has been added successfully to Phonebook!\n")

def export_data():
    write_to_file = input('Enter file name with extension: ')
    file_to_read= "phonebook.txt"
    
    file = open(file_to_read, "r")
    data = file.read()
    file.close()

    with open(write_to_file, "a") as file:
        file.write(data)
        print("Phonebook database has been added successfully to new file!\n")
    
    
show_main_menu()




