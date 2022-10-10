from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Document    
        fields = ["id","type","date","value","cpf","card","hour","store_owner","store_name"]
    
    def create(self, validated_data):
        if (validated_data["type"] == "1"):
            validated_data["type"] = "Débito"
        if (validated_data["type"] == "2"):
            validated_data["type"] = "Boleto"
        if (validated_data["type"] == "3"):
            validated_data["type"] = "Financiamento"
        if (validated_data["type"] == "4"):
            validated_data["type"] = "Crédito"
        if (validated_data["type"] == "5"):
            validated_data["type"] = "Recebimento Empréstimo"
        if (validated_data["type"] == "6"):
            validated_data["type"] = "Vendas"
        if (validated_data["type"] == "7"):
            validated_data["type"] = "Recebimento TED"
        if (validated_data["type"] == "8"):
            validated_data["type"] = "Recebimento DOC"
        if (validated_data["type"] == "9"):
            validated_data["type"] = "Aluguel"
        return Document.objects.create(**validated_data)