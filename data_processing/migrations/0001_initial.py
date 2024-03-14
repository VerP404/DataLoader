# Generated by Django 5.0.3 on 2024-03-14 12:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WOTalon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talon_id', models.IntegerField()),
                ('source', models.CharField(max_length=20)),
                ('source_id', models.IntegerField()),
                ('invoice_number', models.CharField(max_length=20, null=True)),
                ('upload_date', models.DateField(null=True)),
                ('annul_reason', models.CharField(max_length=50, null=True)),
                ('status', models.IntegerField()),
                ('talon_type', models.CharField(max_length=50)),
                ('purpose', models.CharField(max_length=50)),
                ('federal_purpose', models.CharField(max_length=100, null=True)),
                ('patient', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=1)),
                ('policy', models.CharField(max_length=100, null=True)),
                ('smo_code', models.IntegerField()),
                ('insurance_company', models.CharField(max_length=100)),
                ('enp', models.CharField(max_length=16, null=True)),
                ('treatment_start_date', models.DateField()),
                ('treatment_end_date', models.DateField()),
                ('doctor', models.CharField(max_length=100)),
                ('doctor_profile', models.CharField(max_length=200)),
                ('medical_staff_position', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('care_conditions', models.IntegerField()),
                ('medical_help_type', models.IntegerField()),
                ('disease_type', models.IntegerField(null=True)),
                ('main_disease_character', models.IntegerField(null=True)),
                ('visits', models.IntegerField(null=True)),
                ('visits_in_hospital', models.IntegerField(null=True)),
                ('home_visits', models.IntegerField(null=True)),
                ('case', models.CharField(max_length=50, null=True)),
                ('main_diagnosis', models.CharField()),
                ('accompanying_diagnosis', models.CharField()),
                ('medical_profile', models.IntegerField()),
                ('bed_profile', models.IntegerField(null=True)),
                ('dispensary_observation', models.IntegerField(null=True)),
                ('specialty', models.IntegerField(null=True)),
                ('outcome', models.IntegerField(null=True)),
                ('result', models.IntegerField(null=True)),
                ('operator', models.CharField(max_length=100)),
                ('initial_input_date', models.DateField()),
                ('last_change_date', models.DateField()),
                ('tariff', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('payment_type', models.CharField(max_length=100, null=True)),
                ('sanctions', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('ksg', models.CharField(max_length=100, null=True)),
                ('kz', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('drug_therapy_scheme_code', models.CharField(max_length=100, null=True)),
                ('uet', models.CharField(max_length=100, null=True)),
                ('classification_criteria', models.CharField(max_length=100, null=True)),
                ('shrm', models.CharField(max_length=100, null=True)),
                ('referring_hospital', models.CharField(max_length=200, null=True)),
                ('payment_method_code', models.IntegerField()),
                ('newborn', models.CharField(max_length=100, null=True)),
                ('representative', models.CharField(max_length=100, null=True)),
                ('additional_talon_status_info', models.CharField(null=True)),
                ('kslp', models.CharField(max_length=100, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FileUploadInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255)),
                ('upload_datetime', models.DateTimeField(auto_now_add=True)),
                ('total_rows', models.IntegerField()),
                ('type', models.CharField(choices=[('WOTalon', 'WODoctors')], max_length=20)),
                ('uploaded_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
