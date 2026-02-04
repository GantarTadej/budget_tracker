import json
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