from sqlalchemy.ext.automap import automap_base
from sqlalchemy import *

from SETTINGS import settings

Base = automap_base()

class ScheduledText(Base):
    __tablename__ = "scheduled_texts"

engine = create_engine(settings['ENGINE_STRING'])
Base.prepare(engine, reflect = True)
