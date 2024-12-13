# Generated by Django 4.1.6 on 2024-12-12 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soft_delete', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Deleted At')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('author', models.CharField(max_length=255, verbose_name='Author')),
                ('ISBN', models.CharField(max_length=13, unique=True, verbose_name='ISBN')),
                ('page_count', models.PositiveIntegerField(verbose_name='Page Count')),
                ('availability', models.BooleanField(default=True, verbose_name='Availability')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soft_delete', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Deleted At')),
                ('borrow_date', models.DateTimeField(auto_now_add=True, verbose_name='Borrow Date')),
                ('return_date', models.DateTimeField(blank=True, null=True, verbose_name='Return Date')),
                ('status', models.CharField(choices=[('borrowed', 'Borrowed'), ('returned', 'Returned')], default='borrowed', max_length=10, verbose_name='Status')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='library.book', verbose_name='Book')),
            ],
            options={
                'verbose_name': 'Loan',
                'verbose_name_plural': 'Loans',
            },
        ),
    ]
