import json
from datetime import datetime
#Odpre Stroške za branje
def load_expenses():
    try:
        with open('expenses.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
#odpre stroške za pisanje
def save_expenses(expenses):
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file, indent = 4)

#dodaj strošek
def add_expense(expenses):
    amount = float(input("Vnesi vsoto: "))
    category = input("Vnesi kategorijo: (Hrana, Najemnina, Avto, drugo): ")
    description = input("Opis: ") 

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d")
    }    

    expenses.append(expense)
    save_expenses(expenses)
    print("Strošek uspešno dodan!!")

#Preglej Stroške
def view_expenses(expenses):
    if not expenses:
        print("Zaenkrat nimaš stroškov!")
        return 
    
    print("\n--- Tvoji Stroški ---")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['description']} - {expense['amount']:.2f}€ - ({expense['category']} - {expense.get('date', 'N/A')})")

#Skupne vrednosti
def show_totals(expenses):
    if not expenses:
        print("Zaenkrat nimaš stroškov!")
        return 
    
    total = sum(expense['amount'] for expense in expenses)

    category_totals = {}
    for expense in expenses:
        category = expense['category']
        if category in category_totals:
            category_totals[category] += expense['amount']
        else:
            category_totals[category] = expense['amount']
    
    print("\n=== Skupni Stroški ===")
    print(f"Skupaj {total:.2f} €")
    print("\n Po kategorijah: ")
    for category, amount in category_totals.items():
        print(f" {category}: {amount:.2f} €")


#glavni meni

def main():
    expenses = load_expenses()

    while True:
        print("\n=== Budget Tracker ===")
        print("1. Dodaj Strošek")
        print("2. Preglej Stroške")
        print("3. Prikaži skupne Stroške")
        print("4. Izhod")

        choice = input("\nIzberi Opcijo (1-4): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            show_totals(expenses)
        elif choice == '4':
            break
        else:
            print("Napačna izbira, poskusi znova.")

if __name__ == "__main__":
    main()