from django.db import models
from zakaz.settings import AUTH_USER_MODEL

User = AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class SubCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    slug = models.SlugField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'


class Image(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    image = models.ImageField(upload_to='order_images', verbose_name='изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'


class Order(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    user = models.ForeignKey(User, on_delete=models.PROTECT,
                             verbose_name='пользователь')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 verbose_name='категория', null=True,
                                 blank=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL,
                                     verbose_name='подкатегория', null=True,
                                     blank=True)
    description = models.TextField(verbose_name='описание')
    city = models.CharField(max_length=50, verbose_name='город')
    image = models.ManyToManyField(Image, verbose_name='изображение', blank=True)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='создан')
    updated_on = models.DateTimeField(auto_now=True, verbose_name='обновлен')
    publish = models.BooleanField(default=False, verbose_name='опубликовано')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='заказ',
                              related_name='comments')

    def __str__(self):
        return f'{self.user} - {self.order}'

    class Meta:
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'
