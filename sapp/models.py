from django.db import models

# Create your models here.
class register(models.Model):
    name=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    cpassword=models.CharField(max_length=250)
def __str__(self):
    return self.name


class dept(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):

        return self.name


class course(models.Model):
    course_name=models.CharField(max_length=250,unique=True)

    department=models.ForeignKey(dept,on_delete=models.CASCADE)


    # def get_url(self):
    #     return reverse('shopapp:prodetail',args=[self.category.slug,self.slug])
    #
    #
    # class meta:
    #     ordering=('name',)
    #     verbose_name='product'
    #     verbose_name_pulural='products'
    def __str__(self):
        return self.course_name
class order(models.Model):
    # username=models.CharField(max_length=250,unique=True)
    dob=models.DateTimeField()
    # slug=models.SlugField(max_length=250,unique=True)
    nam=models.CharField(max_length=250,null=False, default='Some Default Value')
    # img=models.ImageField(upload_to='product',blank=True)
    # price=models.DecimalField(max_digits=10,decimal_places=2)
    age=models.IntegerField()
    gender=models.CharField(max_length=200)
    phone=models.IntegerField()
    email=models.EmailField()
    address=models.TextField(blank=True)
    department=models.ForeignKey(dept,on_delete=models.CASCADE,default=1)


    def __str__(self):
        return self.nam
