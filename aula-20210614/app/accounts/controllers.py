from database import db
from .models import Account, Transaction


def create_account(user_id, data):
    account = Account(
        user_id=user_id,
        name=data.get('name')
    )

    db.session.add(account)
    db.session.commit()

    return account


def create_transaction(data):

    debit_account = Account.query.get(data.get('debit_account_id'))
    credit_account = Account.query.get(data.get('credit_account_id'))
    value = data.get('value')

    make_accounts_transfer(
        debit_account=debit_account,
        credit_account=credit_account,
        value=value
    )

    transaction = Transaction(
        user_id=data.get('user_id'),
        debit_account_id=data.get('debit_account_id'),
        credit_account_id=data.get('credit_account_id'),
        observation=data.get('observation'),
        value=data.get('value')
    )

    db.session.add(transaction)
    db.session.commit()

    return transaction


def make_accounts_transfer(debit_account, credit_account, value):
    debit_account.balance -= value
    credit_account.balance += value

    db.session.add(debit_account)
    db.session.add(credit_account)
