from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView, Response
# Create your views here.

from .serializers import DocumentSerializer

class FileUploadView(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request, filename, format=None):
        file = request.FILES["file"].read().decode().split("\n")
        if not (file):
            return Response(data={"error": "File not found"},status=400)
        data = []
        for item in file:  
            serializer = DocumentSerializer( data={"type": item[0],"date": item[1:9], "value": item[9:19],"cpf": item[19:30], "card": item[30:42], "hour": item[42:48], "store_owner": item[48:62], "store_name": item[62:81],})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data.append(serializer.data)

        return Response(data=data,status=201)