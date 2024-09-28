from django.shortcuts import render ,get_object_or_404
from django.contrib import messages
from .models import ContactForm , Artical
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.


def Home(request):
    if "query" in request.GET and request.GET['query'].strip():
        search_query = str(request.GET['query'])
        print(search_query)
        articals = Artical.objects.filter(Q(title__icontains=search_query) | Q(summary__icontains=search_query) | Q(content__icontains=search_query)).order_by('-created')
        
       
    else:
        articals = Artical.objects.all().order_by("-created")
    paginator = Paginator( articals,7)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"Page": page_obj }
    return render(request,"index.html", context=context)

def About(request):
    return render(request,"about.html")

def Contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email= request.POST.get("email")
        message = request.POST.get("message")
        try:
            ContactForm.objects.create(name=name,email=email,message=message)
            messages.success(request, "Message sent sucessfully! , I will contact you soon")
        except Exception as e:
            messages.success(request, "error sending message, please try again")
        
    return render(request,"contact.html")

def Post(request ,id):
    artical = get_object_or_404(Artical,pk=id)
    context = {"artical":artical}
    return render(request,'post.html',context=context)