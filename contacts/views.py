from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Contact
from .serializers import IdentifyResponseSerializer

class IdentifyView(APIView):
    def post(self, request):
        email = request.data.get('email')
        phone_number = request.data.get('phoneNumber')

        if not email and not phone_number:
            return Response({"error": "Either email or phoneNumber must be provided"}, status=400)

        # Find existing contacts
        existing_contacts = Contact.objects.filter(
            Q(email=email) | Q(phoneNumber=phone_number)
        ).order_by('createdAt')

        if not existing_contacts:
            # Create new primary contact
            new_contact = Contact.objects.create(
                email=email,
                phoneNumber=phone_number,
                linkPrecedence='primary'
            )
            response_data = {
                "primaryContactId": new_contact.id,
                "emails": [email] if email else [],
                "phoneNumbers": [phone_number] if phone_number else [],
                "secondaryContactIds": []
            }
        else:
            primary_contact = existing_contacts.filter(linkPrecedence='primary').first()
            if not primary_contact:
                primary_contact = existing_contacts.first()
                primary_contact.linkPrecedence = 'primary'
                primary_contact.linkedId = None
                primary_contact.save()

            # Create or update secondary contact if new information is provided
            if (email and email not in [c.email for c in existing_contacts]) or \
               (phone_number and phone_number not in [c.phoneNumber for c in existing_contacts]):
                Contact.objects.create(
                    email=email,
                    phoneNumber=phone_number,
                    linkedId=primary_contact,
                    linkPrecedence='secondary'
                )

            # Collect all related contacts
            all_contacts = Contact.objects.filter(
                Q(id=primary_contact.id) |
                Q(linkedId=primary_contact.id)
            )

            response_data = {
                "primaryContactId": primary_contact.id,
                "emails": list(set(c.email for c in all_contacts if c.email)),
                "phoneNumbers": list(set(c.phoneNumber for c in all_contacts if c.phoneNumber)),
                "secondaryContactIds": [c.id for c in all_contacts if c.linkPrecedence == 'secondary']
            }

        serializer = IdentifyResponseSerializer(data=response_data)
        serializer.is_valid(raise_exception=True)
        return Response({"contact": serializer.data})