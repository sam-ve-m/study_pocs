from hashlib import md5

from src.core.entities.address import Address
from src.core.entities.contacts import Contact
from src.core.entities.contacts import ContactParameters
from src.core.entities.email import Email
from src.core.entities.name import Name
from src.core.entities.phones import Phone


def _create_id(contact: ContactParameters) -> str:
    _id = (
        f"{contact.firstName + contact.lastName}:"
        f"{contact.email}:"
        f"{contact.phoneList[0].number}"
    )
    return md5(_id.encode()).hexdigest()


def transform_parameters_to_contact(contact_parameters: ContactParameters) -> Contact:
    contact = Contact(
        contactId=_create_id(contact_parameters),
        name=Name(
            lastName=contact_parameters.lastName,
            firstName=contact_parameters.firstName,
        ),
        email=Email(
            email=contact_parameters.email
        ),
        phoneList=[Phone(
            type=phone.type,
            number=phone.number
        ) for phone in contact_parameters.phoneList],
        address=Address(
            full_address=contact_parameters.address
        )
    )
    return contact
