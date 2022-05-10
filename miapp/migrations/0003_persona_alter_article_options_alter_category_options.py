# Generated by Django 4.0.3 on 2022-05-04 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_article_image_alter_article_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('fecha_nac', models.DateField()),
                ('ciudad', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Articulo', 'verbose_name_plural': 'Articulos'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
    ]
