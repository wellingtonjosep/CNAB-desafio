from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Document    
        fields = ["id","type","date","value","cpf","card","hour","store_owner","store_name"]
    
    def create(self, validated_data):
        print(validated_data)
        return Document.objects.create(**validated_data)