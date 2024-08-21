from typing import Dict, Type, Callable, List, Union

from pydantic import BaseModel

from src.core.entities.active import Active
from src.core.entities.address import Address
from src.core.entities.email import Email
from src.core.entities.name import LastName, FirstName
from src.core.entities.phones import PhoneList
from src.repository.util.contacts import ContactsRepository


class UpdateContactRepository(ContactsRepository):
    updates_per_entity_methods: Dict[Type[BaseModel], Callable[[BaseModel], dict]] = {
        FirstName: lambda entity_name: {"firstName": entity_name.firstName},
        LastName: lambda entity_name: {"lastName": entity_name.lastName},
        Address: lambda entity_address: {"address": entity_address.full_address},
        Active: lambda entity_active: {"active": entity_active.is_active},
        Email: lambda entity_email: {"email": entity_email.email},
        PhoneList: lambda entity_phone_list: {"phones": [{
            "type": phone.type.value,
            "number": phone.number,
        } for phone in entity_phone_list.phoneList]},
    }

    def update_contact(self, contact_id: str, updates: List[Union[FirstName, LastName, Email, Address, Active, PhoneList]]) -> bool:
        updates_json = {}
        for unique_update in updates:
            update_method = self.updates_per_entity_methods.get(type(unique_update))
            unique_update_json: dict = update_method(unique_update)
            updates_json.update(unique_update_json)
        return self.update_one(contact_id, updates_json)
