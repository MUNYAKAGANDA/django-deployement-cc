from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models
ARTICLE_STATUSES=(
      ('s','submitted'),('r','rejected'),('a','approved')
)
class Article(models.Model):
    title= models.CharField(max_length=50)
    slug= models.SlugField(max_length=10)
    body= models.TextField(max_length=5000)
    thumb=models.FileField(blank=True,null=True)
    status= models.CharField(max_length=10,choices=ARTICLE_STATUSES)
    def ___str__(self):
        self.title

    def approve_status(self):
        return self.status.update(status='a')
    def reject_status(self):
        return self.status.update(status='r')
    def get_query_set(self):
        return reverse('app/article_detail.html',kwargs={'pk':self.pk})
class Trainer(models.Model):
    title= models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name= models.CharField(max_length=256)
    phone_number=models.PositiveIntegerField(null=True)
    state = models.BooleanField(default=False)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    bio= models.TextField(max_length=3000)
    twitter=models.CharField(max_length=30)
    instagram =models.CharField(max_length=30)
    facebook =models.CharField(max_length=30)
    def get_query_set(self):
        return reverse('app/Trainer_page.html',kwargs ={'pk':self.pk})


    def __str__(self):
        return self.name
TRAINING_LIST_TYPE=(('M','masonary' ),('C','cooking'),('T','technology'))
class Training(models.Model):
    name= models.CharField(max_length=256)
    thumb= models.ImageField(null=True)
    trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    description=models.CharField(max_length=7000,null=True)
    training_type= models.CharField(max_length=256,choices=TRAINING_LIST_TYPE)
    def get_query_set(self):
        return reverse ('app/training_detail.html',kwargs={'pk':self.pk})

SPONSORSHIP_TYPE=(('P','Project Fund'),('S','Student Fund'))
class Sponsorship(models.Model):
    first_name=   models.CharField(max_length=256)
    email= models.CharField(max_length=256,default='email @example.com',null=True)
    last_name= models.CharField(max_length=256)
    company_name= models.CharField(max_length=256,blank=True)
    type= models.CharField(max_length=256,choices=SPONSORSHIP_TYPE)
    twitter=models.CharField(max_length=30,blank=True,null=True)
    instagram =models.CharField(max_length=30,blank=True,null=True)
    facebook =models.CharField(max_length=30,blank=True,null=True)
    card_no=models.CharField(max_length=16,blank=True,null=True)
    key=models.PositiveIntegerField(null=True)
    def __str__(self):
        return self.first_name +" "+self.last_name
    def get_query_set(self):
        return reverse('app/sponsership_confirm.html')
class Activity(models.Model):
    name=models.CharField(max_length=23)
    slug=models.CharField(max_length=40)
    description=models.TextField(max_length=7000)
    date_happen=models.DateField()
    vid=models.FileField(null=True)
