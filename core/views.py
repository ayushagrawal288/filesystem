from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.http import JsonResponse
from core.utils.main import FileStorage
from core.config import *


# storage = FileStorage('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,
#                       region=region, bucket_name=bucket_name, temp_file=temp_file)

storage = FileStorage('default', directory=default_storage_directory)


def home(request):
    return render(request, 'home.html')


def upload_file(request):
    if request.method == 'POST':
        try:
            file = request.FILES['file']
        except MultiValueDictKeyError:
            return JsonResponse({"message": "no input file"})
        filename = request.POST.get('filename')
        try:
            storage.create(filename, file)
        except ValueError as e:
            return JsonResponse({"error": e.__str__()})
        return JsonResponse({"payload": "success"})
    return render(request, 'core/test.html')


def list_files(request):
    try:
        data = storage.list()
    except ValueError as e:
        return JsonResponse({"error": e.__str__()})
    return JsonResponse({"payload": data})


def get_file(request):
    if request.method == 'POST':
        # import pdb
        # pdb.set_trace()
        filename = request.POST.get('filename')
        return_type = request.POST.get('type', 'file')
        try:
            data = storage.fetch(filename)
        except ValueError as e:
            return JsonResponse({"error": e.__str__()})
        if return_type == 'file':
            return redirect('/' + data.get('filename'))
        return JsonResponse({"payload": data})
    return render(request, 'core/file.html')


def rename_file(request):
    if request.method == 'POST':
        new_name = request.POST.get('new_name')
        previous_name = request.POST.get('previous_name')
        try:
            storage.rename(new_name, previous_name)
        except ValueError as e:
            return JsonResponse({"error": e.__str__()})
        return JsonResponse({"payload": "success"})
    return render(request, 'core/rename.html')


def delete_file(request):
    if request.method == 'POST':
        filename = request.POST.get('filename')
        try:
            storage.delete(filename)
        except ValueError as e:
            return JsonResponse({"error": e.__str__()})
        return JsonResponse({"payload": "success"})
    return render(request, 'core/delete.html')
