import csv
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import FileUploadInfo, WOTalon


def handle_uploaded_file(file, user):
    # Сначала сохраняем информацию о загрузке файла.
    upload_info = FileUploadInfo.objects.create(
        file_name=file.name,
        uploaded_by=user,
        # Вы можете добавить другие параметры, которые вы хотите сохранить.
    )

    # Затем читаем CSV файл и обновляем записи в БД.
    reader = csv.DictReader(file)
    for row in reader:
        WOTalon.objects.update_or_create(
            talon_id=row['talon_id'],
            defaults={
                'source': row['source'],
                # Здесь должны быть все другие поля модели WOTalon.
                # Обратите внимание, что вы должны преобразовать данные в правильный тип,
                # например, использовать `int()` для полей типа 'IntegerField', `datetime.strptime` для
                # полей типа 'DateField', и т. д.
            }
        )


def upload_file_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'], request.user)
            return redirect('success')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
