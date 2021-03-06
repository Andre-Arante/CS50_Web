# Generated by Django 4.0.3 on 2022-03-20 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_category_remove_auction_listings_watchlisted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listings',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auction_category', to='auctions.category'),
        ),
    ]
