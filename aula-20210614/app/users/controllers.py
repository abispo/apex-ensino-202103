from .models import User, Profile
from database import db


def get_all_users():
    # filter_by -> WHERE (SQL)
    return User.query.filter_by(is_active=True).all()


def get_user_by_id(user_id):
    # get() faz a consulta do valor na coluna chave primária
    return User.query.get(user_id)


def create_user(data):
    user = User(email=data.get('email'), password=data.get('password'))
    # user = User(**data)

    db.session.add(user)
    db.session.commit()

    return user


def delete_user(id):
    user = User.query.get(id)

    user.is_active = False

    db.session.add(user)
    db.session.commit()

    return user


def update_user_profile(profile_id, data):
    profile = Profile.query.get(profile_id)

    profile.first_name = data.get('first_name')
    profile.last_name = data.get('last_name')

    db.session.add(profile)
    db.session.commit()

    return profile
