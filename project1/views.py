from webbrowser import get
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render

# homepage ={
#     'title':'Home page New',
#     'clist':['PHP','Java','Django'],
#     'code':[],
#     'Student_details':[
#         {'name':'Vishal','mobile':'9876543210'},
#         {'name':'testing','mobile':'9876543210'},
#     ]
# }

def Home(request):
    return render(request,"index.html")

def accounts(request):
    if request.method=="GET":
        output=request.GET['output']
    return render(request,"accounts.html",{'output': output})

def aboutdetails(request,id):
    return HttpResponse(id)

def formresult(request):
    return HttpResponse(request)

def products(request):
    return render(request,"products.html")

def form(request):
    a=0
    try:
        # if request.method == "GET":
        # n1=int(request.GET['name1'])
        # n2=int(request.GET['name2'])
        if request.method == "POST":
            n1=int(request.POST['name1'])
            n2=int(request.POST['name2'])
            a=n1+n2
            data={
                'output':a
            }

        # url="/accounts/?output={}".format(a)

        # return HttpResponseRedirect(url)

    except:
        pass

    return render(request,"form.html",{'result':a})