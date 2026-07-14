from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def ImageGallery(request):
    return render(request,'home.html')

def about(request):
    score=[85,90,78,92,88]
    subject="maths"
    return render(request,'about.html',{'score':score, 'subject':subject})

def student(request):
    marks={"aparna":55,"madhuri":88,"anesha":90}
    updated={}
    for key,value in marks.items():
        if value>85:
            updated[key]=value
    return render(request,'conditional.htm',{'marks':marks,'updated':updated})

def templateInheritance(request):
    return render(request,'child.html')
