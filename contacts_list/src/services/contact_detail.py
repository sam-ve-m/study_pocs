from typing import Optional

from pymongo import MongoClient

from src.core.entities.contacts import Contact
from src.core.enum.status import Status
from src.core.interfaces.services.i_detail import IDetail
from src.repository.get_contact_details import GetContactDetailsContactsRepository


class ContactDetail(IDetail):
    def __init__(self, infrastructure: MongoClient):
        self.infrastructure = infrastructure

    def get_detail(self, _id: str) -> dict:
        contact_detail_repository = GetContactDetailsContactsRepository(self.infrastructure)
        contact_detail: Optional[Contact] = contact_detail_repository.get(_id)
        if not contact_detail:
            return {"status": Status.ERROR.value}
        contact_as_json = {
            "contactId": contact_detail.contactId,
            "firstName": contact_detail.name.firstName,
            "lastName": contact_detail.name.lastName,
            "email": contact_detail.email.email,
            "address": contact_detail.address.full_address,
            "phoneList": [{
                "number": phone.number,
                "type": phone.type,
            } for phone in contact_detail.phoneList],
            str(Status.SUCCESS.name).lower(): Status.SUCCESS.value,
        }
        return contact_as_json

