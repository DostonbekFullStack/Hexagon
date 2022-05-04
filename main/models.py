from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Email(models.Model):
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.email

class HeaderTitle(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class HeaderParagraph(models.Model):
    para = models.CharField(max_length=255)

class Logo(models.Model):
    logo = models.ImageField(upload_to='logo')

class YoutubeLink(models.Model):
    link = models.CharField(max_length=300)

class BusinessSucces(models.Model):
    title = models.CharField(max_length=255)
    paragraph = models.CharField(max_length=400)

class BusinessCard(models.Model):
    logo = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    paragraph =  models.CharField(max_length=255)

class Reservation(models.Model):
    image = models.ImageField(upload_to='reservation')
    title = models.CharField(max_length=255)
    paragraph =  models.CharField(max_length=255)
    firstpara = models.CharField(max_length=255)
    secondpara = models.CharField(max_length=255)
    thirdpara = models.CharField(max_length=255)
    fourthpara = models.CharField(max_length=255)

class Reports(models.Model):
    image = models.ImageField(upload_to='reservation')
    title = models.CharField(max_length=255)
    paragraph =  models.CharField(max_length=255)
    firstpara = models.CharField(max_length=255)
    secondpara = models.CharField(max_length=255)
    thirdpara = models.CharField(max_length=255)

class SocialLink(models.Model):
    title = models.CharField(max_length=255)
    #
    firstlogo = models.CharField(max_length=255)
    firstpara = models.CharField(max_length=255)
    firstlink = models.CharField(max_length=255)
    #
    secondlogo = models.CharField(max_length=255)
    secondpara = models.CharField(max_length=255)
    secondlink = models.CharField(max_length=255)
    #
    thirdlogo = models.CharField(max_length=255)
    thirdpara = models.CharField(max_length=255)
    thirdlink = models.CharField(max_length=255)

class Testimonials(models.Model):
    title = models.CharField(max_length=255)
    paragraph =  models.CharField(max_length=255)

class TestimonialsCard(models.Model):
    image = models.ImageField(upload_to='testimonialcards')
    title = models.CharField(max_length=255)
    neartitle = models.CharField(max_length=100)
    paragraph =  models.CharField(max_length=255)

class Pricing(models.Model):
    title = models.CharField(max_length=255)
    paragraph =  models.CharField(max_length=255)

class Count(models.Model):
    firstnumber = models.IntegerField()
    firstpara = models.CharField(max_length=255)
    #
    secondnumber = models.IntegerField()
    secondpara = models.CharField(max_length=255)
    #
    thirdnumber = models.IntegerField()
    thirdpara = models.CharField(max_length=255)
    #
    fourthnumber = models.IntegerField()
    fourthpara = models.CharField(max_length=255)
    #

class Blog(models.Model):
    title = models.CharField(max_length=255)
    paragraph =  models.CharField(max_length=255)

#

class BlogCards(models.Model):
    cardimg = models.ImageField(upload_to='blogcards')
    cardtitle = models.CharField(max_length=255)
    cardpara1 = models.CharField(max_length=255)
    cardpara2 = models.CharField(max_length=255)


class UnderSection(models.Model):
    underlogopara = models.CharField(max_length=255)
    #
    firstcolumntitle = models.CharField(max_length=255)
    firstfirpara = models.CharField(max_length=255)
    firstsecpara = models.CharField(max_length=255)
    firstthipara = models.CharField(max_length=255)
    firstfoupara = models.CharField(max_length=255)
    #
    secondcolumntitle = models.CharField(max_length=255)
    secondfirpara = models.CharField(max_length=255)
    secondsecpara = models.CharField(max_length=255)
    secondthipara = models.CharField(max_length=255)
    secondfoupara = models.CharField(max_length=255)
    #
    contactcolumntitle = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    #
    firstlogo = models.CharField(max_length=255)
    secondlogo = models.CharField(max_length=255)
    thirdlogo = models.CharField(max_length=255)
    fourthlogo = models.CharField(max_length=255)
    fifthlogo = models.CharField(max_length=255)

class Reserved(models.Model):
    date = models.DateField()

# Plan

class Plan(models.Model):
    basicprice = models.FloatField()
    advancedprice = models.FloatField()
    expertprice = models.FloatField()

# Skidka

class Skidka(models.Model):
    basicskidka = models.FloatField()
    advancedskidka = models.FloatField()
    expertskidka = models.FloatField()

class PriceForBasic(models.Model):
    basic = models.ForeignKey(Plan, on_delete=models.CASCADE)
    #
    skidki = models.ForeignKey(Skidka, on_delete=models.CASCADE)
    def basicpriced(self):
        return self.basic.basicprice * (self.skidki.basicskidka / 100)

class PriceForAdvanced(models.Model):
    advanced = models.ForeignKey(Plan, on_delete=models.CASCADE)
    #
    skidki = models.ForeignKey(Skidka, on_delete=models.CASCADE)
    def advancepriced(self):
        return self.advanced.advancedprice * (self.skidki.advancedskidka / 100)

class PriceForExpert(models.Model):
    expert = models.ForeignKey(Plan, on_delete=models.CASCADE)
    #
    skidki = models.ForeignKey(Skidka, on_delete=models.CASCADE)
    def expertpriced(self):
        return self.expert.expertprice * (self.skidki.expertskidka / 100)

# Second Page Users

# Users

class Users(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=500)
    def __str__(self):
        return self.name

# Who am I

class WhoI(models.Model):
    name = models.CharField(max_length=255)
    mycountry = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    dev = models.CharField(max_length=255)
    firstskill = models.CharField(max_length=255)
    secondskill = models.CharField(max_length=255)
    thirdskill = models.CharField(max_length=255)
    fourthskill = models.CharField(max_length=255)

# Second Page Count

class SecondPageCount(models.Model):
    firstnumber = models.IntegerField()
    secondnumber = models.IntegerField()
    thirdnumber = models.IntegerField()
    fourthnumber = models.IntegerField()

# Skills

class MySkills(models.Model):
    firsttitle = models.CharField(max_length=255)
    firstpercent = models.IntegerField()
    #
    secondtitle = models.CharField(max_length=255)
    secondpercent = models.IntegerField()
    #
    thirdtitle = models.CharField(max_length=255)
    thirdpercent = models.IntegerField()
    #
    fourthtitle = models.CharField(max_length=255)
    fourthpercent = models.IntegerField()
    #
    fivetitle = models.CharField(max_length=255)
    fivepercent = models.IntegerField()
    #
    sixtitle = models.CharField(max_length=255)
    sixpercent = models.IntegerField()

# Experience

# Contact

# Sign Up
class SignUp(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
