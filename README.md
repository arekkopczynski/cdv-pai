# cdv-pai

Instalacja na linuxie
1. Wejść do katalogu application
2. virtualenv .venv
3. pip install flask Flask-SQLAlchemy

Instalacja na windows
1. Wejść do katalogu application
2. python -m venv venv
3. pip install flask Flask-SQLAlchemy

Uruchomienie na Linux
1. W konsoli wejść do katalogu application
2. virtualenv .venv
3. source .venv/bin/activate
4. flask run

Uruchomienie na Windows
1. W konsoli wejść do katalogu application
2. .\venv\Scripts\activate
3. flask run

co trzeba jeszcze zrobic:
1. podłączyć z bazą danych (zrobiłem)
2. po dodaniu nowego wydatku saldo portfela musi sie zmniejszyc (zrobilem)
3. moze dac jakis warunek który sprawdza czy inputy nie są puste
4. dodac mozliwosc usuwania wydatkow
5. sprawdzenie czy nie ma za malo pieniedzy podczas dodawania wydaktu
6. zablokowanie dodania ujemnych pieniedzy (zrobilem)
7. ostrzezenia po odswiezeniu storny nie znikaja

h2. Baza danych
Aplikacja wykorzystuje bazę danych SQLite. Plik bazy danych jest zapisywany w katalogu application/app/db.

Tabele:
- Expenses - zapisywanie bieżących wydatków
