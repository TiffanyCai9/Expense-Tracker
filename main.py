from expense import Expense
import calendar
import datetime

def main():
    print("Running Expense Tracker! 💵͜ |• - •|>")
    expense_file_name = "expenses.csv"
    budget = 200

    # Display the main menu options
    while True:
        print("\n1. Add expense (+)")
        print("2. Delete expense (-)")
        print("3. Summarize expense")
        print("4. Quit")

        option = input("Choose an option (1-4): ")

        if option == '1':
            expense = get_user_expense()
            if expense:
                save_expense_to_file(expense, expense_file_name)
        elif option == '2':
            delete_expense(expense_file_name)
        elif option == '3':
            summarize_expense(expense_file_name, budget)
        elif option == '4':
            print("Exiting Expense Tracker. See you next time! |˶˙ᵕ˙ )ﾉﾞ")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

def get_user_expense():
    # Get the details of a new expense from the user
    print("💵 Getting User Expense")
    expense_name = input("Enter expense name: ")
    while True:
        try: 
            expense_amount = float(input("Enter expense amount: "))
            if expense_amount <= 0:
                raise ValueError("Expense amount must be greater than zero.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid amount")
        
    print(f"You've entered {expense_name}, {expense_amount}")

    expense_categories = [
        "Food 𓌉◯𓇋",
        "Entertainment \\(>o<)/",
        "Home 𓉞",
        "Transportation \ō͡≡o˞̶",
        "Personal 𖠋",
        "Misc ⟡"
    ]
    
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories, 1):
            print(f"    {i}. {category_name}")
        
        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name= expense_name, category= selected_category, amount = expense_amount)
            return new_expense
        else: 
            print("Invalid category. Please try again!")

def save_expense_to_file(expense, expense_file_name):
    # Save the expense to the CSV file, expenses.csv
    print(f"💵 Saving User Expense: {expense} to {expense_file_name}")
    with open(expense_file_name, "a") as file:
        file.write(f"{expense.name}, {expense.amount}, {expense.category}\n")

def summarize_expense(expense_file_name, budget):
    # Read expenses from the file and generate a summary report
    print("💵 Summarizing User Expense") 
    expenses = []
    with open(expense_file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_amount, expense_category = stripped_line.split(",")
            line_expense = Expense(
                name=expense_name, amount=float(expense_amount), category=expense_category
            )
            expenses.append(line_expense)

    category_amount = {}
    for expense in expenses:
        key = expense.category
        if expense in category_amount:
            category_amount[key] += expense.amount
        else:
            category_amount[key] = expense.amount
    print("Expenses by Category: ")
    for key, amount in category_amount.items():
        print(f"    {key}: ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"💵 You've spent ${total_spent:.2f} this month!")

    remaining = budget - total_spent
    print(f"💵 Remaining Budget: ${remaining:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining / remaining_days
    print(f"💵 Budget Per Day: ${daily_budget:.2f}")

def delete_expense(expense_file_name):
    # Delete an expense from the CSV file
    print("💵 Deleting User Expense")
    print("Printing Expenses")

    with open(expense_file_name, 'r') as my_file:
        lines = my_file.readlines()

    if not lines:
        print("No expenses to delete.")
        return
        
    print("Current Expenses:")
    for i, line in enumerate(lines, 1):
        print(f"    {i}. {line.strip()}")
    
    while True:
        try: 
            index_to_delete = int(input(f"Choose an expense to delete (1 - {len(lines)}): ")) - 1
            
            if index_to_delete + 1 > len(lines) or index_to_delete + 1 < 1:
                print(f"Choice must be between 1 and {len(lines)}")
                continue

            lines.pop(index_to_delete)
            with open(expense_file_name, 'w') as file:
                file.writelines(lines)
            print("Successfully deleted expense! ")
            break
        except ValueError:
            print("Invalid input. Please try again!")

if __name__ == "__main__":
    main()
