print("Welcome to Expense Tracker")

expense_list = []

while True:
    
    print("""
          ========= MENU ========
          1. Add Expense
          2. View all Expenses
          3. View Total Spending
          4. Exit
          """)
    
    user_choice = int(input("What operation you want to perform? :"))
    
    
    if user_choice == 1:
        date = input("Enter date (DD-MM-YYYY):")
        category = input("Enter category (Food, Travel, etc):")
        description = input("Enter description (optional): ")
        amount = int(input("Enter Amount: "))
        
        expense = {
            "Date" : date,
            "Category" : category,
            "Description" : description,
            "Amount" : amount
        }
        
        expense_list.append(expense)
        print("Expense is added successfully!")
        
    elif user_choice == 2:
        if len(expense_list) == 0:
            print("You have not added any expense")
        
        else:
            count = 1
            for item in expense_list:
                print(f"{count} -> {item['Date']}, {item['Category']}, {item['Description']}, {item['Amount']}")
                count = count + 1
    
    elif user_choice == 3:
        total = 0
        for item in expense_list:
            total = total + item["Amount"]
            
        print(f"Total Spending -> {total}")
    
    elif user_choice == 4:
        print("Thank You for trying our application")
        break
    
    else:
        print("Please enter the correct input:")
        
            
        