from django.shortcuts import render,redirect,reverse
from .models import Pictures

def upload(request):
    if request.method=="POST":
        file_name=request.FILES.get('picture')
        pic=Pictures(pic=file_name)
        pic.save()
        return redirect(reverse('upload:show',args=(pic.id,)))

    return render(request, 'upload/upload.html')

def show_picture(request,fileid):
    filename=Pictures.objects.filter(id=fileid)[0].pic.url
    context={'name':filename}
    return render(request,'upload/show_pic.html',context=context)
