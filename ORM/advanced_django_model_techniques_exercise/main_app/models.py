from decimal import Decimal

from django.core.validators import MinValueValidator, RegexValidator, MinLengthValidator
from django.db import models

from main_app.mixins import RechargeEnergyMixin


# Create your models here.


class BaseMedia(models.Model):
    class Meta:
        abstract = True
        ordering = ["-created_at", "title"]

    title = models.CharField(
        max_length=100,
    )

    description = models.TextField()

    genre = models.CharField(
        max_length=50,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class Book(BaseMedia):
    class Meta(BaseMedia.Meta):
        verbose_name = "Model Book"
        verbose_name_plural = "Models of type - Book"

    author = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(5, "Author must be at least 5 characters long"),
        ]
    )

    isbn = models.CharField(
        max_length=20,
        unique=True,
        validators=[
            MinLengthValidator(6, "ISBN must be at least 6 characters long"),
        ]
    )


class Movie(BaseMedia):
    class Meta(BaseMedia.Meta):
        verbose_name = "Model Movie"
        verbose_name_plural = "Models of type - Movie"

    director = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(8, "Director must be at least 8 characters long"),
        ]
    )


class Music(BaseMedia):
    class Meta(BaseMedia.Meta):
        verbose_name = "Model Music"
        verbose_name_plural = "Models of type - Music"

    artist = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(9, "Artist must be at least 9 characters long"),
        ]
    )


class Product(models.Model):
    name = models.CharField(
        max_length=100,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    def calculate_tax(self) -> Decimal:
        return self.price * Decimal(0.08)

    @staticmethod
    def calculate_shipping_cost(weight: Decimal) -> Decimal:
        return weight * Decimal(2.00)

    def format_product_name(self) -> str:
        return f"Product: {self.name}"


class DiscountedProduct(Product):
    class Meta:
        proxy = True

    def calculate_price_without_discount(self) -> Decimal:
        return self.price * Decimal(1.20)

    def calculate_tax(self) -> Decimal:
        return self.price * Decimal(0.05)

    @staticmethod
    def calculate_shipping_cost(weight: Decimal) -> Decimal:
        return weight * Decimal(1.50)

    def format_product_name(self) -> str:
        return f"Discounted Product: {self.name}"


class Hero(models.Model, RechargeEnergyMixin):
    name = models.CharField(
        max_length=100,
    )

    hero_title = models.CharField(
        max_length=100,
    )

    energy = models.PositiveIntegerField()


class SpiderHero(Hero):
    class Meta:
        proxy = True

    def swing_from_buildings(self):
        if self.energy - 80 >= 0:
            self.energy -= 80 if self.energy - 80 > 0 else 79
            self.save()
            return f"{self.name} as Spider Hero swings from buildings using web shooters"

        return f"{self.name} as Spider Hero is out of web shooter fluid"


class FlashHero(Hero):
    class Meta:
        proxy = True

    def run_at_super_speed(self):
        if self.energy - 65 >= 0:
            self.energy -= 65 if self.energy - 65 > 0 else 64
            self.save()
            return f"{self.name} as Flash Hero runs at lightning speed, saving the day"

        return f"{self.name} as Flash Hero needs to recharge the speed force"



