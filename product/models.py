from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_hit = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")

    def str(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")

    def str(self):
        return self.text[:30]