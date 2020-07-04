from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db import models

class AccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,email,cnic,phone,address,city,country,password=None,is_admin=True,is_staff=False,is_superuser=False,is_client=False):
        if not email:
            raise ValueError("Users must have an email address!")
        if not cnic:
            raise ValueError("Users must have cnic")
        if not phone:
            raise ValueError("Users must have Phone Number")
        
        user = self.model(
            first_name = first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            cnic=cnic,
            phone=phone,
            address=address,
            city=city,
            country=country,
            is_admin = is_admin,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_client=is_client
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,first_name,last_name,email,cnic,phone,address,city,country,password=None,is_superuser=True):
        return self.create_user(first_name=first_name,last_name=last_name,email=email,cnic=cnic,phone=phone,address=address,city=city,country=country,password=password,is_superuser=True,is_admin=True,is_staff=True)

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50,null=False,verbose_name="firstName")
    last_name = models.CharField(max_length=50,verbose_name="lastName")
    email   =   models.EmailField(verbose_name="email",max_length=60,unique=True)
    #username=   models.CharField(max_length=30,unique=True)
    cnic = models.CharField(max_length=13,verbose_name="cnic",unique=True)
    phone = models.CharField(max_length=11,verbose_name="phone")
    address = models.CharField(max_length=150, verbose_name="address")
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50,default="Pakistan")
    date_joined = models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    is_admin    = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'cnic'
    REQUIRED_FIELDS = ['first_name','last_name','email','phone','address','city','country']

    objects = AccountManager()

    def __str__(self):
        return self.first_name +" "+ self.last_name

    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True

