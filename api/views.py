from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.permissions import *
from .permissions import *

from app.models import *
from .serializers import *

@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def user(request):

    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True, context={'request': request})
        return Response(serializer.data, status=HTTP_200_OK)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)     

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def user_detail(request, pk):

    user = User.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)   

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    
#CATEGORY
@api_view(['GET', 'POST'])
@permission_classes([CategoryPermission])
def category(request):

    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True, context={'request': request})
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([CategoryDetailPermission])
def category_detail(request, pk):

    category = Category.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=HTTP_202_ACCEPTED) 
    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=HTTP_204_NO_CONTENT)

#POST
@api_view(['GET', 'POST'])
@permission_classes([ProductPermission])
def product(request):

    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True, context={'request': request})
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([ProductDetailPermission])
def product_detail(request, pk):

    product = Product.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)  
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=HTTP_204_NO_CONTENT)