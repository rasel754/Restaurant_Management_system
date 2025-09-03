from abc import ABC
from orders import Order

class User(ABC) : 
    def __init__(self, name , phone , email , address):
        self.name=name
        self.email=email
        self.address=address
        self.phone=phone

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employee(self , restaurant, employee):
        restaurant.add_employee(employee)

    def view_employee(self,restaurant):
        restaurant.view_employee()

    def add_new_item(self , restaurant , item):
        restaurant.menu.add_menu_item(item)

    def remove_item(self , restaurant , item):
        restaurant.menu.add_menu_item(item)

    def view_menu(self , restaurant):
        restaurant.menu.show_menu()

    


class Employee(User):
    def __init__(self, name, phone, email, address , age , salary, designation):
        super().__init__(name, phone, email, address)
        self.age=age
        self.salary=salary
        self.designation =designation


class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart=Order()

    def show_menu(self , restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self , restaurant , itemName , quantity):
        item = restaurant.menu.find_item(itemName)
        print(item.quantity)
        if item:
            if quantity>item.quantity:
                print("Item quantity exceeded!!")
            else:
                item.quantity=quantity
                self.cart.add_item(item)
                print("item added")
        else:
            print("item no found")

    def view_cart(self):
        print("****view Cart****")
        print("Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price:- {self.cart.total_price}")
    def pay_bill(self):
        print(f"Total {self.cart.total_price} paid successfully")
        self.cart.clear()












# ad=Admin("rasel" ,"9958345","rasel.email","chandpur")
# ad.add_employee("milon","milon.email","859385","borisal",32,"chef",32000)

# amr_res=Restaurant("amr restaurant")

# mn=Menu()
# item=Food_Item("pizza",23,12)
# item2=Food_Item("burger",73,32)
# admin= Admin("Rasel" , 9394939,"rasel.email","chandpur")
# admin.add_new_item(amr_res,item)
# admin.add_new_item(amr_res,item2)
# mn.show_menu()

# customer1=Customer("Rasel" , 9394939,"rasel.email","chandpur")
# customer1.show_menu(amr_res)

# item_name=input("Enter Item Name: ")
# item_quantity=int(input("Enter Item Quantity: "))

# customer1.add_to_cart(amr_res,item_name,item_quantity)
# customer1.view_cart()