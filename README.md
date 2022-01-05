# cdv-pai

odpalenie srodowiska 
1. wejsc w katalog aaa (trzeba zmienic nazwe przy okazji)
2. .\venv\Scripts\activate
3. potem flask run zeby odpalic server



na linuxie
1. virtualenv .venv
2. source .venv/bin/activate
3. flask run

aktualny status jest taki, że jest prosty 
front i po dodaniu wartosci aktualizują się odpowienie elementy

co trzeba jeszcze zrobic:
1. podłączyć z bazą danych
2. po dodaniu nowego wydatku saldo portfela musi sie zmniejszyc (zrobilem)
3. moze dac jakis warunek który sprawdza czy inputy nie są puste 
4. dodac mozliwosc usuwania wydatkow
5. sprawdzenie czy nie ma za malo pieniedzy podczas dodawania wydaktu
6. zablokowanie dodania ujemnych pieniedzy (zrobilem)
7. ostrzezenia po odswiezeniu storny nie znikaja