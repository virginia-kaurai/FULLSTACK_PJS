from django.shortcuts import render


from urllib import request



def index(request):
    return render(request, 'index.html')

def ClassList(request):
    return render(request, 'class_list.html')


def ClassDetail(request, class_id):
    return render(request, 'class_detail.html', {'class_id': class_id})
