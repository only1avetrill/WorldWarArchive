from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=100, verbose_name='Название')
    def __str__(self):
        return self.name

class Country(models.Model):
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    name = models.CharField(max_length=100, verbose_name='Название')
    def __str__(self):
        return self.name

class Document(models.Model):
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    title = models.CharField(max_length=1000, verbose_name='Название')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', blank=True)
    link = models.CharField(max_length=1000, verbose_name='Ссылка')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    country = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name='Страна')
    author = models.CharField(max_length=1000, verbose_name='Автор/издатель')
    year = models.CharField(max_length=4, verbose_name='Год издания')
    author_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор')
    def __str__(self):
        return self.title


