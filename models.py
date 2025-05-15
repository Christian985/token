from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///database.db')
SessionLocalExemplo = sessionmaker(bind=engine)


class UsuarioExemplo(Base):
    __tablename__ = 'usuarios_exemplo'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    senha_hash = Column(String, nullable=False)
    papel = Column(String, nullable=False)

class NotasExemplo(Base):
    __tablename__ = 'notas_exemplo'
    id = Column(Integer, primary_key=True)
    conteudo = Column(String, nullable=False)
    # user_id = Column(Integer, ForeignKey('usuarios_exemplo.id')) # Poderia ter para associar

Base.metadata.create_all(engine)  # Cria as tabelas