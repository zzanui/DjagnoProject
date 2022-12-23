from django.db import models
from django.conf import settings
from common.models import User



class Room(models.Model):
    name = models.CharField(max_length=10,null=True)
    user= models.ManyToManyField(User,related_name='user_id')

    class Meta:
        db_table = "room"
        
    def __str__(self):
        return self.name

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='author_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, db_column="room_id",null=True)

    def __str__(self):
        return self.content
    
    def last_10_message(self,room_id):
        
        message_range = 10
        
        Message_list = Message.objects.filter(room_id=room_id).order_by('timestamp')
        Message_list=Message_list[len(Message_list)-message_range:]
        return Message_list
    
 
