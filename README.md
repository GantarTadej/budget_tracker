# Budget Tracker
Kratek stroškovnik v Pythonu z modularno strukturo

## Funkcionalnosti
- Dodajanje/brisanje stroškov z avtomatskim datumom
- Prilagodljive kategorije z zaščito pred duplikati  
- Mesečni proračun tracking
- Pregledi po kategorijah
- Robustna validacija vnosov

## Kako uporabiti
```bash
python budget.py
```

## Struktura projekta
```
budget-tracker/
├── budget.py           # Glavna aplikacija
├── validation.py       # Input validacija
├── fileoperations.py   # JSON datoteke handling
├── expenses.json       # Stroški
├── categories.json     # Kategorije  
├── settings.json       # Nastavitve
└── .gitignore
```

## Kaj sem se naučil
- JSON file operations (read/write)
- Python datetime modul
- Modularizacija kode
- Input validation z while/try-except
- Osnovni Git workflow in GitHub
- Generator expressions

## Prihodnje izboljšave
- Flask web interface
- SQLite database
- Več funkcionalnosti za vnose
- First time setup