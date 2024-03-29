from django.contrib import admin
from .models import CurrencyAmount

@admin.register(CurrencyAmount)
class CurrencyAmountAdmin(admin.ModelAdmin):
    list_display = ('currency', 'amount')

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == "currency":
            kwargs["choices"] = [(c.currency, f"{c.currency} ({c.amount})") for c in self.model.objects.all()]
        return super().formfield_for_choice_field(db_field, request, **kwargs)