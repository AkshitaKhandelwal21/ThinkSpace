from http.client import HTTPException
from django.shortcuts import render

from DRF.models import Employee, Student
from DRF.serializers import EmployeeSerializer, StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.mixins import *
from rest_framework import viewsets

# Create your views here

#*********************************** Function Based Views ********************************

@api_view(['GET', 'POST'])
def get_students(request):
    if request.method=='GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def get_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Exception as e:
        return HTTPException(e)
    
    if request.method=='GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    if request.method=='PUT':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    if request.method=='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        


#*********************************** Class Based Views ********************************

class EmployeeView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class EmployeeDetailsView(APIView):
    def get_object(self, pk):
        try:
            employee = Employee.objects.get(pk=pk)
            return employee
        except:
            raise HTTPException
    
    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    
    def put(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#*********************************** GenericAPIView Using Mixin ********************************

class StudentsView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    

class StudentDetailsView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
    


#*********************************** API Views DRF ********************************

class EmployeesList(ListAPIView, CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeesListCreate(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeesRetrieve(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'

class EmployeeRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'

class EmployeeRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'

class EmployeeChange(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'



#*********************************** ViewSets and ModelViewSets ********************************

class EmployeesViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def retrieve(self, request, pk=None):
        employee = get_object_or_404(Employee, pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        employee = get_object_or_404(Employee, pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk=None):
        employee = get_object_or_404(Employee, pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
    

class EmployeesModelViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all() 
    serializer_class = EmployeeSerializer