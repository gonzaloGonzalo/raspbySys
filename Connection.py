from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table, ForeignKey
from sqlalchemy import Integer, String, VARCHAR

engine = create_engine('sqlite:///raspBy.db',
                       echo=True)

metadata = MetaData(bind=engine)



addresses_table = Table('position', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('name', VARCHAR, nullable=False),
                        Column('created_on',  VARCHAR, nullable=False),
                        Column('latitude',  VARCHAR, nullable=False),
                        Column('longitude',  VARCHAR, nullable=False)
                        )

# create an Insert object
#ins = users_table.insert()
# add values to the Insert object
#new_user = ins.values(name="Joe", age=20, password="pass")

# create a database connection
#conn = engine.connect()
# add user to database by executing SQL
#conn.execute(new_user)

metadata.create_all()