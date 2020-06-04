from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import FileResponse
from django.template import RequestContext
from django.urls import reverse
from django.utils.http import urlquote

from .models import FileInfo
from .forms import UploadForm
import os


# Create your views here.
def upload(request):
    if request.method == 'POST':
        #form = UploadForm(request.POST, request.FILES)
        print("1")
        my_file = request.FILES.get("myfile", None)
        if not my_file:
            return HttpResponse("no files for update!")
        else:
            file_info = FileInfo(file_name=my_file.name, file_size=my_file.size,
                                 file_path=os.path.join("D:\\upload", my_file.name))
            file_info.save()
            
            destination = open(os.path.join("D:\\upload", my_file.name), 'wb+')
            for chunk in my_file.chunks():
                destination.write(chunk)
            destination.close()

            #return HttpResponse("upload over!")
            return HttpResponseRedirect('/uploader/list/')
    else:
        form = UploadForm()
        return render(request, 'uploader/upload.html', {"form": form})


def list(request):
    file_infos = FileInfo.objects.all()
    return render(request, 'uploader/list.html', {"file_infos": file_infos})


def download(request, id):
    file_info = FileInfo.objects.get(id=id)
    print("下载的文件名：" + file_info.file_name)
    file = open(file_info.file_path, 'rb')
    response = FileResponse(file)
    response['Content-Disposition'] = 'attachment;filename="%s"' % urlquote(file_info.file_name)
    return response


def delete(request, id):
    file_info = FileInfo.objects.get(id=id)
    file_info.delete()

    return HttpResponseRedirect('/uploader/list/')
