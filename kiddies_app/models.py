from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Meta:
    db_table = "tbllogin"

class tblproduct(models.Model):
    product_id = models.CharField(max_length=80)
    product_name = models.CharField(max_length=90)
    category = models.CharField(max_length=90)
    unit_price = models.IntegerField()
    stock_qty = models.IntegerField()
    photo = models.CharField(max_length=90)
    size = models.IntegerField()
    colour = models.CharField(max_length=90)
    age_group = models.CharField(max_length=80)
    remark = models.CharField(max_length=80)

class Meta:
    db_table = "tblproduct"

class tblcustomer(models.Model):
    cust_id = models.CharField(max_length=80)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    address = models.CharField(max_length=100)
    pincode = models.CharField(max_length=90)
    city = models.CharField(max_length=90)
    state = models.CharField(max_length=90)
    country = models.CharField(max_length=90)
    phone = models.CharField(max_length=90)
    email = models.CharField(max_length=90)

class Meta:
    db_table = "tblcustomer"

class tbllogin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    category = models.CharField(max_length=80)

class tblreview(models.Model):
    review_id = models.CharField(max_length=90)
    product_id = models.CharField(max_length=90)
    user_id = models.CharField(max_length=90)
    review = models.CharField(max_length=200)
    review_date = models.CharField(max_length=90)

class Meta:
    db_table = "tblreview"

class tblcomplaint(models.Model):
    complaint_id = models.CharField(max_length=90)
    product_id = models.CharField(max_length=90)
    user_id = models.CharField(max_length=90)
    complaint = models.CharField(max_length=200)
    complaint_date = models.CharField(max_length=90)

class Meta:
    db_table = "tblcomplaint"

class tblcart(models.Model):
    cart_id = models.CharField(max_length=90)
    user_id = models.CharField(max_length=90)
    product_id = models.CharField(max_length=90)
    quantity = models.IntegerField()
    price = models.IntegerField()
    status = models.CharField(max_length=90)

class Meta:
    db_table = "tblcart"

class tblorder(models.Model):
    order_no = models.CharField(max_length=90)
    user_id = models.CharField(max_length=90)
    order_date = models.CharField(max_length=90)
    amount = models.CharField(max_length=90)
    payment_mode = models.CharField(max_length=90)
    order_status = models.CharField(max_length=90)

class Meta:
    db_table = "tblorder"

class tblpayment(models.Model):
    pay_id = models.CharField(max_length=90)
    order_no = models.CharField(max_length=90)
    card_no = models.CharField(max_length=90)
    cvv = models.CharField(max_length=90)
    mobile_no = models.CharField(max_length=90)
    amt = models.CharField(max_length=90)
    tran_date = models.CharField(max_length=90)
    time = models.CharField(max_length=90)

class Meta:
    db_table = "tblpayment"

class idgen(models.Model):
    order_id = models.CharField(max_length=90)

class Meta:
    db_table = "idgen"

class tblorder_details(models.Model):
    order_details_id = models.CharField(max_length=90)
    user_id =  models.CharField(max_length=90)
    product_id =  models.CharField(max_length=90)
    quantity =  models.CharField(max_length=90)
    date =  models.CharField(max_length=90)
    price =  models.CharField(max_length=90)
    status =  models.CharField(max_length=90)
    order_no =  models.CharField(max_length=90)

class Meta:
    db_table = "tblorder_details"