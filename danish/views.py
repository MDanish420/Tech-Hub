from django.shortcuts import render
from django.http import HttpResponse
from danish.models import message_table , registration_table

def web_view(request):
    return render(request , 'home.html')

def mess_view(request):
    if request.method == 'POST':
        n = request.POST['name']
        e = request.POST['email']
        s = request.POST['subject']
        p = request.POST['phone_n']
        m = request.POST['message']
        print(n,e,s,p,m)
        data = message_table.objects.create(name=n , email = e , subject = s , phone_n= p , message = m )
        data.save()
        return render(request , "home.html")
    
def  reg_view(request):
        if request.method == 'POST':
            n = request.POST['name']
            fn = request.POST['fname']
            dob = request.POST['dob']
            em = request.POST['email']
            add = request.POST['address']
            pn = request.POST['phone_n']
            ex = request.POST['exp_skills']
            inf = request.POST['information']
            data = registration_table.objects.create(name = n , fname=fn , dob=dob , email=em , address = add , phone_n = pn , exp_skills = ex , information = inf)
            data.save()

        return render(request , "home.html")

# Create your views here.
