# Budget Tracker
Kratek stroškovnik v pythonu z modularno strukturo

## Project Structure
```
budget-tracker/
├── budget.py           # Main program with expense management
├── validation.py       # Input validation functions
├── fileoperations.py   # JSON file handling
├── expenses.json       # Expense data storage
├── categories.json     # Category data storage
└── .gitignore         # Git ignore rules
```

## Features 
- Dodaj strošek z kategorijo in vsoto
- **Robustna validacija vnosov** (preprečuje napake in crashe)
- **Avtomatsko dodajanje datumov** 
- **Prilagodljive kategorije** (vnaprej določene + možnost dodajanja novih) 
- **Upravljanje kategorij** (izbris nepotrebnih kategorij)
- Izpiši stroške
- **Prikaži skupne stroške po kategorijah** 
- **Izbris stroškov** (hitri izbris zadnjega ali izbira po seznamu)
- .json za shranjevanje
- settings (v procesu dodajanja)

## How to Run
```bash
python budget.py
```

## What I Learned
- delo z json file (read/write Json)
- Funkcije in dictionary
- vnosi in zanke
- Git osnove od osnov in GitHub
- **Python datetime modul**
- **Delo z več JSON files**
- **Dinamični meniji** 
- **List manipulation** (pop, remove)
- **Sub-menus in user flow**
- **Modularizacija kode** (ločevanje v več datotek)
- **Input validation z while loops in try/except**
- **PEP 8 naming conventions**
- **Reusable functions**

## Future Improvements
- **Filtriranje po datumu**
- Prikaz z ascii ali eno izmed knjižnic
- **Export v CSV**
- Mesečni budget (Varčevalnik, Vnos plače)
- Čez 20 let => poveži z kartico
- Unit testing