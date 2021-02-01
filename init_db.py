from server import db
from server.models import Data, Count



db.reflect()
db.drop_all()
db.create_all()

db.session.add(Count(id="count", count=8))

db.session.commit()
