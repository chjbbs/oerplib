# -*- coding: UTF-8 -*-

import unittest

from args import ARGS

import oerplib


class TestDBCreate(unittest.TestCase):

    def setUp(self):
        self.oerp = oerplib.OERP(ARGS.server,
                                 protocol=ARGS.protocol, port=ARGS.port)

    def test_db_create(self):
        res = self.oerp.db.create_and_wait(
                ARGS.super_admin_passwd,
                ARGS.database,
                demo_data=False,
                lang='en_US',
                admin_passwd=ARGS.passwd)
        self.assertIsInstance(res, list)
        self.assertNotEqual(res, list())
        self.assertEqual(res[0], {'login': 'admin', 'password': ARGS.passwd,
                                  'name': "Administrator"})

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
