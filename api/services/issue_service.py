from api.app import db
from api.models.issue import Issue


def save_new_issue(title, preview, message, sources):
    issue = Issue(title=title, preview=preview, message=message, sources=sources)
    db.session.add(issue)
    db.session.commit()


def get_all_issues():
    return Issue.query.all()

def get_issue_by_id(public_id):
    return Issue.query.filter_by(id=public_id).first()