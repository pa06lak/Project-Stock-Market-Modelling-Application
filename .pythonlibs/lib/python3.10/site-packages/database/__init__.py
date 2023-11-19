import pymongo
import logging

from util import show_loading

# get a new logging utility for current module
_logger = logging.getLogger(__name__)

# database configuration
db_host = 'ds161539.mlab.com'
db_port = 61539
db_name = 'ctr_data'
db_user = 'kevin'
db_password = 'kevin!123'

db_uri = "mongodb://{}:{}@{}:{}/{}?authSource={}".format(
    db_user,
    db_password,
    db_host,
    db_port,
    db_name,
    db_name
)

# get a Mongo Client
def get_client():
    _logger.debug('.get_client. uri: {}'.format(db_uri))
    
    show_loading()
    client = pymongo.MongoClient(db_uri)

    _logger.debug('.get_client client created')

    return client

# get a database PyMongo instance


def get_database():
    client = get_client()

    DB = client[db_name]

    return DB

# insert a new document into a given collection
# return an instance of InsertOneResult
# more info https://api.mongodb.com/python/current/api/pymongo/results.html#pymongo.results.InsertOneResult
def insert_document(collection_name="crs_default", document={}):
    DB = get_database()

    collection = DB[collection_name]

    inserted_document = collection.insert_one(document)

    return inserted_document

# get all collections


def get_collections(options):
    DB = get_database()

    collections = DB.collection_names(include_system_collections=False)

    return collections


def get_documents(collection_name=None, filters={}):
    DB = get_database()

    collection = DB[collection_name]

    documents = collection.find(filters)

    return documents

# execute to Mongo


def execute(query=None):
    if query is None:
        raise('Query param is required')
