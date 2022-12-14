# Generated by Django 4.1 on 2022-09-21 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('balance', models.IntegerField()),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2app.groups')),
            ],
        ),
        migrations.CreateModel(
            name='ledgercreation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('alias', models.CharField(max_length=255, null=True)),
                ('under', models.CharField(max_length=255)),
                ('bank_details', models.CharField(max_length=255)),
                ('mname', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('state', models.CharField(max_length=255, null=True)),
                ('pincode', models.IntegerField(null=True)),
                ('pan_no', models.IntegerField(null=True)),
                ('registration_type', models.CharField(max_length=255, null=True)),
                ('gst_uin', models.IntegerField(null=True)),
                ('set_alter_gstdetails', models.CharField(max_length=255, null=True)),
                ('ac_holder_nm', models.CharField(max_length=255, null=True)),
                ('acc_no', models.IntegerField(null=True)),
                ('ifsc_code', models.IntegerField(null=True)),
                ('swift_code', models.IntegerField(null=True)),
                ('bank_name', models.CharField(max_length=255, null=True)),
                ('branch', models.CharField(max_length=255, null=True)),
                ('SA_cheque_bk', models.CharField(max_length=255, null=True)),
                ('Echeque_p', models.CharField(max_length=255, null=True)),
                ('occ_set_odl', models.CharField(max_length=255, null=True)),
                ('occ_ac_holder_nm', models.CharField(max_length=255, null=True)),
                ('occ_acc_no', models.IntegerField(null=True)),
                ('occ_ifsc_code', models.IntegerField(null=True)),
                ('occ_swift_code', models.IntegerField(null=True)),
                ('occ_bank_name', models.CharField(max_length=255, null=True)),
                ('occ_branch', models.CharField(max_length=255, null=True)),
                ('occ_SA_cheque_bk', models.CharField(max_length=255, null=True)),
                ('occ_Echeque_p', models.CharField(max_length=255, null=True)),
                ('od_set_odl', models.CharField(max_length=255, null=True)),
                ('od_ac_holder_nm', models.CharField(max_length=255, null=True)),
                ('od_acc_no', models.IntegerField(null=True)),
                ('od_ifsc_code', models.IntegerField(null=True)),
                ('od_swift_code', models.IntegerField(null=True)),
                ('od_bank_name', models.CharField(max_length=255, null=True)),
                ('od_branch', models.CharField(max_length=255, null=True)),
                ('od_SA_cheque_bk', models.CharField(max_length=255, null=True)),
                ('od_Echeque_p', models.CharField(max_length=255, null=True)),
                ('statutory_details', models.CharField(max_length=255, null=True)),
                ('type_of_ledger', models.CharField(max_length=100, null=True)),
                ('rounding_method', models.CharField(max_length=100, null=True)),
                ('rounding_limit', models.IntegerField(blank=True, default=None, null=True)),
                ('GST_Applicable', models.CharField(max_length=100, null=True)),
                ('Alter_GST_Details', models.CharField(max_length=100, null=True)),
                ('Appropriate', models.CharField(max_length=100, null=True)),
                ('Types_of_supply', models.CharField(max_length=100, null=True)),
                ('type_duty_tax', models.CharField(max_length=100, null=True)),
                ('tax_type', models.CharField(max_length=100, null=True)),
                ('percentage_of_calcution', models.CharField(max_length=100, null=True)),
                ('rond_method', models.CharField(max_length=100, null=True)),
                ('rond_limit', models.IntegerField(blank=True, default=None, null=True)),
                ('balance_billbybill', models.CharField(max_length=100, null=True)),
                ('credit_period', models.CharField(max_length=100, null=True)),
                ('creditdays_voucher', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='transactiontype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transactiontype', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Vouchertype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vouchertype', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='sales',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('Partyname', models.CharField(max_length=255)),
                ('salesledger', models.CharField(max_length=255)),
                ('item', models.CharField(max_length=255)),
                ('rate', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('total_amount', models.IntegerField()),
                ('particualrs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2app.ledger')),
            ],
        ),
        migrations.CreateModel(
            name='receipt',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('amount1', models.IntegerField()),
                ('amount2', models.IntegerField()),
                ('amount3', models.IntegerField()),
                ('particualrs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2app.ledger')),
            ],
        ),
        migrations.CreateModel(
            name='purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoiceno', models.IntegerField()),
                ('no', models.IntegerField()),
                ('partyname', models.CharField(max_length=225)),
                ('purchaseledger', models.CharField(max_length=225)),
                ('itemname', models.CharField(max_length=225)),
                ('quantity', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('total_amount', models.IntegerField()),
                ('particualrs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2app.ledger')),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('amount1', models.IntegerField()),
                ('amount2', models.IntegerField()),
                ('amount3', models.IntegerField()),
                ('particualrs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2app.ledger')),
            ],
        ),
        migrations.CreateModel(
            name='Particulars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('particualrs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2app.ledger')),
            ],
        ),
        migrations.CreateModel(
            name='journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('debit', models.IntegerField()),
                ('credit', models.IntegerField()),
                ('debit1', models.IntegerField()),
                ('credit1', models.IntegerField()),
                ('particualrs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2app.ledger')),
            ],
        ),
        migrations.CreateModel(
            name='contra',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('amount1', models.IntegerField()),
                ('amount2', models.IntegerField()),
                ('amount3', models.IntegerField()),
                ('particualrs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2app.ledger')),
            ],
        ),
        migrations.CreateModel(
            name='bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instno', models.IntegerField()),
                ('instdate', models.DateField()),
                ('amount', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2app.particulars')),
                ('date', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2app.account')),
                ('ledger', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2app.ledger')),
                ('transactiontype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2app.transactiontype')),
                ('vouchertype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2app.vouchertype')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2app.ledger'),
        ),
    ]
