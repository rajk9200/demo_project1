from django.shortcuts import render

# Create your views here.
from Posts.models import Posts,PostCot
def home(request):
    cat_res =PostCot.objects.get(name="Results")
    resposts =Posts.objects.filter(title=cat_res)

    cat_job = PostCot.objects.get(name="Latest Jobs")
    jobposts = Posts.objects.filter(title=cat_job)

    cat_admtcard = PostCot.objects.get(name="Admit Card")
    jobadmtcards = Posts.objects.filter(title=cat_admtcard)
    context ={
        'resposts':resposts,
        'jobposts':jobposts,
        'jobadmtcards':jobadmtcards,
    }
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')

def contacts(request):


    return render(request,'contacts.html')



def details(reqeust,pk=None):
    post = Posts.objects.get(id=pk)

    data ={
        'post':post
    }
    return render(reqeust, 'details.html',data)


def result_page(request):
    cat_res = PostCot.objects.get(name="Results")
    resposts = Posts.objects.filter(title=cat_res)
    context ={
        'resposts':resposts
    }

    return render(request,'resultpage.html',context)