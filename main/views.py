from turtle import title
from django.http import request
from django.shortcuts import redirect, render
from django.template import context
from .models import *
from .form import SignUpForm
# Create your views here.
def Index(request):
    logo = Logo.objects.last()
    title = HeaderTitle.objects.last()
    para =  HeaderParagraph.objects.last()
    link = YoutubeLink.objects.last()
    business = BusinessSucces.objects.last()
    businesscard = BusinessCard.objects.all().order_by('-id')[0:4]
    reservation = Reservation.objects.last()
    reports = Reports.objects.last()
    sociallink = SocialLink.objects.last()
    testimonials = Testimonials.objects.last()
    pricing = Pricing.objects.last()
    count = Count.objects.last()
    blog = Blog.objects.last()
    undersection = UnderSection.objects.last()
    reserved = Reserved.objects.last()
    priceforbasic =  PriceForBasic.objects.last()
    priceforadvanced =  PriceForAdvanced.objects.last()
    priceforexpert =  PriceForExpert.objects.last()
    skidka = Skidka.objects.last()
    testimonialscard = TestimonialsCard.objects.all().order_by('-id')[0:6]
    blogcards = BlogCards.objects.all().order_by('-id')[0:3]
    context = {
        'logo':logo,
        'title':title,
        'para':para,
        'link':link,
        'business':business,
        'reservation':reservation,
        'reports':reports,
        'sociallink':sociallink,
        'testimonials':testimonials,
        'pricing':pricing,
        'count':count,
        'blog':blog,
        'undersection':undersection,
        'reserved':reserved,
        'priceforbasic':priceforbasic,
        'priceforadvanced':priceforadvanced,
        'priceforexpert':priceforexpert,
        'skidka': skidka,
        'businesscard': businesscard,
        'testimonialscard': testimonialscard,
        'blogcards': blogcards,
    }
    return render(request, 'index.html', context)

def SecondPage(request):  
    whoi = WhoI.objects.last()
    secondpagecount = SecondPageCount.objects.last()
    myskills = MySkills.objects.last()
    context = {
        'whoi':whoi,
        'secondpagecount':secondpagecount,
        'myskills':myskills,
    }
    return render(request, '../templates/secondpage/templates/mypage.html', context)

def MessageView(request):
    if request.method == "POST":
        data = request.POST
        Users.objects.create(
            name = data.get('name'),
            phone = data.get('phone'),
            subject = data.get('subject'),
            message = data.get('message')
        )
    return redirect('secondpage')

def EmailSend(request):
    if request.method == "POST":
        data = request.POST
        Email.objects.create(
            email = data.get('email')
        )
    return redirect('index')

def SignUpView(request):
    signup = SignUp.objects.all()
    context = {
        "signupform": SignUpForm
    }
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    
    return render(request, 'signup.html', context)


def ContactView(request):
    logo = Logo.objects.last()
    context = {
        'logo':logo,
    }
    return render(request, 'contact.html', context)

def AboutView(request):
    logo = Logo.objects.last()
    context = {
        'logo':logo,
    }
    return render(request, 'about.html', context)

def FaqView(request):
    logo = Logo.objects.last()
    context = {
        'logo':logo,
    }
    return render(request, 'faq.html', context)

def BlogView(request):
    logo = Logo.objects.last()
    context = {
        'logo':logo,
    }
    return render(request, 'blog.html', context)

def BlogSingleView(request, pk):
    blogcards = BlogCards.objects.get(id=pk)
    logo = Logo.objects.last()
    context = {
        'logo':logo,
        'blogcards':blogcards,
    }
    return render(request, 'blog-single.html', context)
