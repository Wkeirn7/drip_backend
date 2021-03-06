# Generated by Django 4.0.4 on 2022-06-06 00:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graph_name', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('reinvestment_period', models.CharField(max_length=50)),
                ('reinvestment_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('graph_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='graphs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('company_name', models.CharField(max_length=255)),
                ('price_per_share', models.DecimalField(decimal_places=2, max_digits=15)),
                ('div_yield', models.DecimalField(decimal_places=2, max_digits=4)),
                ('shares', models.DecimalField(decimal_places=2, max_digits=15)),
                ('company_overview', models.TextField()),
                ('graph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='api.graph')),
            ],
        ),
    ]
