import json
from datetime import datetime
# Default categories
DEFAULT_CATEGORIES = ["hrana", "najemnina", "transport", "zabava", "zdravje","DRUGO...", "ostalo", "Dodaj Novo Kategorijo"]
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

def load_categories():
    try:
        with open('categories.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return DEFAULT_CATEGORIES.copy()

def save_categories(categories):
    with open('categories.json', 'w') as file:
        json.dump(categories, file, indent=4)

#dodaj strošek
def add_expense(expenses, categories):
    amount = float(input("Vnesi vsoto: "))

    #razpoložljive kategorije
    print("\nRazpoložljive kategorije: ")
    for i, cat in enumerate(categories, 1):
        if cat == "Dodaj Novo Kategorijo":
            print(f"{i}. {cat}")
        else: 
            print(f"{i}. {cat}")
    
    choice = input("\nIzberi Številko Kategorije: ")
    try:
        cat_index = int(choice) - 1
        if categories[cat_index] == "Dodaj Novo Kategorijo":
            new_category = input("Vnesi novo kategorijo: ").lower()
            categories.insert(-1, new_category)
            save_categories(categories)
            category = new_category
            print(f"Nova kategorija >{new_category}< dodana! ")
        else:
            category = categories[cat_index]
    except (ValueError, IndexError):
        print("Napačna Izbira, uporabljam 'ostalo'")
        category = 'ostalo'
    
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

#izbriši strošek
def delete_expense(expenses):
    if not expenses:
        print("Zaenkrat nimaš Stroškov!")
        return
    #Pod meni
    print("\n=== Izbriši Strošek ===")
    print("1. Izbriši zadnji Strošek (Hitro)")
    print("2. Izberi Strošek za izbris")
    print("3. Prekliči")

    choice = input("\nIzberi (1-3): ")

    if choice == '1':#hiter zadnji izbris
        last = expenses[-1]
        print(f"Zadnji strošek {last['description']} - {last['amount']:.2f}€")
        confirm = input("Izbrišem ta strošek? (da/ne): ").lower()

        if confirm == 'da':
            deleted = expenses.pop()
            save_expenses(expenses)
            print(f"Strošek '{deleted['description']}' {deleted['amount']}€  Izbrisan!")
        else:
            print("Preklicano. ")
        

    elif choice == '2':
        #Izbris po izbiri
        print("\n--- Tvoji Stroški ---")
        for i, expense in enumerate(expenses, 1):
            print(f"{i}. {expense['description']} - {expense['amount']:.2f}€ - ({expense['category']}) - {expense.get('date', 'N/A')}")
        try:
            num = int(input("\nVnesi številko stroška za izbris (0 za preklic): "))

            if num == 0:
                print("Preklicano.")
                return
            
            if 1 <= num <= len(expenses):
                expense_to_delete = expenses[num - 1]
                confirm = input(f" Izbrišem '{expense_to_delete['description']}' ? (da/ne): ").lower()    

                if confirm == 'da':
                    deleted = expenses.pop(num - 1)
                    save_expenses(expenses)
                    print(f" Strošek '{deleted['description']}' izbrisan!")
                    
                else:
                    print("Preklicano.")
            else: 
                print("Napačna Številka!")

        except ValueError:
            print("Vnesi veljavno Število!")

    elif choice == '3':
        print("Preklicano.")

    else:
        print("Neveljavna Izbira!")                





#glavni meni

def main():
    expenses = load_expenses()
    categories = load_categories()

    while True:
        print("\n=== Budget Tracker ===")
        print("1. Dodaj Strošek")
        print("2. Preglej Stroške")
        print("3. Prikaži skupne Stroške")
        print("4. Izbriši Strošek")
        print("5. Izhod")

        choice = input("\nIzberi Opcijo (1-5): ")

        if choice == '1':
            add_expense(expenses, categories)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            show_totals(expenses)
        elif choice == '4':
            delete_expense(expenses)
        elif choice == '5':
            break
        else:
            print("Napačna izbira, poskusi znova.")

if __name__ == "__main__":
    main()