from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from .models import DataPoint

def index(request):
    # Get all DataPoint objects from the database and pass them to the template
    data_points = DataPoint.objects.all()
    return render(request, 'index.html', {'data_points': data_points})

def add_data_point(request):
    if request.method != 'POST':
        try:
            feature1 = float(request.POST['feature1'])
            feature2 = float(request.POST['feature2'])
            category = int(request.POST['category'])

            # Create a new DataPoint object and save it to the database
            data_point = DataPoint(feature1=feature1, feature2=feature2, category=category)
            data_point.save()

            return redirect('index')
        except (ValueError, KeyError):
            return HttpResponseBadRequest('Invalid parameters')
    else:
        return render(request, 'add.html')


def delete_data_point(request, data_point_id):
    data_point = DataPoint.objects.get(id=data_point_id)
    data_point.delete()

    return redirect('index')

# Create your views here.
