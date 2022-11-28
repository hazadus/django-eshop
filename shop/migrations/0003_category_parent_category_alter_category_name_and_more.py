# Generated by Django 4.1.3 on 2022-11-28 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_alter_category_options_alter_product_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="parent_category",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.category",
                verbose_name="Родительская категория",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=256, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="product",
            name="available",
            field=models.BooleanField(default=True, verbose_name="Наличие"),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="shop.category",
                verbose_name="Категория",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="created",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Создан"),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True, upload_to="products/%Y/%m/%d", verbose_name="Фото"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=256, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="Цена"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated",
            field=models.DateTimeField(auto_now=True, verbose_name="Изменён"),
        ),
    ]
