from django.shortcuts import render,HttpResponse
def index(request):
     context = {
          "mac":'jjj'
     }
     return render(request,'index.html',context)
     # return HttpResponse('kkkkkkkkkkkkkkkkk')
# def about(request):
#      return render(request,'about_us.html')
# def Services(request):
#      return render(request,'services.html')
# def Contact_us(request):
#      return render(request,'contact.html')
# 