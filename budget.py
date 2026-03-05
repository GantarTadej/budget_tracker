import sqlite3
from datetime import datetime
from validation import get_valid_int, get_valid_float
from fileoperations import initialize_db, delete_category, db_delete_expense, load_expenses, save_expense, load_categories, save_category, load_settings, save_settings, reassign_category

#dodaj strošek
def add_expense():
    amount = get_valid_float("Vnesi vsoto: ", min_value=0.01)

    categories = load_categories()

    print("\nRazpoložljive kategorije: ")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    print(f"{len(categories) + 1}. Dodaj Novo Kategorijo")

    choice = get_valid_int("\nIzberi Številko Kategorije: ", min_value=1, max_value=len(categories) + 1)

    if choice == len(categories) + 1:
        category = get_or_create_category()
    else:
        category = categories[choice - 1]

    description = input("Opis: ")
    date = datetime.now().strftime("%Y-%m-%d")

    save_expense(amount, description, date, category)
    print("Strošek uspešno dodan!!")

#Preveri kategorije nova/stara
def get_or_create_category():
    categories = load_categories()
    while True:
        user_input = input("Vnesi novo kategorijo: ").strip()
        normalized_input = user_input.casefold()
        
        existing = next((cat for cat in categories if cat.casefold() == normalized_input), None)
        
        if existing:
            print(f"Kategorija '{existing}' že obstaja!")
            choice = input("Uporabi obstoječo kategorijo? (da/ne): ").lower()
            if choice == 'da':
                return existing
            else:
                print("Vnesi drugo ime kategorije.")
        else:
            save_category(user_input)
            print(f"Nova kategorija '{user_input}' dodana!")
            return user_input
        
#Preglej Stroške
def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("Zaenkrat nimaš stroškov!")
        return 
    
    print("\n--- Tvoji Stroški ---")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['description']} - {expense['amount']:.2f}€ - ({expense['category']} - {expense['date']})")

#Skupne vrednosti
def show_totals():
    expenses = load_expenses()
    settings = load_settings()
    if not expenses:
        print("Zaenkrat nimaš stroškov!")
        return 
    current_month = datetime.now().month
    current_year = datetime.now().year
    total = sum(expense['amount'] for expense in expenses)

    category_totals = {}
    for expense in expenses:
        category = expense['category']
        if category in category_totals:
            category_totals[category] += expense['amount']
        else:
            category_totals[category] = expense['amount']
    
    monthly_expenses = [
        exp for exp in expenses 
        if datetime.strptime(exp['date'], '%Y-%m-%d').month == current_month 
        and datetime.strptime(exp['date'], '%Y-%m-%d').year == current_year
        ]
    monthly_total = sum(exp['amount'] for exp in monthly_expenses)

    print("\n=== Skupni Stroški ===")
    print(f"Skupaj (vse): {total:.2f}€")

    print("\n--- Po Kategorijah ---")
    for category, amount in category_totals.items():
        print(f"  {category}: {amount:.2f}€")

    print(f"\n--- Ta Mesec ---")
    print(f"Stroški ta mesec: {monthly_total:.2f}€")

    if settings['monthly_budget'] > 0:
        budget = settings['monthly_budget']
        percentage = (monthly_total / budget) * 100
        remaining = budget - monthly_total
    
        print(f"Proračun: {budget:.2f}€")
        print(f"Porabljeno: {percentage:.1f}%")
    
        if monthly_total > budget:
            print(f"Pozor!  Prekoračitev: {abs(remaining):.2f}€")
        else:
            print(f"Ostaja: {remaining:.2f}€")
    else:
        print("(Proračun ni nastavljen)")

#izbriši strošek
def delete_expense():
    expenses = load_expenses()
    
    if not expenses:
        print("Zaenkrat nimaš Stroškov!")
        return

    print("\n=== Izbriši Strošek ===")
    print("1. Izbriši zadnji Strošek (Hitro)")
    print("2. Izberi Strošek za izbris")
    print("3. Prekliči")

    choice = get_valid_int("\nIzberi (1-3): ", min_value=1, max_value=3)

    if choice == 1:
        last = expenses[-1]
        print(f"Zadnji strošek {last['description']} - {last['amount']:.2f}€")
        confirm = input("Izbrišem ta strošek? (da/ne): ").lower()
        if confirm == 'da':
            delete_expense(last['id'])
            print(f"Strošek '{last['description']}' izbrisan!")
        else:
            print("Preklicano.")

    elif choice == 2:
        for i, expense in enumerate(expenses, 1):
            print(f"{i}. {expense['description']} - {expense['amount']:.2f}€ - ({expense['category']}) - {expense['date']}")
        
        num = get_valid_int("\nVnesi številko: ", min_value=0, max_value=len(expenses))
        if num == 0:
            print("Preklicano.")
            return
        
        expense_to_delete = expenses[num - 1]
        confirm = input(f"Izbrišem '{expense_to_delete['description']}' ? (da/ne): ").lower()
        if confirm == 'da':
            db_delete_expense(expense_to_delete['id'])  # and here?
            print(f"Strošek '{expense_to_delete['description']}' izbrisan!")
        else:
            print("Preklicano.")

    elif choice == 3:
        print("Preklicano.")


#uredi kategorije
def manage_categories():
    categories = load_categories()
    expenses = load_expenses()
    print("\n=== Uredi Kategorije ===")
    print("\nObstoječe kategorije: ")

    user_categories = []
    for i, cat  in enumerate(categories):
        if cat not in ["ostalo"]:
            user_categories.append(cat)
            #koliko stroškov uporablja to kategorijo
            count = sum(1 for exp in expenses if exp['category'] == cat)
            print(f"{len(user_categories)}. {cat} ({count} stroškov)")
    if not user_categories:
        print("Nimaš kategorij!")
        return
    
    print("\n0. Prekliči.")

    choice = get_valid_int("\nVnesi Številko kategorije za izbris (0 za preklic): ", min_value = 0, max_value = len(user_categories))

    if choice == 0:
        print("Preklicano. ")
        return
    cat_to_delete = user_categories[choice - 1]
    expense_count = sum(1 for exp in expenses if exp['category'] == cat_to_delete)

    if expense_count > 0:
        print(f"Pazi: {expense_count} stroškov uporablja to kategorijo.")
        confirm = input(f"Izbrišem '{cat_to_delete}' ? Stroški bodo kopirani pod 'ostalo'. (da/ne): ").lower()
    else:
        confirm = input(f"Izbrišem '{cat_to_delete}'? (da/ne): ")
    if confirm == 'da':
        reassign_category(cat_to_delete)
        delete_category(cat_to_delete)
        print(f"Kategorija '{cat_to_delete}' izbrisana.")
    else:
        print("Preklicano.")

#Nastavitve
def settings_menu():
    settings = load_settings()
    print("\n=== Nastavitve ===")
    print(f"1. Nastavi mesečni proračun (trenutno: {settings['monthly_budget']:.2f}€)")
    print("2. Nazaj")
    
    choice = get_valid_int("Izberi (1-2): ", min_value=1, max_value=2)
    
    if choice == 1:
        new_budget = get_valid_float("Vnesi mesečni proračun: ", min_value=0.01)
        settings['monthly_budget'] = new_budget
        save_settings(settings)
        print(f"Mesečni proračun nastavljen na {new_budget:.2f}€")
        
    elif choice == 2:
        return

#glavni meni

def main():
    initialize_db()

    while True:
        print("\n=== Budget Tracker ===")
        print("1. Dodaj Strošek")
        print("2. Preglej Stroške")
        print("3. Prikaži skupne Stroške")
        print("4. Izbriši Strošek")
        print("5. Izbriši Kategorijo")
        print("6. Nastavitve")
        print("7. Izhod")

        choice = get_valid_int("Vnesi izbiro med 1 in 6: ", min_value = 1, max_value = 7)

        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice ==  3:
            show_totals()
        elif choice == 4:
            delete_expense()
        elif choice == 5:
            manage_categories()
        elif choice == 6:
            settings_menu()
        elif choice == 7:
            break
        else:
            print("Napačna izbira, poskusi znova.")

if __name__ == "__main__":
    main()