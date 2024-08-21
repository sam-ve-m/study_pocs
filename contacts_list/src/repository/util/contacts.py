from src.core.entities.address import Address
from src.core.entities.contacts import Contact
from src.core.entities.email import Email
from src.core.entities.name import Name
from src.core.entities.phones import Phone
from src.core.enum.active import ActiveCondition
from src.core.interfaces.repository.i_mongo_repository import IMongo


class ContactsRepository(IMongo):
    DATABASE: str = "contact_list"
    COLLECTION: str = "contacts"

    @staticmethod
    def _transform_from_json_to_contact(contact_as_json: dict) -> Contact:
        contact = Contact(
            contactId=contact_as_json.get("_id"),
            name=Name(
                firstName=contact_as_json.get("firstName"),
                lastName=contact_as_json.get("lastName"),
            ),
            email=Email(
                email=contact_as_json.get('email')
            ),
            phoneList=[Phone(
                type=phone.get('type'),
                number=phone.get('number')
            ) for phone in contact_as_json.get('phones')],
            address=Address(
                full_address=contact_as_json.get('address')
            )
        )
        return contact
