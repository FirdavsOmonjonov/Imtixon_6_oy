from django.db import models


#About web agentlik haqida birlamchi tushuncha olish uchun
class About(models.Model):
    image = models.FileField(upload_to='about/')
    body = models.TextField()

    def __str__(self):
        return self.body


#Service web agentlik mijozlarga qanday xizmatlarni ko'rsata olishi haqida 
class Service(models.Model):
    name = models.CharField(max_length=255)
    icon = models.FileField(upload_to='service/')
    
    def __str__(self):
        return self.name
    

#Blog bu yerda ssaytga tashrif byuruvchilar agentlikni ijodiy ishlari va mijozlarni agentlik haqidagi fikrlarini o'qishlari mumkin
class Blog(models.Model):
    name = models.CharField(max_length=255)
    body = models.TextField()
    image = models.FileField(upload_to='blog/')
    
    def __str__(self):
        return self.name


#Contact- xabar qoldirish:Dastur foydalanuvchisi xabar qoldirish uchun mo`ljallangan sahifa
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255)
    body = models.TextField()
    is_show = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
