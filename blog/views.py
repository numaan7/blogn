from django.shortcuts import get_object_or_404, render,redirect
from .models import Category, Contact, Post,Comment
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from taggit.models import Tag

def post_list(request, tag_slug=None):
    posts = Post.objects.filter(status="published").order_by('-created_at')
    categories=Category.objects.all()
    recent_post=Post.objects.filter(status="published").order_by('-created_at')[0:3]
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
    
    paginator = Paginator(posts, 7) # 10 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
       
    return render(request,'post_list.html',{'posts':posts, page:'pages','categories':categories,'tag':tag,'recent_post':recent_post})

def category(request,category):

    categories=Category.objects.all()
    posts=Post.objects.filter(category__name__contains=category)

    return render(request,'cat.html',{'posts':posts,'categories':categories})
def post_detail(request,slug):
    tag = None
    recent_post=Post.objects.filter(status="published").order_by('-created_at')[0:3]
    
    post=get_object_or_404(Post,slug=slug,status="published")
    categories=Category.objects.all()
    print(post.tags.all)
    post.views=post.views+1 
    post.save()
    if request.method=="POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        comment=request.POST.get("comment")
        commentid=request.POST.get("commentid")
        post= Post.objects.get(id=commentid)
        slug=request.POST.get("slug")
        comment=Comment(fname=fname,lname=lname,email=email,comment=comment,post=post)
        comment.save()
        redirect("/"+ slug)
    comments=Comment.objects.filter(post=post).order_by('-created')
    return render(request,"post_details.html",{'post':post,'categories':categories,'comments':comments,'recent_post':recent_post})
def search(request):
    search=request.GET['search']
    posts=Post.objects.filter(title__icontains=search)
    return render(request,"search.html",{'posts':posts})
def contact(request):
    if request.method=="POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        message=request.POST.get("comment")
        contact=Contact(fname=fname,lname=lname,email=email,message=message)
        contact.save()
        redirect("/")
    categories=Category.objects.all()
    return render(request,'contact.html',{'categories':categories})
def error(request):
    return render(request,"404.html")
    