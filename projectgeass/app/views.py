from django.shortcuts import render
from django.http import JsonResponse
from app.models import Post
from django.http import HttpResponse


def index(request):
    
   # posts = Post.objects.all()
   
   # serialized_posts=[]
   # for post in posts:
        # temp_dict = {}
        # temp_dict["title"]=post.title
        # temp_dict["text"]=post.text
        # temp_dict["id"]=post.id
        # temp_dict["time"]=post.time
        # serialized_posts.append(temp_dict)

# user authenitcation, comment , login logout, passowrd change, decorators       
        
   

    #return JsonResponse({"posts":serialized_posts})


   posts=Post.objects.all()
   return render(request,'app/index.html',{'posts':posts})





def part(request,id1):
 try:    
   posts = Post.objects.get(id=id1)
   serialized_posts=[]
   
   temp_dict={}
   temp_dict["title"]=posts.title
   temp_dict["text"]=posts.text
   serialized_posts.append(temp_dict)
 
   return JsonResponse({"posts":serialized_posts})

 except Exception:
   return HttpResponse("error")


# Create your views here.

