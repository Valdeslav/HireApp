from django.db import models


class CartDb(models.Model):
    user_id = models.IntegerField(db_index=True)
    product_id = models.IntegerField()


