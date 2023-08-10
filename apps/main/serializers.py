from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ['body'] #для отобр одного поля
        # exclude = [''] #кого не хотим отобр