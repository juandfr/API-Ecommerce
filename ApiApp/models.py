from django.db import models
from django.contrib.auth.models import User


def upload_image_book(instance, filename):
    return f"{instance.title}-{filename}"


class Category(models.Model):
    title = models.CharField(verbose_name='Título', max_length=255)

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
        verbose_name='Imagem', upload_to=upload_image_book, blank=False, null=False)
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
    product_tag = models.CharField(verbose_name='Título', max_length=10, null=False , blank=False )
    name = models.CharField(verbose_name='Nome', max_length=100)
    category = models.ForeignKey(
        Category, verbose_name='Categoria', related_name='products', on_delete=models.CASCADE)
    price = models.FloatField(verbose_name='Preço')
    stock = models.IntegerField(verbose_name='Estoque')
    imageUrl = models.ImageField(
        verbose_name='Imagem', upload_to=upload_image_book, blank=False, null=False)
    created_by = models.ForeignKey(
        'auth.User', verbose_name='Criado por', related_name='products', on_delete=models.CASCADE)
    status = models.BooleanField(verbose_name='Status', default=True)
    date_created = models.DateField(verbose_name='Data de criação', auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{} {}'.format(self.product_tag, self.name)


class Cart(models.Model):
    cart_id = models.OneToOneField(
        User, verbose_name='Data de criação', on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(verbose_name='Data de criação', auto_now_add=True)
    books = models.ManyToManyField(Book, verbose_name='Livros')
    products = models.ManyToManyField(Product, verbose_name='Produtos')

    class Meta:
        ordering = ['cart_id', '-created_at']

    def __str__(self):
        return f'{self.cart_id}'
