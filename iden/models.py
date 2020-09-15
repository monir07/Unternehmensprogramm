from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

# This is Final Iden Model here -----------------------------------------------------------------------
class attention(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class sender_shopName(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class receiver_shopName(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class new_iden(models.Model):
    ref = models.CharField(max_length=100, blank=True, null=True)
    iden_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    sender_shop = models.ManyToManyField(sender_shopName)
    receiver_shop = models.ManyToManyField(receiver_shopName)
    subject = models.CharField(max_length=300, blank=True, null=True)
    job_no = models.CharField(max_length=100,blank=True,null=True)
    iden_body = RichTextField(blank=True,null=True)
    attention = models.ManyToManyField(attention,blank=True,null=True)
    sender_name = models.CharField(max_length=100, blank=True, null=True)
    sender_designation = models.CharField(max_length=100, blank=True, null=True)
    sign = models.ImageField(upload_to='images/',blank=True, null=True)
    viewed = models.BooleanField(default=False)
    attachment = models.FileField(upload_to='documents/',blank=True, null=True)

    def __str__(self):
        return self.sender_name

    def get_senderShop(self):
        return "\n".join([p.name for p in self.sender_shop.all()])

    def get_receiverShop(self):
        list1 = []
        for p in self.receiver_shop.all():
            list1.append(p)
        return list1

        #return "\n".join([p.name for p in self.receiver_shop.all()])

    def get_attention(self):
        list1 = []
        for p in self.attention.all():
            list1.append(p)
        return list1

        #return "\n".join([p.name for p in self.attention.all()])

# END OF This is Final Iden Model here -----------------------------

# Start for Preview model

class Iden_preview(models.Model):
    ref = models.CharField(max_length=100, blank=True, null=True)
    iden_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    sender_shop = models.ManyToManyField(sender_shopName)
    receiver_shop = models.ManyToManyField(receiver_shopName)
    subject = models.CharField(max_length=300,blank=True, null=True)
    job_no = models.CharField(max_length=100,blank=True,null=True)
    iden_body = RichTextField(blank=True,null=True)
    attention = models.ManyToManyField(attention,blank=True,null=True)
    sender_name = models.CharField(max_length=100, blank=True, null=True)
    sender_designation = models.CharField(max_length=100,blank=True, null=True)
    sign = models.ImageField(upload_to='prevImg/',blank=True, null=True)
    viewed = models.BooleanField(default=False)
    attachment = models.FileField(upload_to='prevDoc/',blank=True, null=True)

    def __str__(self):
        return self.sender_name

    def get_senderShop(self):
        return "\n".join([p.name for p in self.sender_shop.all()])

    def get_receiverShop(self):
        list1 = []
        for p in self.receiver_shop.all():
            list1.append(p)
        return list1

        #return "\n".join([p.name for p in self.receiver_shop.all()])

    def get_attention(self):
        list1 = []
        for p in self.attention.all():
            list1.append(p)
        return list1