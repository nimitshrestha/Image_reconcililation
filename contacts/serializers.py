from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'phoneNumber', 'email', 'linkedId', 'linkPrecedence', 'createdAt', 'updatedAt']

class IdentifyResponseSerializer(serializers.Serializer):
    primaryContactId = serializers.IntegerField()
    emails = serializers.ListField(child=serializers.EmailField())
    phoneNumbers = serializers.ListField(child=serializers.CharField())
    secondaryContactIds = serializers.ListField(child=serializers.IntegerField())