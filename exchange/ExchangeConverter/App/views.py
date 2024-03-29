"""
URL configuration for ExchangeConverter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
Zadanie zaliczeniowe z Django
Imię i nazwisko ucznia: Tobiasz Borysionek
Data wykonania zadania: 26.03.2024r. 23.13
Treść zadania: 11. Aplikacja przeliczająca waluty. (Tobiasz Borysionek)
Opis funkcjonalności aplikacji: 
Java script:
Na początku definiowane są stałe (const), które odwołują się do elementów HTML za pomocą ich identyfikatorów (ID). Są to pola wyboru walut (currency-one i currency-two), pola wprowadzania kwoty (amount-one i amount-two), przycisk zamiany walut (swap) oraz element wyświetlający aktualny kurs (rate).
Funkcja calculate() jest zdefiniowana, aby wykonać obliczenia konwersji walutowej. Po wywołaniu pobiera wartości wybranych walut oraz kwoty do przeliczenia.
Następnie funkcja wykonuje żądanie do zewnętrznego API (ExchangeRate-API), aby uzyskać aktualne kursy walutowe. Adres URL żądania jest tworzony na podstawie wybranej waluty źródłowej (curr1).
Po uzyskaniu odpowiedzi z API, funkcja przetwarza ją jako dane JSON. Następnie aktualizuje element HTML (theRate), aby wyświetlić aktualny kurs wymiany między wybranymi walutami.
Dodatkowo, oblicza kwotę w walucie docelowej (amount2) na podstawie wprowadzonej kwoty w walucie źródłowej (amount1) i kursu wymiany.
Są również dodane nasłuchiwacze zdarzeń (event listeners) na polach wyboru walut, polach wprowadzania kwoty oraz przycisku zamiany walut. Gdy użytkownik zmienia wybraną walutę, wprowadza kwotę lub kliknie przycisk zamiany walut, wywoływana jest funkcja calculate(), która aktualizuje wyniki konwersji.
Przycisk zamiany walut (swap) zamienia wybrane waluty miejscami, po czym ponownie wywołuje funkcję calculate(), aby odzwierciedlić zmianę w kalkulacji.

html:
Struktura strony HTML:
Nagłówek (header) zawiera nazwę aplikacji oraz nazwę kantoru wymiany walut.
Sekcja jumbotron zawiera tytuł oraz obrazek związany z kantorem wymiany walut.
Formularz do konwersji walut zawiera:
Pole wyboru waluty źródłowej (currency-one) oraz pole wprowadzania kwoty (amount-one).
Przycisk "Swap" (swap) służący do zamiany walut miejscami.
Pole wyboru waluty docelowej (currency-two) oraz pole wprowadzania kwoty wynikowej (amount-two).
Stopka (footer) zawiera informacje o autorze projektu oraz użytych technologiach.
Stylowanie:
Wykorzystane są arkusze stylów Bootstrap oraz Font Awesome do stylizacji i ikon.
Wykorzystane są również style inline do dodatkowego dostosowania wyglądu elementów.
Skrypty JavaScript:
Na końcu strony dołączony jest skrypt JavaScript (script.js), który implementuje logikę kalkulatora walutowego.
Skrypt ten zawiera funkcje do pobierania kursów walut z zewnętrznego API oraz do obliczania konwersji walutowej na podstawie wybranych wartości i kursów.
Dynamiczne elementy:
Elementy takie jak currency-one, currency-two, amount-one, amount-two i rate są manipulowane dynamicznie przez skrypt JavaScript w celu wykonywania konwersji walutowej bez konieczności odświeżania strony.
Responsywność:
Wykorzystane są klasy Bootstrapa, które sprawiają, że strona jest responsywna i dobrze wygląda na różnych urządzeniach.

urls.py:
from django.contrib import admin: Importuje moduł admin z biblioteki Django, który umożliwia tworzenie panelu administracyjnego.
from django.urls import path: Importuje funkcję path z modułu urls z Django, która jest używana do definiowania wzorców adresów URL.
from App import views: Importuje moduł views z aplikacji o nazwie App. Prawdopodobnie ten moduł zawiera widoki aplikacji.
from django.conf import settings: Importuje moduł settings z Django, który zawiera ustawienia konfiguracyjne dla projektu.
from django.conf.urls.static import static: Importuje funkcję static z modułu urls w celu obsługi plików statycznych, takich jak obrazy, arkusze stylów CSS itp.
urlpatterns: Jest to lista wzorców adresów URL, które Django będzie przetwarzać. W tej konfiguracji są dwa elementy:
path('admin/', admin.site.urls): Przekierowuje zapytania na adres URL /admin/ do panelu administracyjnego Django.
path('', views.index, name="index"): Przekierowuje zapytania na podstawową stronę (root URL) na widok o nazwie index w module views aplikacji App.

views.py:
from django.shortcuts import render: Importuje funkcję render z modułu shortcuts Django. Funkcja ta służy do renderowania szablonów HTML i zwracania ich jako odpowiedzi na żądania HTTP.
def index(request): Definiuje funkcję widoku o nazwie index, która przyjmuje obiekt request jako argument. Obiekt ten zawiera informacje o żądaniu HTTP, które zostało przesłane do serwera.
template = 'index.html': Przypisuje nazwę szablonu HTML do zmiennej template. W tym przypadku nazwa szablonu to 'index.html'.
return render(request, template): Renderuje szablon HTML o nazwie index.html i zwraca go jako odpowiedź na żądanie HTTP. Funkcja render przyjmuje obiekt request oraz nazwę szablonu i zwraca gotowy do wysłania jako odpowiedź dokument HTML.

setting.py:

import os

STATIC_URL = 'static/'
MEDIA_URL = 'images/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'App', 
]
"""
from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'index.html'
    return render(request, template)