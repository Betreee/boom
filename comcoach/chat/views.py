
from django.shortcuts import render

def chat_view(request):
    return render(request, 'chat/chat.html')

from django.http import HttpResponse
import random
import json

class Chatbot:
    def __init__(self):
        self.responses = {
            "hi": "Hello there!",
            "how are you?": "I am doing great!",
            "tell me something interesting": "Did you know that dolphins can recognize themselves in a mirror?",
            "tell me something funny": "Why did the tomato blush? Because it saw the salad dressing!"
        }
        self.default_responses = [
            'I see!', 'Interesting.', 'Could you tell me more?', 'What do you think?', 'That\'s awesome!', 'That\'s hilarious!'
        ]

    def generate_response(self, user_text):
        response = {'status': None, 'response': None}

        if user_text is not None:
            response['status'] = 'success'
            if user_text in self.responses.keys():
                response['response'] = self.responses[user_text]
            else:
                response['response'] = random.choice(self.default_responses)
        else:
            response['status'] = 'error'
            response['response'] = 'No input detected.'

        return response
i = []
def chatbot_response(request):
    
    # Get the user input
    user_text = request.GET.get('msg')
    # copy the user input to a list
    i.append(user_text)
    # Generate a response
    chatbot = Chatbot()
    response = chatbot.generate_response(user_text)
    # Return the response in JSON format
    print("user_text",user_text)
    return HttpResponse(json.dumps(response), content_type="application/json")