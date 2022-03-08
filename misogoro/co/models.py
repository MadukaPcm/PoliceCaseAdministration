from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User,Group
from django.utils.translation import gettext as _

# Create your models here.
class Role(Group):
    class Meta:
        proxy = True
        app_label = 'auth'
        verbose_name = _('Role')

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
    phone = models.CharField(max_length=15,null=False,blank=False,unique=True)
    address = models.CharField(max_length=20,null=False,blank=False)
    occupation = models.CharField(max_length=20,null=False,blank=False)
    tribe = models.CharField(max_length=20,null=False,blank=False)
    age = models.IntegerField(null=False,blank=False)
    empNo = models.CharField(max_length=20,null=False,blank=False)

    def __str__(self):
        return self.phone

class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,null=True)
    image = models.FileField(upload_to='uploads/profile', validators=[FileExtensionValidator(allowed_extensions=['png','jpg','jpeg'])])
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.User.username

class Case(models.Model):
    case_no = models.IntegerField(null=False,blank=False,unique=True)
    reporter = models.CharField(max_length=30,blank=False,null=False)
    case_site = models.CharField(max_length=50,blank=False,null=False)
    phoneNo = models.CharField(max_length=15,null=True,blank=False)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.case_no)

class CaseAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
    case = models.OneToOneField(Case,on_delete=models.CASCADE,blank=True,null=True)
    date_assigned = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.case)

class CaseStatus(models.Model):
    caseassignment = models.ForeignKey(CaseAssignment,on_delete=models.CASCADE,blank=True,null=True)
    datetime = models.DateField(auto_now_add=True)
    contact = models.CharField(max_length=15,blank=False,null=False)
    description = models.TextField()

    def __str__(self):
        return self.caseassignment.user.username +" || " +str(self.datetime)

