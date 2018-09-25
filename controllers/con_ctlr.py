from controllers.api_client import ApiClient
from views.con_table import ContactsTable


def import_from_db():
    return ContactsTable(ApiClient.get('http://localhost:5000/con_api/get_all'))



