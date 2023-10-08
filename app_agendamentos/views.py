from django.shortcuts import render

def home(request):
    return render(request,'app/index.html')

def agendamentos(request):
    return render(request,'app/agendamentos.html')