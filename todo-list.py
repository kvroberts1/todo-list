todo = ["Eat a tree", "Listen to Weezer"]
status_off = 0

def print_todo():
    n=1
    print("")
    for i in range(len(todo)):
        print(n, todo[i])
        n=n+1


while status_off == 0:
    print("")
    print("Welcome to your Todo List")
    print("1. Review List")
    print("2. Check Off Item")
    print("3. Add Item to List")
    print("4. Exit Application")

    try:
        user_choice = int(input("Select a Choice: "))
        if user_choice == 4:
            status_off = 1
        else:
            if user_choice == 1:
                print_todo()
            elif user_choice == 2:
                delete_item = int(input("What Item would you like to delete: "))
                try:
                    todo.pop(delete_item)
                    print_todo()
                except IndexError:
                    print("Oops your list is empty or you are trying to delete and item that doesn't exsist.")
            elif user_choice == 3:
                add_item = input("What would you like to add to your list: ")
                todo.append(add_item)
                print_todo()
    except ValueError:
        print("Oops you can only select a number")