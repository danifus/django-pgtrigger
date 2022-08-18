# Generated by Django 3.2.15 on 2022-08-17 22:11

from django.db import migrations
from psqlextra.backend.migrations.operations import PostgresAddRangePartition


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0010_auto_20220817_2211'),
    ]

    operations = [
        PostgresAddRangePartition(
            model_name="partitionmodel",
            name="pt1",
            from_values="2019-01-01",
            to_values="2019-02-01",
        ),
        PostgresAddRangePartition(
            model_name="partitionmodel",
            name="pt2",
            from_values="2019-02-01",
            to_values="2019-03-01",
        ),
        PostgresAddRangePartition(
            model_name="partitionmodel",
            name="pt3",
            from_values="2019-03-01",
            to_values="2019-04-01",
        ),
    ]