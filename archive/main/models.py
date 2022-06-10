from django.db import models

class Period(models.Model):
    class Meta:
        verbose_name = 'Период'
        verbose_name_plural = 'Периоды'

    name = models.CharField(max_length=100, verbose_name='Название')
    def __str__(self):
        return self.name

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

    title = models.TextField(verbose_name='Название')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', blank=True)
    link = models.CharField(max_length=1000, verbose_name='Ссылка')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    period = models.ForeignKey('Period', on_delete=models.CASCADE, verbose_name='Период')
    country = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name='Страна', blank=True)
    author = models.CharField(max_length=1000, verbose_name='Автор/издатель', blank=True)
    year = models.CharField(max_length=4, verbose_name='Год издания', blank=True)
    author_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор')
    pub_author_admin = models.CharField(max_length=1000, verbose_name='Автор публикации')
    pub_time_admin = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')
    def __str__(self):
        return self.title


