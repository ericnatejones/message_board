from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext

from django.views.generic.list import ListView 
from main.forms import *

from main.models import Comment, Message

# Create your views here.
class MessageListView(ListView):  
    model = Message
    template_name = "message_list.html"

def comments(request, pk):  
    comments = Comment.objects.filter(message_id = pk)
    context = {}
    context['comments'] = comments
    context['pk'] = pk
    return render_to_response( "comments.html", context, context_instance=RequestContext(request) )

def message_create(request):

    request_context = RequestContext(request)
    context = { }

    if request.method == 'POST':
        form = CreateMessageForm(request.POST)
        context["form"] = form

        if form.is_valid():
            form.save()
            print "is valid"
            context['valid'] = "is valid"
            return redirect('/message_list/')

        else:
            context['valid'] = form.errors
            print "wtf?"
            return render_to_response( "message_create.html", context, context_instance=request_context )

    else:
        form = CreateMessageForm()
        context["form"] = form

        return render_to_response( "message_create.html", context, context_instance=request_context )

def comment_create(request, pk):

    request_context = RequestContext(request)
    context = { }
    context['pk'] = pk

    if request.method == 'POST':
        form = CreateCommentForm(request.POST)
        
        context["form"] = form
        

        if form.is_valid():


			form.save()

			context['valid'] = "is valid"
			return redirect('/comments/%s' %pk)
        else:
			context['valid'] = form.errors

			return render_to_response( "comment_create.html", context, context_instance=request_context )

    else:
        form = CreateCommentForm(initial={'message':pk})

        context["form"] = form

        return render_to_response( "comment_create.html", context, context_instance=request_context )

def delete_message(request,pk):
	Message.objects.get(id=pk).delete()
	return redirect('/message_list/')

def delete_comment(request,pk):
	Comment.objects.get(id=pk).delete()	
	return redirect('/message_list/')
