from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter() 
router.register('viewsets', views.EmployeesViewset, basename='employees')
router.register('model_viewsets', views.EmployeesModelViewset)


urlpatterns = [
    path('get_students/', views.get_students, name='get_students'),
    path('get_student/<int:pk>/', views.get_student, name='get_student'),

    path('get_emps/', views.EmployeeView.as_view(), name='get_emps'),
    path('get_emp/<int:pk>/', views.EmployeeDetailsView.as_view(), name='get_emp'),

    path('students/', views.StudentsView.as_view(), name='students'),
    path('student/<int:pk>/', views.StudentDetailsView.as_view(), name='student'),

    path('employees_list/', views.EmployeesList.as_view(), name='employees_list'),
    path('employees_create/', views.EmployeesListCreate.as_view(), name='employees_create'),
    path('employees_update/<int:pk>', views.EmployeeRetrieveUpdate.as_view(), name='employees_update'),
    path('employees_delete/<int:pk>', views.EmployeeRetrieveDestroy.as_view(), name='employees_delete'),
    path('employees_retrieve/<int:pk>', views.EmployeesRetrieve.as_view(), name='employees_retrieve'),
    path('employees_crud/<int:pk>', views.EmployeeChange.as_view(), name='employees_crud'),

    path('', include(router.urls))
]