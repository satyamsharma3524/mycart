from django.db import models
from django.db.models.fields import AutoField

# Create your models here.


class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_category = models.CharField(max_length=50, default="")
    product_subcategory = models.CharField(max_length=50, default="")
    product_price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=300)
    publish_date = models.DateField()
    product_image = models.ImageField(upload_to="shop/images", default="")
    

    def __str__(self):
        return self.product_name
        