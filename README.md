# Budget Tracker
Kratek stroškovnik v Pythonu z modularno strukturo in SQLite bazo.

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
├── fileoperations.py   # SQLite database handling
├── budget.db           # SQLite baza (avtomatsko ustvarjena)
└── .gitignore
```

## Kaj sem se naučil
- JSON file operations (read/write)
- Python datetime modul
- Modularizacija kode / separation of concerns
- Input validation z while/try-except
- Osnovni Git workflow in GitHub
- Generator expressions
- SQLite database design (tabele, primary/foreign keys, normalizacija)
- SQL osnove: SELECT, INSERT, UPDATE, DELETE, JOIN
- Parameterized queries (SQL injection zaščita)
- Transakcije (commit/rollback)

## Prihodnje izboljšave
- Flask web interface
- GROUP BY statistike v show_totals()
- Več funkcionalnosti za vnose
- First time setup