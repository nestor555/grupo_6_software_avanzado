# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.dni import Dni
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAlumnoController(BaseTestCase):
    """ AlumnoController integration test stubs """

    def test_alumno_post(self):
        """
        Test case for alumno_post

        Crea un alumno
        """
        dni = Dni()
        response = self.client.open('/cobros/alumno',
                                    method='POST',
                                    data=json.dumps(dni),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
