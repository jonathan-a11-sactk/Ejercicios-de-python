#IT IS A CRUD FOCUSED ON CONTACTS
class Contact:
    def __init__(self,name,lasname,number,sex,email,address):
        self.name = name
        self.lasname = lasname
        self.number = number
        self.sex = sex
        self.email = email
        self.address = address
    def __str__(self):
        return f"Name:{self.name},Lasname:{self.lasname},Numero:{self.number},Sex:{self.sex},Email:{self.email},Address:{self.address}"
    #Setter update object
    def setname(self,name):
        self.name = name
    def setlasname(self,lastaname):
        self.lasname = lastaname
    def setnumber(self,number):
        self.number = number
    def setsex(self,sex):
        self.sex = sex
    def setemail(self,email):
        self.email = email
    def setaddress(self,address):
        self.address = address
#We create instances of the contact class
contact1 = Contact("Jonathan","Lituma","0958994767","Super hombre","jonathan@gamil.com","ofelia")
contact2 = Contact("Paul","Galarza","2290843","Hombresote","paul@gamil.com","latacunga")
list_contact = []
list_contact.append(contact1)
list_contact.append(contact2)
#Basic functions of raw materials
def add_contact():
    name = input("Enter contact name")
    lastname = input("Enter contact lastname")
    number = input("Enter contact number")
    sex = input("Enter contact sex")
    email = input("Enter contact email")
    address = input("Enter contact address")
    try:
        contact3 = Contact(name,lastname,number,sex,email,address)
        list_contact.append(contact3)
    except:
        print("The user could not be created correctly")
def update_contact():
    try:
        index = int(input("Enter the index of the contact you want to update:"))
        if 0 <= index < len(list_contact):
            contact = list_contact[index]
            print(f"Current contact: {contact}")
            name = input("Enter new contact name:")
            contact.setname(name)
            lastname = input("Enter new contact lastname:")
            contact.setlasname(lastname)
            number = input("Enter new contact number:")
            contact.setnumber(number)
            sex = input("Enter new contact sex:")
            contact.setsex(sex)
            email = input("Enter new contact email:")
            contact.setemail(email)
            address = input("Enter new contact address:")
            contact.setaddress(address)
            print("Contact updated successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number for the index.")
def delete_contact():
    index = int(input("Enter the index of the contact you want to delete: "))
    for contact in list_contact:
        if index < len(list_contact):
            list_contact.pop(index)
        else:
            print("Invalid index.")
def view_contact():
    for contact in list_contact:
        print(contact)

opc = input("1.Add Contact 2.  Update Contact 3. Delete Contact 4. View Contact 5. Go out")
while(opc!="5"):
    if opc == "1":
        add_contact()
    elif opc == "2":
        update_contact()
    elif opc == "3":
        delete_contact()
    elif opc == "4":
        view_contact()
    opc = input("1.Add Contact 2. Delete  Contact 3. Update Contact 4. View Contact 5. Go out")
print("Thank you for using the program")
