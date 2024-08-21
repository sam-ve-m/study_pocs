from typing import List, Optional
from pymongo import MongoClient

from src.core.entities.contacts import Contact
from src.core.enum.status import Status
from src.core.interfaces.services.i_list import IList
from src.repository.get_contact_list import GetContactListContactsRepository


class ListsContacts(IList):

    def __init__(self, infrastructure: MongoClient):
        self.infrastructure = infrastructure

    def get_list(self, optional_filter: Optional[dict] = {}) -> dict:
        contacts_repository = GetContactListContactsRepository(self.infrastructure)
        list_of_contacts: List[Contact] = contacts_repository.get(optional_filter)
        list_of_contacts_return = [{
            "contactId": contact.contactId,
            "firstName": contact.name.firstName,
            "lastName": contact.name.lastName,
            "email": contact.email.email,
            "phoneList": [{
                "number": phone.number,
                "type": phone.type,
            } for phone in contact.phoneList]
        } for contact in list_of_contacts]
        if not list_of_contacts_return:
            return {'status': Status.ERROR.value}
        return {'contactsList': list_of_contacts_return, 'status': Status.SUCCESS.value}
