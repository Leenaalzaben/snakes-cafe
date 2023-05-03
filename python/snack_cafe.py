menu = {
    "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    "Desserts": ["Ice Cream", "Cake", "Pie"],
    "Drinks": ["Coffee", "Tea", "Unicorn Tears"]
}

orders = {}


def startup():
    print('''
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
    ''')


def orderList():
    print(''' 
     ***********************************
     ** What would you like to order? **
     ***********************************
     ''')
    for Selection, items in menu.items():
        print(f"{Selection}:")
        print("-" * len(Selection))
        print()
        for item in items:
            print(f" - {item}")
        print()
        print()


def user_insertion():
    user_input = input(">")
    return user_input


def close_application():
    print("Thank you for choosing Snakes Cafe, We hope to see you again soon!")


startup()

orderList()
while True:
    order = user_insertion()
    if order.lower() == "quit":
        break
    elif order in menu["Appetizers"] + menu["Entrees"] + menu["Desserts"] + menu["Drinks"]:
        if order in orders:
            orders[order] += 1
        else:
            orders[order] = 1
        print(
            f"** {orders[order]} orders of {order} have been added to your meal **")
    else:
        print(
            f"I'm sorry, {order} is not available. Please choose a different option.")

close_application()
