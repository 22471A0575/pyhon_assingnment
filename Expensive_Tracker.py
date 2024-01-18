expenses={}
def add_expense():
    category=input("Enter expense category: ")
    amount=float(input("Enter expense amount: $"))
    if category in expenses:
        expenses[category]+=amount
    else:
        expenses[category]=amount
def view_expenses():
    for category,amount in expenses.items():
        print(f"{category}:${amount}")
while True:
    print("\nOptions:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    choice=input("Enter your choice (1, 2, or 3): ")
    if choice=="1":
        add_expense()
    elif choice=="2":
        view_expenses()
    elif choice=="3":
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
