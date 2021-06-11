# coding: utf-8
from sqlalchemy import ARRAY, Boolean, Column, DateTime, Integer, JSON, String, Table, text
from sqlalchemy.dialects.postgresql import INET
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Client(Base):
    __tablename__ = 'client'

    client_id = Column(String(255), primary_key=True)
    resource_ids = Column(String(255))
    client_secret = Column(String(255))
    scope = Column(String(255))
    authorized_grant_types = Column(String(255))
    web_server_redirect_uri = Column(String(255))
    authorities = Column(String(255))
    access_token_validity = Column(Integer)
    refresh_token_validity = Column(Integer)
    additional_information = Column(String(4096))
    autoapprove = Column(Boolean)
    created_at = Column(DateTime(True), server_default=text("CURRENT_TIMESTAMP"))


class OauthAccessToken(Base):
    __tablename__ = 'oauth_access_token'

    authentication_id = Column(String(255), primary_key=True)
    user_name = Column(String(255))
    client_id = Column(String(255))
    token_type = Column(String(40))
    access_token = Column(String(255))
    refresh_token = Column(String(255))
    authentication = Column(JSON)
    created_at = Column(DateTime(True), server_default=text("CURRENT_TIMESTAMP"))


t_oauth_approvals = Table(
    'oauth_approvals', metadata,
    Column('user_id', String(255), server_default=text("NULL::character varying")),
    Column('client_id', String(255), server_default=text("NULL::character varying")),
    Column('scope', String(255), server_default=text("NULL::character varying")),
    Column('status', String(10), server_default=text("NULL::character varying")),
    Column('expires_at', DateTime, server_default=text("CURRENT_TIMESTAMP")),
    Column('last_modified_at', DateTime, server_default=text("CURRENT_TIMESTAMP"))
)


class OauthCode(Base):
    __tablename__ = 'oauth_code'

    code = Column(String(255), primary_key=True)
    authentication = Column(JSON)
    created_at = Column(DateTime(True), server_default=text("CURRENT_TIMESTAMP"))


class OauthRefreshToken(Base):
    __tablename__ = 'oauth_refresh_token'

    token_id = Column(String(255), primary_key=True)
    token = Column(String(255))
    authentication = Column(JSON)
    created_at = Column(DateTime(True), server_default=text("CURRENT_TIMESTAMP"))


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    last_login = Column(DateTime)
    first_name = Column(String(30))
    last_name = Column(String(150))
    email = Column(String(255))
    phone = Column(String(255))
    ip_whitelist = Column(ARRAY(INET()))
    enable_ip_filter = Column(Boolean, nullable=False)
    is_active_bool = Column('is_active bool', Boolean, nullable=False)
    created_at = Column(DateTime(True), server_default=text("CURRENT_TIMESTAMP"))
