# Dependencies
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

# Create Engine
engine = create_engine("sqlite:///../Resources/mammal_masses.sqlite", echo=False)

# Reflect Database into ORM classes
Base = automap_base()
Base.prepare(engine, reflect=True)
# Display classes/keys
Base.classes.keys()
# ['ea'] ['na']

# Map Europe class
EA = Base.classes.ea

# Map North American class
NA = Base.classes.na

# create a session
session = Session(engine)


# filter North American mammals whose genus is "Antilocapra"
# 'filter' is equivalent to WHERE in SQL
mammals = session.query(NA).filter(NA.genus == 'Antilocapra').all()

# query, loop over and print out animals.
for mammal in mammals:
    print("Family: {0}, Genus: {1}".format(mammal.family, mammal.genus))


# Display table names
inspector = inspect(engine)
inspector.get_table_names()
# ['ea'] ['na']

# Get a list of column names and types
columns = inspector.get_columns('ea')
for column in columns:
    print(column['name'], column["type"])

# id INTEGER
# record_id INTEGER
# continent TEXT
# status TEXT
# sporder TEXT
# family TEXT
# genus TEXT
# species TEXT
# log_mass_g FLOAT
# comb_mass_g FLOAT
# reference TEXT

# one way to query -- limit 100 results -- show all
session.query(EA.sporder, NA.sporder).limit(100).all()

# another way to query using engine.execute and SQL
engine.execute('SELECT * FROM ea LIMIT 5').fetchall()

# query using 'func' to count genus -- show all
session.query(func.count(ea.genus)).all()