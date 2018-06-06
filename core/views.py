from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from django.http import JsonResponse
from core.utils.main import FileStorage

storage = FileStorage('s3')


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
        filename = request.POST.get('filename')
        try:
            data = storage.fetch(filename)
        except ValueError as e:
            return JsonResponse({"error": e.__str__()})
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
    return render(request, 'core/file.html')
