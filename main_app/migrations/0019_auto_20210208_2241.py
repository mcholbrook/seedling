# Generated by Django 3.1.6 on 2021-02-08 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_auto_20210208_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seed',
            name='kind',
            field=models.CharField(choices=[('flower', 'flower'), ('herb', 'herb'), ('arugula', 'arugula'), ('asparagus', 'asparagus'), ('basil', 'basil'), ('beans(green)', 'beans(green)'), ('beet', 'beet'), ('blueberries', 'blueberries'), ('bokchoy)', 'bokchoy'), ('broccoli', 'broccoli'), ('brussels', 'brussels'), ('cabbage(green)', 'cabbage(green)'), ('cabbage(red)', 'cabbage(red)'), ('calendula', 'calendula'), ('cantaloupe', 'cantaloupe'), ('carrots', 'carrots'), ('cauliflower', 'cauliflower'), ('chives', 'chives'), ('collards', 'collards'), ('corn', 'corn'), ('cucumber', 'cucumber'), ('daikon', 'daikon'), ('delicata', 'delicata'), ('dill', 'dill'), ('eggplant', 'eggplant'), ('eggplant(graffiti)', 'eggplant(graffiti'), ('fennel', 'fennel'), ('flower(other)', 'flower(other)'), ('fruit(other)', 'fruit(other)'), ('garlic', 'garlic'), ('jalapeno', 'jalapeno'), ('kale', 'kale'), ('lettuce', 'lettuce'), ('mint', 'mint'), ('onion', 'onion'), ('oregano', 'oregano'), ('parsley', 'parsley'), ('peas', 'peas'), ('peas(snow)', 'peas(snow)'), ('pepper(hot)', 'pepper(hot)'), ('pepper(bell)', 'pepper(bell)'), ('potato', 'potato'), ('pumpkin', 'pumpkin'), ('radish', 'radish'), ('raspberries', 'raspberries'), ('rhubarb', 'rhubarb'), ('sage', 'sage'), ('scallions', 'scallions'), ('spinach', 'spinach'), ('squash(acorn)', 'squash(acorn)'), ('squash(butternut)', 'squash(butternut'), ('squash(summer)', 'squash(summer)'), ('strawberries', 'strawberries'), ('tarragon', 'tarragon'), ('thyme', 'thyme'), ('tomato', 'tomato'), ('tomato(cherry)', 'tomato(cherry)'), ('tomato(heirloom)', 'tomato(heirloom)'), ('turnip', 'turnip'), ('veggie(other)', 'veggie(other)'), ('watermelon', 'watermelon'), ('yam', 'yam')], default='flower', max_length=500),
        ),
    ]
