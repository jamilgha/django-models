from django.db import models

# Class stores Dec...
class stores (models.Model):
    store_id=models.IntegerField(primary_key=True)
    store_name=models.CharField(max_length=256,null=False)
    phone =models.CharField(max_length=256)
    email =models.CharField(max_length=256),
    street =models.CharField(max_length=256)
    city=models. CharField(max_length=256)
    state=models. CharField(max_length=256)
    zip_code=models.CharField(max_length=256)
# Class staffs 
class staffs (models.Model):
    store_id_fk = models.ForeignKey(stores, on_delete=models.CASCADE,)
    staff_id =models.IntegerField(primary_key=True)
    first_name =models.CharField(max_length=256,null=False)
    last_name  =models.CharField(max_length=256,null=False)
    email  =models.CharField(max_length=256,null=False ,unique=False),
    phone  =models.CharField(max_length=100,null=False)
    active =models. IntegerField(max_length=256,null=False)
    store_id =models. IntegerField(max_length=256,null=False)
    manager_id =models.IntegerField(max_length=256)
# Class products categories
class categories (models.Model):
    category_id=models.IntegerField(primary_key=True)
    category_name=models.CharField(max_length=256,null=False)
# Class products brands
class brands (models.Model):
    brand_id=models.IntegerField(primary_key=True)
    brand_name=models.CharField(max_length=256,null=False)
    
# Class products 
class products (models.Model):
    brand_id_fk = models.ForeignKey(stores, on_delete=models.CASCADE,)
    category_id_fk = models.ForeignKey(stores, on_delete=models.CASCADE,)
    brand_id_fk = models.ForeignKey(stores, on_delete=models.CASCADE,)
    product_id=models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=256,null=False)
    brand_id =models.IntegerField(max_length=256,null=False)
    category_id =models.IntegerField(max_length=256,null=False),
    model_year =models.CharField(max_length=4,null=False)
    list_price=models.DecimalField(max_digits=10, decimal_places=2 ,null=False)
# class Store customers 
class customers (models.Model):
    customer_id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=256,null=False)
    last_name =models.CharField(max_length=256,null=False)
    phone =models.CharField(max_length=256,null=False)
    email =models.CharField(max_length=256,null=False)
    street=models.CharField(max_length=256,null=False)
    city =models.CharField(max_length=256,null=False)
    state  =models.CharField(max_length=256,null=False)
    zip_code  =models.IntegerField(max_length=15)


# class orderitems 
class orderitems (models.Model):
    order_id =models.IntegerField(null=False)
    item_id =models.IntegerField(null=False)
    product_id =models.IntegerField(null=False)
    quantity =models.IntegerField(null=False)
    list_price =models.DecimalField(max_digits=10, decimal_places=2 ,null=False)
    discount =models.DecimalField(max_digits=10, decimal_places=2 ,null=False)
# class Store Stocks 
class stocks (models.Model):
    store_id  =models.IntegerField(null=False)
    product_id =models.IntegerField(null=False) 
    quantity =models.IntegerField(null=False)

class order (models.Model):
    store_id_fk = models.ForeignKey(stores, on_delete=models.CASCADE,)
    staff_id_fk = models.ForeignKey(staffs, on_delete=models.CASCADE,)
    brand_id_fk = models.ForeignKey(brands, on_delete=models.CASCADE,)
    order_id = models.ForeignKey(orderitems,on_delete=models.CASCADE,)
    order_id =models.IntegerField(primary_key=True)
    customer_id=models.IntegerField(null=False)
    order_status=models.IntegerField(max_length=1,null=False) 
    # Order status: 1 = Pending; 2 = Processing; 3 = Rejected; 4 = Completed
    order_date= models.DateTimeField(null=False)
    required_date=models.DateTimeField(null=False) 
    shipped_date=models.DateTimeField() 
    store_id=models.IntegerField(null=False)
    staff_id=models.IntegerField(null=False)
