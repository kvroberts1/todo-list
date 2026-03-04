todo = ["Eat a tree"]
status_off = 0

while status_off == 0:
    print("Welcome to your Todo List")
    print("1. Review List")
    print("2. Check Off Item")
    print("3. Add Item to List")
    print("4. Exit Application")

    user_choice = int(input("Select a Choice: "))

    if user_choice == 4:
        status_off = 1
    else:
        if user_choice == 1:
            print(todo)
        else:
            print("Woo cowboy")