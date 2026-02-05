import json
# Default categories
DEFAULT_CATEGORIES = ["hrana", "najemnina", "transport", "zabava", "zdravje","DRUGO...", "ostalo", "Dodaj Novo Kategorijo"]
# Default settings
DEFAULT_SETTINGS = {
    "monthly_budget": 0.0
}
#Odpre Stroške za branje
def load_expenses():
    try:
        with open('expenses.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Napaka pri branju expenses.json. Uporabljam prazno bazo.")
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
    except json.JSONDecodeError:
        print("Napaka pri branju categories.json. Uporabljam privzete kategorije.")
        return DEFAULT_CATEGORIES.copy()

def save_categories(categories):
    with open('categories.json', 'w') as file:
        json.dump(categories, file, indent=4)

def load_settings():
    try:
        with open('settings.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return DEFAULT_SETTINGS.copy()
    except json.JSONDecodeError:
        print("⚠️  Napaka pri branju settings.json. Uporabljam privzete nastavitve.")
        return DEFAULT_SETTINGS.copy()

def save_settings(settings):
    with open('settings.json', 'w') as file:
        json.dump(settings, file, indent=4)