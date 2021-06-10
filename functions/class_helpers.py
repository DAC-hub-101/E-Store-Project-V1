import csv
import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


granted_adminlog = False


def granted_adminlogin():
    global granted_adminlog
    granted_adminlog = True


granted_publiclog = False


def granted_publiclogin():
    global granted_publiclog
    granted_publiclog = True


def adminlogin(email, password, role):
    success = False
    file = open("login.csv", "r")
    for i in file:
        a, b, c, d, e, j = i.split(",")
        c = c.strip()
        if a == email and b == password and c == role:
            success = True
            break
    file.close()

    if (success):
        granted_adminlogin()
        print("Admin Login Successful!")
    else:
        print("Wrong email or password. Please Try Again.")
        begin()


def publiclogin(email, password):
    success = False
    file = open("login.csv", "r")
    for i in file:
        a, b, c, d, e, j = i.split(",")
        b = b.strip()
        if a == email and b == password:
            success = True
            break
    file.close()
    if (success):
        granted_publiclogin()
        print("Login Successful!")
    else:
        print("Wrong email or password. Please Try Again.")
        begin()


dateofreg = {'date': '', 'email': '', 'password': '', 'role': '', 'name': '', 'surname': '', 'telephone': ''}


def register(email, password, role, name, surname, telephone):
    file = open("login.csv", "a")
    file.write("\n" + email + "," + password + "," + role + "," + name + "," + surname + "," + telephone)
    file.close()

    dateofreg['date'] = datetime.datetime.now()
    dateofreg['email'] = email
    dateofreg['password'] = password
    dateofreg['role'] = role
    dateofreg['name'] = name
    dateofreg['surname'] = surname
    dateofreg['telephone'] = telephone

    with open('registered.csv', mode='a') as reg:
        writing = csv.writer(reg, delimiter=",")
        writing.writerow(dateofreg.values())
    print("Thank you for you registration!")

    granted_publiclogin()


def access(option):
    global email
    if (option == "publiclogin"):
        email = input("Enter your email: ")
        password = input("Enter your password:")
        publiclogin(email, password)
    elif (option == "adminlogin"):
        email = input("Enter your email: ")
        password = input("Enter your password:")
        role = input("Please Enter your role:")
        adminlogin(email, password, role)

    elif (option == "reg"):
        print("Enter your name and password to register.")
        email = input("Enter your email: ")
        pas = input("Enter your password: ")
        role = input("Enter your role: ")
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        telephone = input("Enter your telephone: ")
        register(email, pas, role, name, surname, telephone)


def begin():
    global option
    print("Welcome to the Shop")
    option = input("Login or Register (publiclogin, adminlogin, reg): ")
    if (option != "publiclogin" and option != "adminlogin" and option != "reg"):
        begin()
    else:
        print('Please select one of the options.')

def read_csvfile(filename: str):
    database = []
    with open(filename, mode='r') as csvf:
        reader = csv.reader(csvf, delimiter=',')
        for row in reader:
            database.append(row)
    return database

class Car:
    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year

    def __str__(self):
        return f'This Car haves {self.maker}, {self.model}, {self.year}'

    def __repr__(self): return str(self.__dict__)


car_list = {}

with open('Products.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader, None)
    for row in reader:
        car_list[row[0]] = Car(row[3], row[4], 2020)


class Product:
    def __init__(self, product_code, name, model, firm, price):
        self.product_code = product_code
        self.name = name
        self.model = model
        self.firm = firm
        self.price = price

    def __repr__(self): return str(self.__dict__)


products_list = {}

with open('Products.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader, None)
    for row in reader:
        products_list[row[0]] = Product(row[1], row[2], row[3], row[4], int(row[5]))


class Store():
    global cart
    cart = []

    global dateofpurchase
    dateofpurchase = {'date': '', 'bill': '', 'email': '', 'product': ''}

    def displayproducts(self):
        print("The available product are: ")
        for key, value in products_list.items():
            print(key, value)

    def add_to_cart(self, product):
        for key, value in products_list.items():
            if product == key:
                cart.append(value)
        print(f'Product added to cart {key, value}')

    def display(self):
        print('Items in the card')
        for item in cart:
            print(item)

    def remove_from_cart(self, product):
        for item in cart:
            if item.product_code == product:
                cart.remove(item)

    def generate_bill(self):
        global bill
        bill = 0

        for item in cart:
            item.price
            bill += item.price
        dateofpurchase['bill'] = bill
        print(f'Your Bill is: {bill}\nThank you for shopping with us!')

    def display_options(self):
        print(
            "OPTIONS LIST:\n1.Display Products \n2.Add product to cart\n3.Remove Product\n4.View cart\n5.Generate Bill\n6.Exit\n7.Buy product\n8.View Cars")

    def buy_product(self):
        dateofpurchase['product'] = cart
        dateofbuy = datetime.datetime.now()
        dateofpurchase['date'] = dateofbuy
        dateofpurchase['email'] = email
        Store.generate_bill(self)

        with open('buydproducts.csv', mode='a') as productbuy:
            writing = csv.writer(productbuy, delimiter=",")
            writing.writerow(dateofpurchase.values())
        print("Thank you for you purchase. Have a nice day!")

    @classmethod
    def choices(cls):
        print(f"Welcome to the Shop:  {email}")
        s = Store()
        s.display_options()
        x = True
        while x:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                s.displayproducts()
            elif choice == 2:
                product = input("Enter product code: ")
                s.add_to_cart(product)

            elif choice == 3:
                product = input("Enter product code to remove product: ")
                s.remove_from_cart(product)

            elif choice == 4:
                s.display()

            elif choice == 5:
                s.generate_bill()

            elif choice == 6:
                x = False
                print('You have Exited the store! Have a nice day.')

            elif choice == 7:
                s.buy_product()

            elif choice == 8:
                print(car_list)

            else:
                print("Enter a valid choice")

def plotorders(buydproducts, records: int):
    ordersdatabase = read_csvfile(buydproducts)
    datatoplot = [[], [], []]
    for row in ordersdatabase:
        datatoplot[0].append(row[1])
        datatoplot[1].append(float(row[2]) * int(row[5]))
        datatoplot[2].append(float(row[3]) * int(row[6]))

    if records >= len(ordersdatabase):
        records = len(ordersdatabase)

    date = datatoplot[0][-records:]
    expenses = datatoplot[1][-records:]
    incomes = datatoplot[2][-records:]

    labels = []
    for element in date:
        labels.append(datetime.datetime.strptime(element, '%c'))

    x = np.arange(len(labels))

    width = 0.05  # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, incomes, label='incomes')
    rects2 = ax.bar(x + width / 2, expenses, label='expenses')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('EUR')
    ax.set_title('Incomes/Expenses by date')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=90)
    ax.legend()

    ax.bar_label(rects1, padding=5)
    ax.bar_label(rects2, padding=1)

    fig.tight_layout()

    plt.show()

begin()
access(option)

if granted_publiclog:
    Store.choices()
elif granted_adminlog:
    admin_option = input(
        'To enter store type (store),\nEnter (view) to see sells report,\nEnter (remove) to remove a user,\nEnter (lookatinfo) to look at  the info of the users\nEnter (changeinfo) to change the information of the user :')
    if admin_option == 'store':
        Store.choices()

    elif admin_option == 'remove':
        with open('login.csv', mode='w') as remove_user:
            lines = list()
            members = input('Enter the email for removal: ')
            with open('login.csv', mode='r') as remove_user:
                reader = csv.reader(remove_user)
                for row in reader:
                    lines.append(row)
                    for field in row:
                        if field == members:
                            lines.remove(row)
            with open('login.csv', mode='w') as remove_user:
                writer = csv.writer(remove_user)
                writer.writerow(lines)

    elif admin_option == 'view':

        plotorders('buydproducts.csv', 10)

    elif admin_option == 'lookatinfo':

        with open('registered.csv', mode='r') as f:
            lines = f.readlines()
            for line in lines:
                print(line)

    elif admin_option == 'changeinfo':
            lines = list()
            members = input("Please enter a member's name to be deleted.")
            with open('registered.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    lines.append(row)
                    for field in row:
                        if field == members:
                            try:
                                lines.remove(row)
                            except ValueError:
                                print('gips')
            with open('registered.csv', 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(lines)
            access(option)