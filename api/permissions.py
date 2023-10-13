from rest_framework.permissions import BasePermission

#USER PERMISSION
class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_staff
        elif request.method == 'POST':
            return request.user.is_staff

class UserDetailPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_authenticated
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_authenticated

#CATEGORY PERMISSION
class CategoryPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method == 'POST':
            return request.user.is_authenticated

class CategoryDetailPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_authenticated
#PRODUCT PERMISSION
class ProductPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method == 'POST':
            return request.user.is_staff

class ProductDetailPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True 
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_staff

