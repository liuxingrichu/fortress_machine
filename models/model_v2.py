#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import Column, Integer, String, ForeignKey, \
    UniqueConstraint, Table, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_utils import ChoiceType

Base = declarative_base()

bindhost_m2m_hostgroup = Table('bindhost_m2m_hostgroup', Base.metadata,
                               Column('bindhost_id', Integer,
                                      ForeignKey('bind_host.id')),
                               Column('hostgroup_id', Integer,
                                      ForeignKey('host_group.id'))
                               )

user_m2m_bindhost = Table('user_m2m_bindhost', Base.metadata,
                          Column('fortress_user_id', Integer,
                                 ForeignKey('fortress_user.id')),
                          Column('bindhost_id', Integer,
                                 ForeignKey('bind_host.id'))
                          )

user_m2m_hostgroup = Table('user_m2m_hostgroup', Base.metadata,
                           Column('fortress_user_id', Integer,
                                  ForeignKey('fortress_user.id')),
                           Column('hostgroup_id', Integer,
                                  ForeignKey('host_group.id'))
                           )


class BindHost(Base):
    '''
    192.168.1.10 web
    192.168.1.11 mysql
    '''
    __tablename__ = 'bind_host'
    # 联合唯一
    __table_args__ = (UniqueConstraint('host_id', 'remoteuser_id',
                                       name='_host_remoteuser_uc'),)
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer, ForeignKey('host.id'))
    remoteuser_id = Column(Integer, ForeignKey('remote_user.id'))

    host = relationship('Host', backref='bind_hosts')
    remote_user = relationship('RemoteUser', backref='bind_remote_users')

    def __repr__(self):
        return '<%s -- %s>' % (self.host.id,
                               self.remote_user.username)


class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(64))
    ip = Column(String(64), unique=True)
    port = Column(Integer, default=22)

    def __repr__(self):
        return self.hostname


class HostGroup(Base):
    __tablename__ = 'host_group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    bind_hosts = relationship('BindHost', secondary='bindhost_m2m_hostgroup',
                              backref='hostgroups')

    def __repr__(self):
        return self.name


class RemoteUser(Base):
    __tablename__ = 'remote_user'
    # 联合唯一
    __table_args__ = (UniqueConstraint('auth_type', 'username', 'password',
                                       name='type_user_passwd_uc'),)

    id = Column(Integer, primary_key=True)
    AuthTypes = [
        ('ssh-password', 'SSH/Password'),
        ('ssh-type', 'SSH/KEY'),
    ]
    # 联合唯一的数据内容必须为非空
    auth_type = Column(String(64), ChoiceType(AuthTypes), nullable=False)
    username = Column(String(64), nullable=False)
    password = Column(String(128), nullable=False)

    def __repr__(self):
        return self.username


class FortressUser(Base):
    __tablename__ = 'fortress_user'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    password = Column(String(128))
    bind_hosts = relationship('BindHost', secondary='user_m2m_bindhost',
                              backref='fortress_users')
    host_groups = relationship('HostGroup', secondary='user_m2m_hostgroup',
                               backref='fortress_users')

    def __repr__(self):
        return self.username


class AuditLog(Base):
    __tablename__ = 'audit_log'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('fortress_user.id'))
    bind_host_id = Column(Integer, ForeignKey('bind_host.id'))
    action_choices = [
        (u'cmd', u'CMD'),
        (u'login', u'Login'),
        (u'logout', u'Logout'),
    ]
    action_type = Column(ChoiceType(action_choices))
    cmd = Column(String(255))
    date = Column(DateTime)

    fortress_user = relationship("FortressUser")
    bind_host = relationship("BindHost")
