from django.shortcuts import render, redirect,get_object_or_404
from .models import Ted
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.models import User

def cover_views(request):    
    context = {}
    return render(request, 'lagos/cover.html',context)

def blog_views(request):
    emma = Ted.objects.all()
    template = 'lagos/blog.html'
    ordering = ['-id']
    context = {"emma":emma}
    return render(request, template, context)

def blog_post(request):
    emma = Ted.objects.all()
    if request.method== 'POST':
        post = request.POST.get('post')
        title = request.POST.get('title')
        description = request.POST.get('description')
        body = request.POST.get('body')
        author = request.POST.get('author')
        category = request.POST.get('category')
        file = request.FILES['images']

        if post != '':
            obj = Ted.objects.create(
                title = title,
                description = description,
                body = body,
                author = author,
                category = category,
                created_by = request.user,
                image= file,
            )
            obj.save()
            messages.success(request, "Your post has been added")
            print('Gone')
            return redirect('/home/')
    else:
        print('No Post')
    
    template = 'lagos/post.html'
    context = {"emma":emma}
    return render(request, template, context)

def about_page(request):
    template = 'lagos/about.html'
    return render(request,template)

def delete_button(request, id):

    obj = get_object_or_404(Ted, id = id)
    if request.method == 'POST':
        obj.delete() 
        messages.success(request, "Post successfully deleted!")
        return redirect('/home/')
    template = 'lagos/delete.html'
    context = {"obj":obj}
    return render(request, template, context)

def update_button(request, id):
    obj = Ted.objects.get(id=id)
    if request.method == 'POST':
        body = request.POST.get('body')
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        file = request.FILES['image']
        Ted.objects.filter(id=id).update(body=body,title=title,description=description,category=category,image=file)
        return redirect('home')
    context = {'obj':obj}
    return render(request, 'lagos/update.html',context)

# form = PostForm(request.POST or None)
    # if form.is_valid():
    #     obj = form.save(commit = False)
    #     obj.created_by = request.user
    #     obj.save()
    #     form = PostForm()

      # if len(request.FILES) != 0:
        #     if len(obj.image) > 0:
        #         os.remove(prod.image.path)
        #         file = request.FILES['image']

# @login_required(login_url='login')
