from django.db import models


def upload_image_book(instance, filename):
    return f"{instance.title}-{filename}"


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(verbose_name='Título', max_length=150)
    category = models.ForeignKey(
        Category, verbose_name='Categoria', related_name='books', on_delete=models.CASCADE)
    author = models.CharField(verbose_name='Autor',
                              max_length=100, default='John Doe')
    isbn = models.CharField(verbose_name='ISBN', max_length=13)
    pages = models.IntegerField(verbose_name='N° de páginas')
    price = models.FloatField(verbose_name='Preço')
    stock = models.IntegerField(verbose_name='Estoque', )
    description = models.TextField(verbose_name='Descrição', )
    imageUrl = models.ImageField(
        verbose_name='Imagem', upload_to=upload_image_book, blank=True, null=True)
    created_by = models.ForeignKey(
        'auth.User', verbose_name='Criado por', related_name='books', on_delete=models.CASCADE)
    status = models.BooleanField(verbose_name='Status', default=True)
    date_created = models.DateField(
        verbose_name='Data de cadastramento', auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title


class Product(models.Model):
    product_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    price = models.FloatField()
    stock = models.IntegerField()
    imageUrl = models.URLField()
    created_by = models.ForeignKey(
        'auth.User', related_name='products', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{} {}'.format(self.product_tag, self.name)
