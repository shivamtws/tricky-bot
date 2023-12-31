from django.shortcuts import render,redirect
from django.http import JsonResponse
import openai


from django.contrib import auth
from django.utils import timezone
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

openai_api_key = os.getenv('OPENAI_KEY')

def ask_openai(message):
    response = openai.Completion.create(
                    model='text-davinci-003',
                    prompt=message,
                    n=1,
                    stop=None,
                    max_tokens = 2000,
                    api_key=openai_api_key
                )
    description = response.choices[0].text.strip()
    return description

# Create your views here.

def chatbot(request):

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        # chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now)
        # chat.save()
        chats = "dbj"
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chat.html')
