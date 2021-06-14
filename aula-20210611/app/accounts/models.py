from database import db
"""
Criar a model Account. Ela deve ter os seguintes campos:
    - id chave primária auto incremento
    - user_id que vai ser chave estrangeira da tabela tb_users(id)
    - name string que não pode ser nula
    - user que vai ser do tipo db.relationship

"""


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
