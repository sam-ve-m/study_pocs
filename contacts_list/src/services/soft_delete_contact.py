from pymongo import MongoClient
from redis import Redis

from src.core.entities.active import Active
from src.core.enum.status import Status
from src.core.interfaces.services.i_delete import IDelete
from src.repository.get_contact_details import GetContactDetailsContactsRepository
from src.repository.soft_deleted_registers import SoftDeleteRegisters
from src.repository.update_contact import UpdateContactRepository


class DeleteContact(IDelete):
    status_alias = {
        True: Status.SUCCESS.value,
        False: Status.ERROR.value
    }

    def __init__(
            self,
            mongo_infrastructure: MongoClient,
            redis_infrastructure: Redis,
    ):
        self.mongo_infrastructure = mongo_infrastructure
        self.redis_repository = SoftDeleteRegisters(redis_infrastructure)

    def delete(self, contact_id: str) -> dict:
        update_repository = UpdateContactRepository(self.mongo_infrastructure)
        mongo_repository = GetContactDetailsContactsRepository(self.mongo_infrastructure)
        contact = mongo_repository.get(contact_id)
        if not contact:
            return {'status': self.status_alias.get(False)}
        add_to_redis = self.redis_repository.add_contact_to_redis(contact)
        update_repository.update_contact(contact_id, [Active(is_active=False)])
        return {'status': self.status_alias.get(update_repository and add_to_redis)}
