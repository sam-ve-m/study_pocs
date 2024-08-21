from src.core.entities.contacts import Contact
from src.core.interfaces.repository.i_redis_repository import IRedis


class SoftDeleteRegisters(IRedis):
    def verify_if_contact_was_deleted(self, contact: Contact) -> bool:
        contact_id = contact.contactId
        exists = self.verify_if_exists(contact_id)
        return exists

    def delete_contact_from_redis(self, contact: Contact) -> bool:
        contact_id = contact.contactId
        exclude = self.exclude(contact_id)
        return exclude

    def add_contact_to_redis(self, contact: Contact) -> bool:
        contact_id = contact.contactId
        add = self.insert(contact_id)
        return add
