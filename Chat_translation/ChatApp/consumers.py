import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Message,Room
from common.models import User
from .papago import papagoapi

class ChatConsumer(WebsocketConsumer):
    
    def fetch_messages(self,data):#채팅기록 가져오기
        room_id = int(self.room_name)
        messages = Message.last_10_message(self,room_id=room_id)
        content = {
            'command':'messages',
            'messages':self.messages_to_json(messages)
        }
        self.send_message(content)
        
    
    def new_messages(self,data):#채팅 보내기
        user_id = data['user_id']
        room_id = int(self.room_name)
        user_contact = User.objects.filter(id = user_id)[0]
        room_contact = Room.objects.filter(id = room_id)[0]
        message_create = Message.objects.create(
            author = user_contact,
            room_id = room_contact,
            content = data['message']
            )
        content = {
            'command':'new_messages',
            'message': self.message_to_json(message_create)
        }
        return self.send_chat_message(content)
    
    
    def translation(self,data):#번역
        papago = papagoapi()
        print(data)
        print(data['text'])
        translation_text = papago.papago_translation(data['text'])
        content = {
            'command':'translation',
            'text' : translation_text
        }
        return self.send_translation(content)
        
        
    
    def messages_to_json(self,messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result
    
    def message_to_json(self,message):
        return {
            'author':message.author.username,
            'content':message.content,
            'timestamp':str(message.timestamp)
        }
    commands = {
        "fetch_messages" : fetch_messages,
         "new_messages" : new_messages,
         "translation" : translation
    }
    
    # websocket 연결
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group / 그룹에 참여
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
            )
        # websocket 연결을 수락 / connect() 메서드 내에서 accept()를 호출하지 않으면 연결이 거부되고 닫힌다.
        self.accept()
        
    # websocket 연결 해제
    def disconnect(self, close_code):
        # Leave room group/ 그룹에서 탈퇴
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, 
            self.channel_name
            )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self,data)
        
        
    def send_chat_message(self,message):
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, 
            {
                "type": "chat_message",
                "message": message
            }
        )
    def send_translation(self,text):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, 
            {
                "type": "translation",
                "message": text
            }
        )


    def send_message(self,message):
        self.send(text_data=json.dumps(message))
        
    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps(message))