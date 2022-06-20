from tokenize import Name
from unicodedata import name
from django.shortcuts import redirect, render, get_object_or_404
from .models import Student
from .form import updateitem 

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
# from . models import Login


def main(request):
    return render(request, 'pages/main.html')
    # return HttpResponse("hello")


def home(request):
    return render(request, 'pages/home.html')


def AddStudent(request):
    n = request.POST.get('name')
    x = request.POST.get('Identity')
    e = request.POST.get('email')
    p = request.POST.get('Phone')
    gpa = request.POST.get('GPA')
    de = request.POST.get('Dept')
    l = request.POST.get('Level')
    g = request.POST.get('Gender')
    d = request.POST.get('Date')
    a = request.POST.get('act')
    if a == 'on':
        a = True
    else:
        a = False

    if request.method == 'POST':
        data = Student(Name=n, StudentID=x, Email=e, Phone=p, GPA=gpa,
                       Department=de, level=l, Gender=g, Date=d, activation=a)
        # print(data.activation)
        data.save()
    return render(request, 'pages/AddStudent.html')


def UpdateInfo(request):

    return render(request, 'pages/UpdateInfo.html', {'stu': Student.objects.all()})

# def update(request, id):
#   mymember = Student.objects.get(StudentID=id)
#   template = loader.get_template('pages/UpdateInfo.html')
#   context = {
#     'mymember': {'stu': Student.objects.all()},
#   }
#   return HttpResponse(template.render(context, request))

# def update(request,id):
#     obj = get_object_or_404(Student,StudentID=id)
#     if request.method == "POST":
#         form=updateitem(request.POST,instance=obj)
#         if form.is_valid():
#            form.save()
#            return HttpResponseRedirect("/")
#     else:
#         form = updateitem() 
#     return render(request,"UpdateInfo.html",{"form":form})

def update(request, id):
    obj=Student.objects.get(StudentID=id)
    form =updateitem(instance=obj)
    if request.method == 'POST':
        form =updateitem(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={
        'form':form,
    }
   
    return render(request,'pages/UpdateInfo.html', context)


def delete(request, id):
    member = Student.objects.get(StudentID=id)
    member.delete()
    return HttpResponseRedirect(reverse('UpdateInfo'))

# def search(request):
#     search=Student.objects.all()
#     title =None
#     if 'search_Name'in request.GET:
#         title =request.GET['search_name']
#         if title:
#             search =search.filter(Name__icontains=name)

def search(request):
    context = {
        "object": Student.StudentID,
        "random_page": Student.Name
    }
    context['object_list'] = Student.objects.filter(title__icontains=request.GET.get('search'))
    return render(request, "main/Search.html", context)
            

# def updaterecord(request, id):
#   first = request.POST['Uname']
# #   last = request.POST['last']
#   member = Student.objects.get(StudentID=id)
#   member.Name = first
# #   member.lastname = last
#   member.save()
#   return HttpResponseRedirect(reverse('UpdateInfo'))


# def update(request, id):
#     mymember = Student.objects.get(StudentID=id)

#     template = loader.get_template('UpdateInfo.html')
#     context = {
#         'mymember': mymember,
#     }
#     return HttpResponse(template.render(context, request))





def View(request):

    return render(request, 'pages/View.html', {'student': Student.objects.all()})


def Search(request):
    return render(request, 'pages/Search.html', {'actStu': Student.objects.all().filter(activation=True)})


def login(request):
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')

    #     if request.method == 'POST':
    #         dataa = Login(email=email, password=password)

    #         dataa.save()
    return render(request, 'pages/login.html')


# Create your views here.