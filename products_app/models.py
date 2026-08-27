from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField('Название', max_length=20, unique=True)
    image = models.ImageField('Изображение', upload_to='products/default_images', null=True)

    def __str__(self):
        return f'{self.name}'


class Brand(models.Model):
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    name = models.CharField('Название', max_length=20, unique=True)

    def __str__(self):
        return f'{self.name}'


class Products(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    class Condition(models.TextChoices):
        USED = 'Б-У', 'Б/У'
        NEW = 'Новое', 'Новое'

    name = models.CharField(verbose_name='Название', max_length=22)
    description = models.TextField(verbose_name='Короткое описание', max_length=120)
    image = models.ImageField(verbose_name='Изображение', upload_to='products/images', null=True, blank=True)
    full_description = models.TextField(verbose_name='Полное описание')
    price = models.IntegerField(verbose_name='Цена') 
    author = models.CharField(verbose_name='Автор')
    category = models.ForeignKey('products_app.Category', on_delete=models.PROTECT, verbose_name='Категория',
                                 related_name='products', null=True)
    brand = models.ForeignKey('products_app.Brand', on_delete=models.PROTECT, verbose_name='Бренд',
                              related_name='products', null=True)
    condition = models.CharField(
        verbose_name='Состояние',
        choices=Condition.choices,
        default=Condition.NEW,
    )
    model = models.CharField(verbose_name='Модель', max_length=30)
    date = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True)
    ubdate_date = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)

    def __str__(self):
        return f'{self.name}'
