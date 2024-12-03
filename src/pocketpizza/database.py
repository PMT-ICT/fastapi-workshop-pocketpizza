from sqlalchemy import create_engine
from pocketpizza import settings

engine = create_engine(settings.sqlalchemy_url, echo=True)
