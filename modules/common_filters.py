# _*_coding:utf-8_*_

from models import model_v2
from modules.db_conn import engine, session
from modules.utils import print_err


def bind_hosts_filter(vals):
    print('**>', vals.get('bind_hosts'))
    bind_hosts = session.query(model_v2.BindHost).filter(
        model_v2.Host.hostname.in_(vals.get('bind_hosts'))).all()
    if not bind_hosts:
        print_err(
            "none of [%s] exist in bind_host table." % vals.get('bind_hosts'),
            quit=True)
    return bind_hosts


def fortress_user_filter(vals):
    fortress_users = session.query(model_v2.FortressUser).filter(
        model_v2.FortressUser.username.in_(vals.get('fortress_user'))
        ).all()
    if not fortress_users:
        print_err("none of [%s] exist in user_profile table." % vals.get(
            'fortress_user'), quit=True)
    return fortress_users
