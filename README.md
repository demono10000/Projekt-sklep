Dokumentacja projektu
=====================
Projekt został stworzony w ramach przedmiotu "Programowanie obiektowe" na Wyższej Szkole Informatyki i Zarządzania w Rzeszowie.

Uruchomienie projektu
----------------------
Aby uruchomić projekt należy wykonać następujące kroki:
1. Pobrać projekt z repozytorium
2. Otworzyć konsolę w folderze z projektem
3. Wykonać komendę ```python manage.py runserver```

Alternatywnie można przetestować działanie aplikacji na stronie: http://demono10000.eu.pythonanywhere.com/

Panel administracyjny
-------------
Aby uzyskać dostęp do panelu administracyjnego lokalnie należy:
1. Wejść na stronę http://127.0.0.1:8000/admin
2. Zalogować się danymi: login: admin, hasło: admin

W przypadku kożystania z hostowanej strony należy:
1. Wejść na stronę http://demono10000.eu.pythonanywhere.com/admin
2. Zalogować się danymi: login: admin, hasło: admin

W panelu można dodawać nowe usługi w zakładce "Services" (ścieżka: /admin/main/service/) po naciśnięciu przycisku ADD SERVICE

![add](https://user-images.githubusercontent.com/48636182/206041383-9e40434c-3373-4ea9-a37f-74209385cf15.png)

Otwiera się wtedy formularz w którym należy uzupełnić informacje dotyczące nowej usługi

![ss2](https://user-images.githubusercontent.com/48636182/206041779-b3bc6915-3c1b-4441-8262-7542b1c75369.png)

W panelu można również zobaczyć wszystkie zamówienia w zakładce "Orders" (ścieżka: /admin/main/order/), oraz zamówienia, które nie zostały jeszcze zrealizowane w zakładce "Pending orders" (ścieżka: /admin/main/orderproxy/)

![image](https://user-images.githubusercontent.com/48636182/206170153-e835bd7b-d840-4562-8e1f-6ba8e426ed20.png)

W panelu administratora można oprócz dodawania i odczytu rekordów z bazy danych, również edytować i usuwać dane.

Interfejs użytkownika
---------------------
Aby użytkownik mógł korzystać z serwisu musi stworzyć konto i się na nie zalogować. Niezalogowany użytkownik ma zablokowany dostęp do wszystkich funkcjonalności serwisu oprócz rejestracji i logowania.

![image](https://user-images.githubusercontent.com/48636182/206172196-71cb367c-7768-420b-a943-0cb2104056d4.png)

Po zalogowaniu użytkownik ma opcję doładowania swojego konta, aby móc dokonywać płatności za usługi.

![image](https://user-images.githubusercontent.com/48636182/206172586-341ac62d-28da-4b39-b23c-c018d01ab09f.png)

Następnie użytkownik może już zakupić usługę, która jest dostępna w serwisie.

![image](https://user-images.githubusercontent.com/48636182/206172776-e8d2fe52-a823-4969-bb0d-28b29fc3d687.png)

![image](https://user-images.githubusercontent.com/48636182/206172977-7afafe9c-c4f1-4ab2-a1b8-bd8b217a03ab.png)

![image](https://user-images.githubusercontent.com/48636182/206173066-57ecea2e-c6e7-42fc-b7ec-f0748a8d8c9e.png)

![image](https://user-images.githubusercontent.com/48636182/206173118-c90eee61-ed8d-4d57-a2a5-fdc8466c9c8f.png)

Backend
-------
Drzewo katalogów projektu:

![image](https://user-images.githubusercontent.com/48636182/206174662-be2deeaf-0a96-47d4-8b7c-9498a19e2a5e.png)

Modele

![image](https://user-images.githubusercontent.com/48636182/206174907-3b64edc2-1111-4c54-af9e-d6ef04273290.png)

Adresy URL

![image](https://user-images.githubusercontent.com/48636182/206175048-f63bcf82-9388-42fc-97eb-2da55471a7ed.png)

Przykładowe testy

![image](https://user-images.githubusercontent.com/48636182/206175474-bdcdcd11-e16f-4a48-9011-970c20b6b8e8.png)

Wszystkie testy znajdują się w folderze tests https://github.com/demono10000/Projekt-sklep/tree/master/tests

Testy wykonuje się poprzez komendę ```python manage.py test```

Baza danych db.sqlite3

![image](https://user-images.githubusercontent.com/48636182/206176266-d87e28bd-6b43-445e-88f7-266e45617fea.png)

Obsługa zapytań, walidacja danych, obsługa wyjątków i zwracanie danych odbywa się w pliku views.py (/main/views.py)

https://github.com/demono10000/Projekt-sklep/blob/master/main/views.py