from django.test import TestCase
from documents.models import Document

class DocumentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.document_data = {
            "type": "1",
            "date": "20210301",
            "value": "0000014200",
            "cpf": "09620676017",
            "card": "4753****3153",
            "hour": "153453",
            "store_owner": "JOÃO MACEDO",
            "store_name": "BAR DO JOÃO"
        }
    
    def test_document_fields(self):
        self.document = Document.objects.create(**self.document_data)

        self.assertEqual(self.document.type, self.document_data["type"])
        self.assertEqual(self.document.date, self.document_data["date"])
        self.assertEqual(self.document.value, self.document_data["value"])
        self.assertEqual(self.document.cpf, self.document_data["cpf"])
        self.assertEqual(self.document.card, self.document_data["card"])
        self.assertEqual(self.document.hour, self.document_data["hour"])
        self.assertEqual(self.document.store_owner, self.document_data["store_owner"])
        self.assertEqual(self.document.store_name, self.document_data["store_name"])