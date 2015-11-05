from django import forms
from main.models import Comment, Message


class CreateMessageForm(forms.ModelForm): 
	
    class Meta:
        model = Message

        fields = ['title', 'message', 'message_maker']


class CreateCommentForm(forms.ModelForm): 

    
    class Meta:
        model = Comment

        fields = ['comment', 'comment_maker', 'message']
