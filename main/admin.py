from django.contrib import admin

from .models import Dashboard,Table,Piechart,Barchart

admin.site.register(Dashboard)
admin.site.register(Table)
admin.site.register(Piechart)
admin.site.register(Barchart)