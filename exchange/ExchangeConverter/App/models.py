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

"""
from django.db import models

class CurrencyAmount(models.Model):
    currency = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.currency} ({self.amount})"
