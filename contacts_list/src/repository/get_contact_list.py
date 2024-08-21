from typing import List, Iterator, Optional

from src.core.entities.contacts import Contact
from src.core.enum.active import ActiveCondition
from src.repository.util.contacts import ContactsRepository


class GetContactListContactsRepository(ContactsRepository):
    def get(self, optional_filter: Optional[dict] = {}) -> List[Contact]:
        list_of_contacts: Iterator[dict] = self.find_all({**optional_filter, **ActiveCondition.ACTIVE.value})
        list_of_contacts_return = [
            self._transform_from_json_to_contact(contact_as_json)
            for contact_as_json in list_of_contacts
        ]
        return list_of_contacts_return

