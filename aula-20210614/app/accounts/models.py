from database import db


class Account(db.Model):
    __tablename__ = 'tb_accounts'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('tb_users.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    balance = db.Column(db.Float(), default=0)

    user = db.relationship("User", uselist=False, back_populates="accounts")

    def serialize(self):
        return {
            'name': self.name,
            'balance': self.balance
        }


class Transaction(db.Model):
    __tablename__ = 'tb_transactions'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    debit_account = db.Column(db.Integer(), db.ForeignKey('tb_accounts.id'), nullable=False)
    credit_account = db.Column(db.Integer(), db.ForeignKey('tb_accounts.id'), nullable=False)
    observation = db.Column(db.Text())
    timestamp = db.Column(db.DateTime(), server_default=db.func.now())
