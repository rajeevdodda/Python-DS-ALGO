from ecommerce.database import Database

from ecommerce import Products

# d = Database()
p = Products()

database_connection = None


def initialise_database():
    global database_connection
    database_connection = Database()


initialise_database()
print(database_connection.server_ip)
