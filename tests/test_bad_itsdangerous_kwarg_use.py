#!/usr/bin/env python

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

import dlint


class TestBadItsDangerousKwargUse(dlint.test.base.BaseTest):

    def test_bad_itsdangerous_kwarg_usage(self):
        python_node = self.get_ast_node(
            """
            import itsdangerous

            itsdangerous.signer.Signer("key", algorithm=itsdangerous.signer.NoneAlgorithm())
            itsdangerous.signer.Signer("key", algorithm=itsdangerous.NoneAlgorithm())
            itsdangerous.Signer("key", algorithm=itsdangerous.NoneAlgorithm())
            itsdangerous.Signer("key", algorithm=itsdangerous.signer.NoneAlgorithm())

            itsdangerous.timed.TimestampSigner("key", algorithm=itsdangerous.signer.NoneAlgorithm())
            itsdangerous.timed.TimestampSigner("key", algorithm=itsdangerous.NoneAlgorithm())
            itsdangerous.TimestampSigner("key", algorithm=itsdangerous.NoneAlgorithm())
            itsdangerous.TimestampSigner("key", algorithm=itsdangerous.signer.NoneAlgorithm())

            itsdangerous.jws.JSONWebSignatureSerializer("key", algorithm_name="none")
            itsdangerous.JSONWebSignatureSerializer("key", algorithm_name="none")
            """
        )

        linter = dlint.linters.BadItsDangerousKwargUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = [
            dlint.linters.base.Flake8Result(
                lineno=4,
                col_offset=0,
                message=dlint.linters.BadItsDangerousKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=5,
                col_offset=0,
                message=dlint.linters.BadItsDangerousKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=6,
                col_offset=0,
                message=dlint.linters.BadItsDangerousKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=7,
                col_offset=0,
                message=dlint.linters.BadItsDangerousKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=9,
                col_offset=0,
                message=dlint.linters.BadItsDangerousKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=10,
                col_offset=0,
                message=dlint.linters.BadItsDangerousKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=11,
                col_offset=0,
                message=dlint.linters.BadItsDangerousKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=12,
                col_offset=0,
                message=dlint.linters.BadItsDangerousKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=14,
                col_offset=0,
                message=dlint.linters.BadItsDangerousKwargUseLinter._error_tmpl
            ),
            dlint.linters.base.Flake8Result(
                lineno=15,
                col_offset=0,
                message=dlint.linters.BadItsDangerousKwargUseLinter._error_tmpl
            ),
        ]

        assert result == expected

    def test_false_positive_in_the_wild(self):
        python_node = self.get_ast_node(
            """
from flask.ext.restful import fields, url_for
from itsdangerous import JSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), unique=True)
    password_hash = db.Column(db.String(256))

    def generate_api_token(self):
        serializer = Serializer(app.config['SECRET_KEY'])
        return serializer.dumps({'id': self.id})

    @staticmethod
    def verify_api_token(token):
        serializer = Serializer(app.config['SECRET_KEY'])
        try:
            data = serializer.loads(token)
        except BadSignature:
            # invalid token
            return None
        return User.query.get(data['id'])

    @property
    def password(self):
        raise AttributeError('password is not readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.email
"""
        )
        linter = dlint.linters.BadItsDangerousKwargUseLinter()
        linter.visit(python_node)

        result = linter.get_results()
        expected = []
        assert result == expected

if __name__ == "__main__":
    unittest.main()
