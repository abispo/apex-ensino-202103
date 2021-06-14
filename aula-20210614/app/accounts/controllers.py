from database import db
from .models import Account


def create_account(user_id, data):
    account = Account(
        user_id=user_id,
        name=data.get('name')
    )

    db.session.add(account)
    db.session.commit()

    return account
