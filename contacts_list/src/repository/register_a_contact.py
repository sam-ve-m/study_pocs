from src.core.entities.contacts import Contact
from src.core.enum.active import ActiveCondition
from src.repository.util.contacts import ContactsRepository


class RegisterContactsRepository(ContactsRepository):
    def register(self, contact: Contact) -> bool:
        contact_as_json = {
            "_id": contact.contactId,
            "firstName": contact.name.firstName,
            "lastName": contact.name.lastName,
            "email": contact.email.email,
            "address": contact.address.full_address,
            "phones": [{
                "type": phone.type.value,
                "number": phone.number,
            } for phone in contact.phoneList],
            **ActiveCondition.ACTIVE.value,
        }
        insert_status = self.insert_one(contact_as_json)
        return insert_status

