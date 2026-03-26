expenses = []

while True:
    print("\n==== Expense Tracker ====")
    print("1. Add expense")
    print("2. Show all expenses")
    print("3. Show total")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        try:
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            expenses.append((amount, category))
            print("Expense added.")
        except:
            print("Invalid input.")

    elif choice == "2":
        if not expenses:
            print("No expenses yet.")
        else:
            for e in expenses:
                print(f"{e[1]}: {e[0]}")

    elif choice == "3":
        total = sum([e[0] for e in expenses])
        print("Total spending:", total)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")