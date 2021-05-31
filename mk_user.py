#!/usr/bin/env python3
# -*- coding:utf8 -*-
"""Simple python code that creates users and displays them"""

from app import db
from database import User


def create_my_user(first_name, last_name, hobbies):
    """Creates users"""
    db.session.add(
        User(
            first_name=first_name,
            last_name=last_name,
            hobbies=hobbies
        )
    )
    db.session.commit()


if __name__ == "__main__":
    create_my_user("Laura", "Liber", "Sewing & Gardening")
    users = User.query.all()                                    # SELECT * FROM user;
    print(users)
    create_my_user("John", "Doe", "Playing Golf")
    user = User.query.filter_by(first_name="John").first()      # SELECT * FROM user WHERE first_name="John"
    print(user)
