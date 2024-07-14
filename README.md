# 💵 Expense Tracker
A simple command-line application designed to help you manage your monthly expenses. 

**Features:**

The application presents a menu with the following options:

- **Add Expense (+):** Enter the name, amount, and category for a new expense.

- **Delete Expense (-):** Choose an expense from the list to delete.

- **Summarize Expense:** View expenses by category, total spending, remaining budget, and daily budget.

- **Quit:** Exit the application.

**How it Works:**
- **Expense Data:** Expenses are saved in a CSV file named expenses.csv.
  
- **Monthly Budget:** The default budget is $200, which you can adjust in the main() function of main.py.
  
- **Expense Categories:** Predefined categories include Food, Entertainment, Home, Transportation, Personal, and Miscellaneous.

**Note:**

To change the default budget amount of $200, you need to update the budget variable in expense_tracker.py:

```ruby
budget = 200  # Set your budget amount here
```

Modify this line to set your preferred budget amount for tracking expenses.



