from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DataPoint
from .forms import DataPointForm
from .serializers import DataPointSerializer


def index(request):
    # Get all DataPoint objects from the database and pass them to the template
    data_points = DataPoint.objects.all()
    return render(request, 'index.html',
                  {'data_points': data_points})


def add_data_point(request):
    if request.method == 'POST':
        form = DataPointForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponseBadRequest('Invalid parameters')
    else:
        form = DataPointForm()
    return render(request, 'add.html')


def delete_data_point(request, data_point_id):
    data_point = DataPoint.objects.get(id=data_point_id)
    data_point.delete()
    return redirect('index')


# API

@api_view(['GET', 'POST'])
def data_point_list(request):
    if request.method == 'GET':
        data_points = DataPoint.objects.all()
        serializer = DataPointSerializer(data_points, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DataPointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def data_point_detail(request, pk):
    try:
        data_point = DataPoint.objects.get(pk=pk)
    except DataPoint.DoesNotExist:
        return Response({'error': 'Record not found'},
                        status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        data_point.delete()
        return Response({'id': pk})

