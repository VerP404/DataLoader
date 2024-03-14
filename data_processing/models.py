from django.contrib.auth.models import User
from django.db import models


class WOTalon(models.Model):
    talon_id = models.IntegerField()  # Талон
    source = models.CharField(max_length=20)  # Источник
    source_id = models.IntegerField()  # ID источника
    invoice_number = models.CharField(max_length=20, null=True)  # Номер счёта
    upload_date = models.DateField(null=True)  # Дата выгрузки
    annul_reason = models.CharField(max_length=50, null=True)  # Причина аннулирования
    status = models.IntegerField()  # Статус
    talon_type = models.CharField(max_length=50)  # Тип талона
    purpose = models.CharField(max_length=50)  # Цель
    federal_purpose = models.CharField(max_length=100, null=True)  # Фед. цель
    patient = models.CharField(max_length=100)  # Пациент
    date_of_birth = models.DateField()  # Дата рождения
    gender = models.CharField(max_length=1)  # Пол
    policy = models.CharField(max_length=100, null=True)  # Полис
    smo_code = models.IntegerField()  # Код СМО
    insurance_company = models.CharField(max_length=100)  # Страховая
    enp = models.CharField(max_length=16, null=True)  # ЕНП
    treatment_start_date = models.DateField()  # Начало лечения
    treatment_end_date = models.DateField()  # Окончание лечения
    doctor = models.CharField(max_length=100)  # Врач
    doctor_profile = models.CharField(max_length=200)  # Врач (Профиль МП)
    medical_staff_position = models.CharField(max_length=100)  # Должность мед.персонала (V021)
    department = models.CharField(max_length=100)  # Подразделение
    care_conditions = models.IntegerField()  # Условия оказания помощи
    medical_help_type = models.IntegerField()  # Вид мед. помощи
    disease_type = models.IntegerField(null=True)  # Тип заболевания
    main_disease_character = models.IntegerField(null=True)  # Характер основного заболевания
    visits = models.IntegerField(null=True)  # Посещения
    visits_in_hospital = models.IntegerField(null=True)  # Посещения в МО
    home_visits = models.IntegerField(null=True)  # Посещения на Дому
    case = models.CharField(max_length=50, null=True)  # Случай
    main_diagnosis = models.CharField()  # Диагноз основной (DS1)
    accompanying_diagnosis = models.CharField()  # Сопутствующий диагноз (DS2)
    medical_profile = models.IntegerField()  # Профиль МП
    bed_profile = models.IntegerField(null=True)  # Профиль койки
    dispensary_observation = models.IntegerField(null=True)  # Диспансерное наблюдение
    specialty = models.IntegerField(null=True)  # Специальность
    outcome = models.IntegerField(null=True)  # Исход
    result = models.IntegerField(null=True)  # Результат
    operator = models.CharField(max_length=100)  # Оператор
    initial_input_date = models.DateField()  # Первоначальная дата ввода
    last_change_date = models.DateField()  # Дата последнего изменения
    tariff = models.DecimalField(max_digits=10, decimal_places=2)  # Тариф
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Сумма
    paid = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Оплачено
    payment_type = models.CharField(max_length=100, null=True)  # Тип оплаты
    sanctions = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Санкции
    ksg = models.CharField(max_length=100, null=True)  # КСГ
    kz = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # КЗ
    drug_therapy_scheme_code = models.CharField(max_length=100, null=True)  # Код схемы лекарственной терапии
    uet = models.CharField(max_length=100, null=True)  # УЕТ
    classification_criteria = models.CharField(max_length=100, null=True)  # Классификационный критерий
    shrm = models.CharField(max_length=100, null=True)  # ШРМ
    referring_hospital = models.CharField(max_length=200, null=True)  # МО, направившая
    payment_method_code = models.IntegerField()  # Код способа оплаты
    newborn = models.CharField(max_length=100, null=True)  # Новорожденный
    representative = models.CharField(max_length=100, null=True)  # Представитель
    additional_talon_status_info = models.CharField(null=True)  # Доп. инф. о статусе талона
    kslp = models.CharField(max_length=100, null=True)  # КСЛП
    last_updated = models.DateTimeField(auto_now=True)  # Последнее обновление в базе данных

    def __str__(self):
        return self.talon_id


class FileUploadInfo(models.Model):
    FILE_TYPES = [
        ('WOTalon', 'WODoctors'),
    ]

    file_name = models.CharField(max_length=255)  # имя файла
    upload_datetime = models.DateTimeField(auto_now_add=True)  # Дата загрузки
    total_rows = models.IntegerField()  # Количество строк в файле
    type = models.CharField(max_length=20, choices=FILE_TYPES)  # Тип файла
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Пользователь

    def __str__(self):
        return self.file_name
