from django.shortcuts import render
from .models import Employee
from django.db.models import Q

# Create your views here.


def employee_search(request, field, lookup, search_string):
    if field == "empname":
        if lookup == "startswith":
            employees = Employee.objects.filter(Q(fname__startswith=search_string) | Q(lname__startswith=search_string))
        elif lookup == "contains":
            employees = Employee.objects.filter(Q(fname__icontains=search_string) | Q(lname__icontains=search_string))
    elif field == "empage" and lookup == "lte":
        employees = Employee.objects.filter(age__lte=search_string)
    else:
        employees = Employee.objects.none()

    return render(request, 'empapp/employee_list.html', {'employees': employees})

def default_view(request):
    return render(request, 'empapp/default.html') 