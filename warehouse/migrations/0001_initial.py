# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-17 12:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AWS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField(default='none')),
                ('identity_lineitemid', models.TextField(null=True)),
                ('identity_timeinterval', models.TextField(null=True)),
                ('bill_invoiceid', models.TextField(null=True)),
                ('bill_billingentity', models.TextField(null=True)),
                ('bill_billtype', models.TextField(null=True)),
                ('bill_payeraccountid', models.TextField(null=True)),
                ('bill_billingperiodstartdate', models.DateTimeField(null=True)),
                ('bill_billingperiodenddate', models.DateTimeField(null=True)),
                ('lineitem_usageaccountid', models.TextField(null=True)),
                ('lineitem_lineitemtype', models.TextField(null=True)),
                ('lineitem_usagestartdate', models.DateTimeField(null=True)),
                ('lineitem_usageenddate', models.DateTimeField(null=True)),
                ('lineitem_productcode', models.TextField(null=True)),
                ('lineitem_usagetype', models.TextField(null=True)),
                ('lineitem_operation', models.TextField(null=True)),
                ('lineitem_availabilityzone', models.TextField(null=True)),
                ('lineitem_resourceid', models.TextField(null=True)),
                ('lineitem_usageamount', models.DecimalField(decimal_places=10, max_digits=19, null=True)),
                ('lineitem_normalizationfactor', models.DecimalField(decimal_places=10, max_digits=19, null=True)),
                ('lineitem_normalizedusageamount', models.DecimalField(decimal_places=10, max_digits=19, null=True)),
                ('lineitem_currencycode', models.TextField(null=True)),
                ('lineitem_unblendedrate', models.DecimalField(decimal_places=10, max_digits=19, null=True)),
                ('lineitem_unblendedcost', models.DecimalField(decimal_places=10, max_digits=19, null=True)),
                ('lineitem_blendedrate', models.DecimalField(decimal_places=10, max_digits=19, null=True)),
                ('lineitem_blendedcost', models.DecimalField(decimal_places=10, max_digits=19, null=True)),
                ('lineitem_lineitemdescription', models.TextField(null=True)),
                ('lineitem_taxtype', models.TextField(null=True)),
                ('product_productname', models.TextField(null=True)),
                ('product_availability', models.TextField(null=True)),
                ('product_clockspeed', models.TextField(null=True)),
                ('product_currentgeneration', models.TextField(null=True)),
                ('product_dedicatedebsthroughput', models.TextField(null=True)),
                ('product_directorysize', models.TextField(null=True)),
                ('product_directorytype', models.TextField(null=True)),
                ('product_directorytypedescription', models.TextField(null=True)),
                ('product_durability', models.TextField(null=True)),
                ('product_ebsoptimized', models.TextField(null=True)),
                ('product_endpointtype', models.TextField(null=True)),
                ('product_enhancednetworkingsupported', models.TextField(null=True)),
                ('product_fromlocation', models.TextField(null=True)),
                ('product_fromlocationtype', models.TextField(null=True)),
                ('product_group', models.TextField(null=True)),
                ('product_groupdescription', models.TextField(null=True)),
                ('product_instancefamily', models.TextField(null=True)),
                ('product_instancetype', models.TextField(null=True)),
                ('product_licensemodel', models.TextField(null=True)),
                ('product_location', models.TextField(null=True)),
                ('product_locationtype', models.TextField(null=True)),
                ('product_maxiopsburstperformance', models.TextField(null=True)),
                ('product_maxiopsvolume', models.TextField(null=True)),
                ('product_maxthroughputvolume', models.TextField(null=True)),
                ('product_maxvolumesize', models.TextField(null=True)),
                ('product_memory', models.TextField(null=True)),
                ('product_networkperformance', models.TextField(null=True)),
                ('product_operatingsystem', models.TextField(null=True)),
                ('product_operation', models.TextField(null=True)),
                ('product_physicalprocessor', models.TextField(null=True)),
                ('product_preinstalledsw', models.TextField(null=True)),
                ('product_processorarchitecture', models.TextField(null=True)),
                ('product_processorfeatures', models.TextField(null=True)),
                ('product_productfamily', models.TextField(null=True)),
                ('product_servicecode', models.TextField(null=True)),
                ('product_sku', models.TextField(null=True)),
                ('product_storage', models.TextField(null=True)),
                ('product_storageclass', models.TextField(null=True)),
                ('product_storagemedia', models.TextField(null=True)),
                ('product_tenancy', models.TextField(null=True)),
                ('product_tolocation', models.TextField(null=True)),
                ('product_tolocationtype', models.TextField(null=True)),
                ('product_transfertype', models.TextField(null=True)),
                ('product_usagetype', models.TextField(null=True)),
                ('product_vcpu', models.DecimalField(decimal_places=10, max_digits=19, null=True)),
                ('product_version', models.TextField(null=True)),
                ('product_volumetype', models.TextField(null=True)),
                ('pricing_leasecontractlength', models.TextField(null=True)),
                ('pricing_offeringclass', models.TextField(null=True)),
                ('pricing_purchaseoption', models.TextField(null=True)),
                ('pricing_publicondemandcost', models.DecimalField(decimal_places=10, max_digits=19, null=True)),
                ('pricing_publicondemandrate', models.DecimalField(decimal_places=10, max_digits=19, null=True)),
                ('pricing_term', models.TextField(null=True)),
                ('pricing_unit', models.TextField(null=True)),
                ('reservation_availabilityzone', models.TextField(null=True)),
                ('reservation_normalizedunitsperreservation', models.TextField(null=True)),
                ('reservation_numberofreservations', models.TextField(null=True)),
                ('reservation_reservationarn', models.TextField(null=True)),
                ('reservation_totalreservednormalizedunits', models.DecimalField(decimal_places=10, max_digits=19, null=True)),
                ('reservation_totalreservedunits', models.DecimalField(decimal_places=10, max_digits=19, null=True)),
                ('reservation_unitsperreservation', models.DecimalField(decimal_places=10, max_digits=19, null=True)),
                ('resourcetags_aws_cloudformation_logical_id', models.TextField(null=True)),
                ('resourcetags_aws_cloudformation_stack_id', models.TextField(null=True)),
                ('resourcetags_aws_cloudformation_stack_name', models.TextField(null=True)),
                ('resourcetags_aws_createdby', models.TextField(null=True)),
                ('resourcetags_user_environment', models.TextField(null=True)),
                ('resourcetags_user_graylog', models.TextField(null=True)),
                ('resourcetags_user_name', models.TextField(null=True)),
                ('resourcetags_user_owner', models.TextField(null=True)),
                ('resourcetags_user_team', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AWS_Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget_name', models.TextField()),
                ('actual_spend', models.DecimalField(decimal_places=10, max_digits=19, null=True)),
                ('forcasted_spend', models.DecimalField(decimal_places=10, max_digits=19, null=True)),
                ('limit', models.DecimalField(decimal_places=10, max_digits=19, null=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='AWS_files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.TextField(null=True)),
                ('key', models.TextField(default='empty', null=True)),
                ('last_updated', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Budget_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.TextField(null=True)),
                ('account', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('r_id', models.IntegerField(unique=True)),
                ('month', models.DateField(null=True)),
                ('ammount', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('comp', models.TextField(blank=True, null=True)),
                ('exp', models.DateTimeField(blank=True, null=True)),
                ('reg', models.TextField(blank=True, null=True)),
                ('nameserver', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted', models.DateField()),
                ('r_id', models.IntegerField(unique=True)),
                ('inv_date', models.DateField()),
                ('gl_id', models.CharField(max_length=6)),
                ('vendor', models.TextField(null=True)),
                ('invoice', models.TextField(null=True)),
                ('memo', models.TextField(null=True)),
                ('cost_structure', models.TextField(null=True)),
                ('category', models.TextField(null=True)),
                ('class_1', models.TextField(null=True)),
                ('class_2', models.TextField(null=True)),
                ('comments', models.TextField(null=True)),
                ('owner', models.TextField(null=True)),
                ('account', models.CharField(max_length=6)),
                ('dept_num', models.CharField(max_length=4)),
                ('dept', models.TextField(null=True)),
                ('location_name', models.TextField(null=True)),
                ('location', models.TextField(null=True)),
                ('project_name', models.TextField(null=True)),
                ('txn_no', models.TextField()),
                ('jnl', models.TextField(null=True)),
                ('curr', models.CharField(max_length=3)),
                ('money', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='High_Level_Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.DecimalField(decimal_places=3, max_digits=6, unique=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='IsAlive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fil', models.FileField(upload_to='data/')),
            ],
        ),
        migrations.AddField(
            model_name='gl',
            name='code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.High_Level_Budget'),
        ),
        migrations.AddField(
            model_name='budget_detail',
            name='code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.High_Level_Budget'),
        ),
    ]
