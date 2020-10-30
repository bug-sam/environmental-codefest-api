from api.app import db


class Issue(db.Model):

    __tablename__ = "issues"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    preview = db.Column(db.String(1024))
    message = db.Column(db.String(8192))
    sources = db.Column(db.String(255))

    def __repr__(self):
        return "<User '{}'>".format(self.title)