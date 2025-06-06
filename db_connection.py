
SQLALCHEMY_DATABASE_URI = "postgresql://fwvision:visi$devpostg$2019@dev-fogwing-vision.southindia.cloudapp.azure.com:6642/fwvisionmaster"

# Explanation of Each Part
# postgresql://
# This specifies the database dialect SQLAlchemy should use, in this case, PostgreSQL.

# fwvision
# The username used to authenticate with the PostgreSQL server.

# visi$devpostg$2019
# The password for the above user. Special characters (like $) are allowed and often need to be URL-encoded in some contexts, though SQLAlchemy typically handles this.

# dev-fogwing-vision.southindia.cloudapp.azure.com
# The host of the PostgreSQL database. This is a domain name pointing to a cloud-hosted server (in this case, probably an Azure VM or managed database).

# 6642
# The port on which the PostgreSQL server is listening. The default for PostgreSQL is 5432, so this is a custom port.

# fwvisionmaster
# The database name to which SQLAlchemy will connect.


# What is a URI?
# A URI is a string of characters used to identify a resource on a network — such as a file, a webpage, or in your case, a database.

# It tells your program:

# What type of resource you're connecting to (e.g., PostgreSQL database)

# Where it is located (e.g., a server or IP)

# How to access it (e.g., with a username and password)