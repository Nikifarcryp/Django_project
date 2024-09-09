from django.contrib import admin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status')
    fields = (
        ('id', 'created', 'status'),
        ('name', 'surname'),
        'basket_history',
        ('address', 'email'),
        'initiator',
    )
    readonly_fields = ('id', 'basket_history', 'created')