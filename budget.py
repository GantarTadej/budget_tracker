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

#glavni meni

def main():
    expenses = load_expenses()

    while True:
        print("\n=== Budget Tracker ===")
        print("1. Dodaj Strošek")
        print("2. Preglej Stroške")
        print("3. Izhod")

        choice = input("\nIzberi Opcijo (1-3): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            break
        else:
            print("Napačna izbira, poskusi znova.")

if __name__ == "__main__":
    main()