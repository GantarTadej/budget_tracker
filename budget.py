import json

#Odpre Stroške za branje
def load_expenses():
    try:
        with open('expenses.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
#odpre stroške za pisanje

def save_expenses():
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file, indent = 4)


        