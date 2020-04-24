from django.shortcuts import render,redirect
from .forms import PostForm
# Create your views here.
def add_post(request):
    print('dd')
    form =PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    context ={
        'form':form
    }

    return render(request, 'addpost.html',context)