from django.urls import path
from .views import *

urlpatterns = [
    path('', Index, name='index'),
    path('email/', EmailSend, name='emailsent'),
    path('secondpage/', SecondPage, name='secondpage'),
    path('message/', MessageView, name='message'),
    path('signup/', SignUpView, name='sign-up'),
    path('contact/', ContactView, name='contact'),
    path('about/', AboutView, name='about'),
    path('faq/', FaqView, name='faq'),
    path('blog/', BlogView, name='blog'),
    path('blogsingleview/<int:pk>/', BlogSingleView, name='blogsingleview'),
]