from django.contrib import admin

from retailer.models import Supplier, Product, Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'contact', 'link', 'debt', 'created_at', 'level')
    list_filter = ('contact__city',)  # Фильтр по городу
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        """ Admin action для очистки задолженности непосредственно из админ-панели для пользователя-админинстратора"""
        queryset.update(debt=0)

    clear_debt.short_description = 'Очистить задолженность'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'title', 'model', 'release_date')
