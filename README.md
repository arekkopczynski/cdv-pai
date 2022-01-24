# cdv-pai

# Aplikacja Mój portfel

Aplikacja pozwalająca w prosty sposob zarzadzać portfelem w tym:
- notować wydatki,
- dodawać przychody

Język programowania: Python/Flask

# Uruchomienie - Docker

Uruchomienie za pomocą docker-compose

```
docker-compose up
```

Alternatywnie mozna zbudowac obraz za pomocą
```
docker build --tag cdv-pai .
```

Uruchomienie z obrazu
```
docker run -p 5000:5000 -d cdv-pai
```
Aplikacja nasłuchuje na porcie 5000

# Baza danych
Aplikacja wykorzystuje bazę danych SQLite. Plik bazy danych jest zapisywany w katalogu application/app/db.

Tabele:
- Expenses - zapisywanie bieżących wydatków
- Incomes - zapisywanie dochodów

# Instalacja lokalna

Aplikację można uruchomić rownież z poziomu lokalnej maszyny.

Linux
1. Wejść do katalogu application
2. virtualenv .venv
3. pip install flask Flask-SQLAlchemy

Windows
1. Wejść do katalogu application
2. python -m venv venv
3. pip install flask Flask-SQLAlchemy

# Uruchomienie lokalne
Linux
1. W konsoli wejść do katalogu application
2. virtualenv .venv
3. source .venv/bin/activate
4. flask run

Windows
1. W konsoli wejść do katalogu application
2. .\venv\Scripts\activate
3. flask run

# Możliwości rozwoju
1. Dodawanie nazwy dodawanego przychodu
2. Dodanie tabeli z wyświetlaniem, usuwaniem i edycją przychodów
