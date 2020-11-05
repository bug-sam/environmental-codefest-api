from api.app import db
from api.models.issue import Issue


def save_new_issue(issuejson):
    issue = Issue(**issuejson)
    db.session.add(issue)
    db.session.commit()
    return issue


def get_all_issues():
    return Issue.query.all()


def get_issue_by_id(public_id):
    return Issue.query.filter_by(id=public_id).first()
