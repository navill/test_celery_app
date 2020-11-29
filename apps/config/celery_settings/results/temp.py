from celery.backends.database import TaskExtended
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///results.sqlite', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
# print(db_session)

# print(db_session.query(TaskExtended).get(10))
table = db_session.query(TaskExtended).get({'id': 10})
print(table)
# print(table.result)
# print(table.name)
