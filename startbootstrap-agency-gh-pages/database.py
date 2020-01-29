from model import Base, Story
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db', connect_args={'check_same_thread':False})
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

session.rollback()

def query_all():
	story = session.query(Story).all()
	return story

def story(name,story):
	story_object = Story(
        name=name,
        story=story)
	session.add(story_object)
	session.commit()

print(query_all())


