# cdv-pai

## Instalacja

Linux
1. Wejść do katalogu application
2. virtualenv .venv
3. pip install flask Flask-SQLAlchemy

Windows
1. Wejść do katalogu application
2. python -m venv venv
3. pip install flask Flask-SQLAlchemy

## Uruchomienie
Linux
1. W konsoli wejść do katalogu application
2. virtualenv .venv
3. source .venv/bin/activate
4. flask run

Windows
1. W konsoli wejść do katalogu application
2. .\venv\Scripts\activate
3. flask run

Co trzeba jeszcze zrobic:
1. podłączyć z bazą danych (zrobiłem)
2. po dodaniu nowego wydatku saldo portfela musi sie zmniejszyc (zrobilem)
3. moze dac jakis warunek który sprawdza czy inputy nie są puste
4. dodac mozliwosc usuwania wydatkow
5. sprawdzenie czy nie ma za malo pieniedzy podczas dodawania wydaktu
6. zablokowanie dodania ujemnych pieniedzy (zrobilem)
7. ostrzezenia po odswiezeniu strony nie znikaja
8. spakować aplikację w kontener
9. dopracować dokumentację

Można rozwijać o:
1. Dodawanie nazwy dodawanego przychodu
2. Dodanie tabeli z wyświetlaniem, usuwaniem i edycją przychodów

## Baza danych
Aplikacja wykorzystuje bazę danych SQLite. Plik bazy danych jest zapisywany w katalogu application/app/db.

Tabele:
- Expenses - zapisywanie bieżących wydatków
