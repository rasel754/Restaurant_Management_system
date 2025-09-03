from foodItem import Food_Item
from menu import Menu
from  user import Admin , Customer, Employee
from restaurant import Restaurant
from orders import Order

mamar_restaurant=Restaurant("Mamar Restaurant")

def customer_menu():
    name=input("Enter your name: ")
    email=input("Enter your email: ")
    phone=input("Enter your phone: ")
    address=input("Enter your address: ")
    customer=Customer(name=name,email=email,phone=phone,address=address)

    while True:
        print(f"Welcome {customer.name} !!")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3 View Cart")
        print("4. PayBill")
        print("5. Exit")

        choice=int(input("Enter Your Choice: "))

        if choice ==1:
            customer.show_menu(mamar_restaurant)
        elif choice == 2:
            itemName=input("Enter Item Name: ")
            itemQuantity=int(input("Enter Item Quantity: "))

            customer.add_to_cart(mamar_restaurant , itemName , itemQuantity)
        elif choice ==3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice ==5:
            break
        else:
            print("Invalid input ")



def admin_menu():
    name=input("Enter your name: ")
    email=input("Enter your email: ")
    phone=input("Enter your phone: ")
    address=input("Enter your address: ")
    admin=Admin(name=name,email=email,phone=phone,address=address)

    while True:
        print(f"Welcome {admin.name} !!")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3 View Employee")
        print("4. View Item")
        print("5. Delete Item")
        print("6. Exit")

        choice=int(input("Enter Your Choice: "))

        if choice ==1:

            itemName=input("Enter Item Name: ")
            itemPrice=int(input("Enter Item Price: "))
            itemQuantity=int(input("Enter Item Quantity: "))
            item=Food_Item(itemName, itemPrice , itemQuantity)

            admin.add_new_item(mamar_restaurant, item)

        elif choice == 2:
            name = input("Enter employee name : ")
            phone = input("Enter employee phone : ")
            email = input("Enter employee email : ")
            designation = input("Enter employee designation : ")
            age = input("Enter employee age : ")
            salary = input("Enter employee salary : ")
            address = input("Enter employee address : ")
            employee = Employee(name, email, phone, address,age, designation, salary)

            admin.add_employee(mamar_restaurant , employee)

        elif choice ==3:
            admin.view_employee(mamar_restaurant)

        elif choice == 4:
            admin.view_menu(mamar_restaurant)

        elif choice ==5 :
            item_name=input("Enter Item Name: ")
            admin.remove_item(mamar_restaurant,item_name)

        elif choice ==6:
            break
        else:
            print("Invalid input ")



while True:
    print("Welcome!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid Input!!")

