from node import Node

STATUS_OK = 200
STATUS_ERROR = 404

DB_SERVER_ADDRESS = '172.112.112.12'
DB_SERVER_PORT = 3306

_DEFAULT_DB_USER = 'root'
_DEFAULT_DB_PASSWORD = 'p'

DB_NODES_NAME = 'nodes'
DB_NODES_USER = _DEFAULT_DB_USER
DB_NODES_PASSWORD = _DEFAULT_DB_PASSWORD

DB_SERVICES_NAME = 'services'
DB_SERVICES_USER = _DEFAULT_DB_USER
DB_SERVICES_PASSWORD = _DEFAULT_DB_PASSWORD

DEFAULT_NODE_PORT = 5000
LIST_OF_NODES = (
    Node('172.113.113.2', DEFAULT_NODE_PORT),
    Node('172.113.113.3', DEFAULT_NODE_PORT),
    Node('172.113.113.4', DEFAULT_NODE_PORT),
    Node('172.113.113.5', DEFAULT_NODE_PORT),
    Node('172.113.113.6', DEFAULT_NODE_PORT)
)