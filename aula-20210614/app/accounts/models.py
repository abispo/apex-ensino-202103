from database import db


class Account(db.Model):
    __tablename__ = 'tb_accounts'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('tb_users.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    balance = db.Column(db.Float(), default=0)

    user = db.relationship("User", uselist=False, back_populates="accounts")
    transactions = db.relationship("Transaction", back_populates="")

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'balance': self.balance
        }


class Transaction(db.Model):
    __tablename__ = 'tb_transactions'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('tb_users.id'), nullable=True)
    debit_account_id = db.Column(db.Integer(), db.ForeignKey('tb_accounts.id'), nullable=False)
    credit_account_id = db.Column(db.Integer(), db.ForeignKey('tb_accounts.id'), nullable=False)
    value = db.Column(db.Float(), default=0)
    observation = db.Column(db.Text())
    timestamp = db.Column(db.DateTime(), server_default=db.func.now())

    user = db.relationship("User", uselist=False, back_populates="transactions")
    debit_account = db.relationship("Account", uselist=False, back_populates="transactions")
    credit_account = db.relationship("Account", uselist=False, back_populates="transactions")

    def serialize(self):
        return {
            'id': self.id,
            'user': self.user.email,
            'debit_account_id': self.debit_account_id,
            'credit_account_id': self.credit_account_id,
            'value': self.value,
            'observation': self.observation,
            'timestamp': self.timestamp
        }
