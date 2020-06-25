from django.shortcuts import render
from .models import Dashboard , Table , Piechart 
# Create your views here.
def index(request):
    dashboard = Dashboard.objects.all()
    piechart = Piechart.objects.all()
    tables = Table.objects.order_by('date')
    return render(request,'index.html',{'dashboard':dashboard,'tables':tables, 'piechart':piechart})