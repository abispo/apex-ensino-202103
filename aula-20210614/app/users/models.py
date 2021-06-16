from database import db
from sqlalchemy import event


class User(db.Model):
    __tablename__ = 'tb_users'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean(), default=True)

    profile = db.relationship("Profile", uselist=False, back_populates="user")
    accounts = db.relationship("Account", back_populates="user")
    transactions = db.relationship("Transaction", back_populates="user")

    def serialize(self, full=False):

        dict_fields = {
            'id': self.id,
            'email': self.email,
            'is_active': self.is_active
        }

        if full:
            dict_fields.update({
                # como profile é o objeto relacionado a User, temos acesso aos atributos
                # e métodos normalmente
                'profile': self.profile.serialize(),
                'accounts': [account.serialize() for account in self.accounts]
            })

        return dict_fields


class Profile(db.Model):
    __tablename__ = 'tb_profiles'

    id = db.Column(db.Integer(), db.ForeignKey('tb_users.id'), primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))

    user = db.relationship("User", uselist=False, back_populates="profile")

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name
        }


@event.listens_for(User, 'after_insert')
def create_profile_after_user_save(mapper, connection, target):     # target = instancia de User
    profile = Profile()
    profile.user = target

    db.session.add(profile)
