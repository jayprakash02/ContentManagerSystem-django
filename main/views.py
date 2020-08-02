from django.shortcuts import render
from .models import Dashboard , Table , Piechart , Barchart
# Create your views here.
def index(request):
    dashboard = Dashboard.objects.all()
    piechart = Piechart.objects.all()
    barchart = Barchart.objects.all()
    tables = Table.objects.order_by('date')
    
    plabel = []
    pdata = []
    for pie in piechart:
        plabel.append(pie.label)
        pdata.append(pie.data)
    
    bdata = []
    for bar in barchart:
        bdata.append(bar.data)

    return render(request,'index.html',{'dashboard':dashboard,'tables':tables, 'plabel':plabel, 'pdata':pdata, 'bdata':bdata })