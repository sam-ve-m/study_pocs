from fastapi import APIRouter

from src.core.entities.contacts import ContactParameters, ContactOptionalParameters
from src.core.interfaces.services.i_delete import IDelete
from src.core.interfaces.services.i_detail import IDetail
from src.core.interfaces.services.i_list import IList
from src.core.interfaces.services.i_register import IRegister
from src.core.interfaces.services.i_update import IUpdate
from src.infrastructure.mongo import MongoDBInfrastructure
from src.infrastructure.redis import RedisKeyDBInfrastructure
from src.services.contact_detail import ContactDetail
from src.services.count_contact import CountContacts
from src.services.list_contacts import ListsContacts
from src.services.register_contact import RegisterContact
from src.services.soft_delete_contact import DeleteContact
from src.services.update_contact import UpdateContact
from src.services.utils.env_config import config

route = APIRouter(prefix=config("ROUTERS_PREFIX"))


@route.post("/register")
def register_contact(contact: ContactParameters):
    mongo_connection = MongoDBInfrastructure.get_singleton_connection()
    redis_connection = RedisKeyDBInfrastructure.get_singleton_connection()
    register_service: IRegister = RegisterContact(mongo_connection, redis_connection)
    register_return = register_service.register(contact)
    return register_return


@route.get("/contacts")
def lists_contacts():
    mongo_connection = MongoDBInfrastructure.get_singleton_connection()
    list_contact_service: IList = ListsContacts(mongo_connection)
    contacts_list = list_contact_service.get_list()
    return contacts_list


@route.get("/count")
def lists_phones():
    mongo_connection = MongoDBInfrastructure.get_singleton_connection()
    count_contact_service: IList = CountContacts(mongo_connection)
    contacts_list = count_contact_service.get_list()
    return contacts_list


@route.get("/contact/{_id}")
def contact_detail(_id: str):
    mongo_connection = MongoDBInfrastructure.get_singleton_connection()
    get_contact_detail_service: IDetail = ContactDetail(mongo_connection)
    contact_details = get_contact_detail_service.get_detail(_id)
    return contact_details


@route.put("/edit/{_id}")
def contact_update(_id: str, updates: ContactOptionalParameters):
    mongo_connection = MongoDBInfrastructure.get_singleton_connection()
    get_contact_update_service: IUpdate = UpdateContact(mongo_connection)
    contact_updates = get_contact_update_service.update(_id, updates)
    return contact_updates


@route.delete("/remove/{_id}")
def delete_contact(_id: str):
    mongo_connection = MongoDBInfrastructure.get_singleton_connection()
    redis_connection = RedisKeyDBInfrastructure.get_singleton_connection()
    get_contact_delete_service: IDelete = DeleteContact(mongo_connection, redis_connection)
    contact_deleted = get_contact_delete_service.delete(_id)
    return contact_deleted

    
@route.get("/contacts/{letter}")
def list_contact_by_letter(letter: str):
    mongo_connection = MongoDBInfrastructure.get_singleton_connection()
    list_contact_service: IList = ListsContacts(mongo_connection)
    filter_for_letter = {"firstName": {"$regex": f"^{letter.upper()}|^{letter.lower()}"}}
    contacts_list_for_letter = list_contact_service.get_list(filter_for_letter)
    return contacts_list_for_letter
