from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chatbot.models import ChatHistory
# Create your views here.

from hugchat import hugchat
from hugchat.login import Login

# Log in to huggingface and grant authorization to huggingchat

sign = Login("ds307931@gmail.com", "Ds307931@")
cookies = sign.login()

# Save cookies to the local directory
cookie_path_dir = "./cookies_snapshot"
sign.saveCookiesToDir(cookie_path_dir)

chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
id = chatbot.new_conversation()
#print(id)
chatbot.change_conversation(id)


@api_view(["POST"])
def chat_message(request):
    data = request.data
    response = chatbot.chat(text=data['prompt'])

    message = ChatHistory()
    message.session_id = id
    message.prompt = data['prompt']
    message.response = response
    message.save()

    return Response(data={"response": response}, status=200)

@api_view(["GET"])
def chat_history(request):
    records = ChatHistory.objects.filter(session_id=id).order_by('created').all()
    data = []
    for item in records:
        data.append(
            {
                "prompt": item.prompt,
                "response": item.response,
                "date": item.created
            }
        )

    return Response(data={"data": data}, status=200)
