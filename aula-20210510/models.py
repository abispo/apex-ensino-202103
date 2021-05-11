
from datetime import datetime
from database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Table
from sqlalchemy.orm import relationship

# Tabela associativa entre Post e Tag
posts_tags = Table('tb_posts_tags', Base.metadata,
                   Column('post_id', Integer, ForeignKey('tb_posts.id')),
                   Column('tag_id', Integer, ForeignKey('tb_tags.id'))
                   )


class User(Base):
    # A propriedade __tablename__ serve pra definir o nome da tabela no banco de dados
    # que será mapeada para essa classe
    __tablename__ = 'tb_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50), nullable=False)
    login = Column(String(20), nullable=False)
    passwd = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())

    posts = relationship("Post", back_populates='user')
    profile = relationship("Profile", uselist=False, back_populates='user')

    def __repr__(self):
        return f"User(id={self.id}, email={self.email}, login={self.login})"


class Profile(Base):
    __tablename__ = 'tb_profiles'

    id = Column(Integer, ForeignKey("tb_users.id"), primary_key=True, autoincrement=False)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, onupdate=datetime.utcnow())

    user = relationship("User", uselist=False, back_populates='profile')

# Criar model Post
# O nome da tabela no banco será tb_posts
# Terá um campo chave primária chamado id, auto incremento
# Terá um campo chave estrangeira de nome user_id que vai apontar para o campo id da
# tabela tb_users
# Terá os campos: title(string 100, não nula), body (Text, não nulo) created_at/updated_at


class Post(Base):
    __tablename__ = 'tb_posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('tb_users.id'))
    title = Column(String(50), nullable=False)
    body = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, onupdate=datetime.utcnow())

    user = relationship("User", uselist=False, back_populates='posts')
    tags = relationship("Tag", secondary=posts_tags, back_populates="posts")


class Tag(Base):
    __tablename__ = 'tb_tags'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    posts = relationship("Post", secondary=posts_tags, back_populates="tags")
