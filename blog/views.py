from django.shortcuts import render, redirect
from .models import Member
from django.db.models import Q

# Create your views here.

def index(request):
    members = Member.objects.all().order_by('lastname')
    return render(request, 'blog/index.html', {'members': members})

def create(request):
    member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'])
    member.save()
    return redirect('/')

def search(request):

    members = Member.objects.filter(Q(firstname=request.GET.get('search')) | Q(lastname=request.GET.get('search')))
    return render(request, 'blog/index.html', {'members': members})