# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-09 14:26
from __future__ import unicode_literals

from django.db import migrations


def run_migration(apps, schema_editor):
    Billing = apps.get_model('billing', 'Billing')

    for billing in Billing.objects.all():
        for project in billing.projects.all():
            group = project.group_set.get(
                internal=True,
                name__endswith='@Billing',
            )
            billing.user.groups.add(group)


class Migration(migrations.Migration):

    dependencies = [
        ('weblate_auth', '0010_auto_20180509_1630'),
        ('billing', '0014_plan_change_access_control'),
    ]

    operations = [
        migrations.RunPython(run_migration)
    ]
