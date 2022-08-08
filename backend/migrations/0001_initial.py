# Generated by Django 3.1 on 2022-01-05 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=64, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Kanban',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('photo', models.CharField(blank=True, max_length=100, null=True)),
                ('groups', models.IntegerField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='backend.page')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Page_element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('element_type', models.CharField(max_length=85)),
                ('order_on_page', models.FloatField()),
                ('group', models.IntegerField()),
                ('column', models.IntegerField()),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_elements', to='backend.page')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('page_element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table', to='backend.page_element')),
            ],
        ),
        migrations.CreateModel(
            name='Table_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=1000, null=True)),
                ('number', models.FloatField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('checkbox', models.BooleanField(blank=True, null=True)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('property_type', models.CharField(max_length=100)),
                ('header', models.BooleanField()),
                ('width', models.IntegerField()),
                ('order', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='To_do',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('completed', models.BooleanField()),
                ('page_element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_do', to='backend.page_element')),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=5000, null=True)),
                ('page_element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text', to='backend.page_element')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('table_data', models.ManyToManyField(blank=True, related_name='tags', to='backend.Table_data')),
                ('table_head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_heads', to='backend.table_data')),
            ],
        ),
        migrations.CreateModel(
            name='Table_row',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.FloatField()),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rows', to='backend.table')),
            ],
        ),
        migrations.AddField(
            model_name='table_data',
            name='table_row',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='backend.table_row'),
        ),
        migrations.CreateModel(
            name='PageLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.page')),
                ('page_element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_link', to='backend.page_element')),
            ],
        ),
        migrations.CreateModel(
            name='Kanban_Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('color', models.CharField(max_length=100)),
                ('order', models.FloatField()),
                ('kanban', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kanban_group', to='backend.kanban')),
            ],
        ),
        migrations.CreateModel(
            name='Kanban_Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('order_on_group', models.FloatField()),
                ('kanban_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kanban_card', to='backend.kanban_group')),
            ],
        ),
        migrations.AddField(
            model_name='kanban',
            name='page_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kanban', to='backend.page_element'),
        ),
        migrations.CreateModel(
            name='Heading_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_text', models.CharField(blank=True, max_length=85, null=True)),
                ('page_element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='heading_2', to='backend.page_element')),
            ],
        ),
        migrations.CreateModel(
            name='Heading_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_text', models.CharField(blank=True, max_length=85, null=True)),
                ('page_element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='heading_1', to='backend.page_element')),
            ],
        ),
    ]
