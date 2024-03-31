import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from .models import DataPoint
from .forms import DataPointForm
from .serializers import DataPointSerializer


def index(request):
    data_points = DataPoint.objects.all()
    return render(request, 'index.html',
                  {'data_points': data_points})


def add_data(request):
    if request.method == 'POST':
        form = DataPointForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context = {'error_code': 400,
                       'error_message': 'Invalid data'}
            return render(request, 'error.html', context=context,
                          status=400)
    else:
        form = DataPointForm()
    return render(request, 'add.html', {'form': form})


def delete_data(request, data_point_id):
    if request.method == 'POST':
        data_point = get_object_or_404(DataPoint, pk=data_point_id)
        data_point.delete()
        return redirect('index')
    else:
        context = {'error_code': 404, 'error_message': 'Not found'}
        return render(request, 'error.html', context=context,
                      status=404)


# API
@api_view(['GET', 'POST'])
def manage_data_via_api(request):
    if request.method == 'GET':
        data_points = DataPoint.objects.all()
        serializer = DataPointSerializer(data_points, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = DataPointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'pk': serializer.data['id']})
        return JsonResponse({'error': 'Invalid data'},
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_data_via_api(request, pk):
    try:
        data_point = DataPoint.objects.get(pk=pk)
    except DataPoint.DoesNotExist:
        return JsonResponse({'error': 'Record not found'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        data_point.delete()
        return JsonResponse({'pk': pk})
