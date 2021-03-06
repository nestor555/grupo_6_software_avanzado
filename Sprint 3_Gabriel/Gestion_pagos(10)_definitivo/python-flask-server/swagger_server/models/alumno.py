# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Alumno(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, dni: int=None, nombre: str=None, apellidos: str=None, asignatura: str=None):
        """
        Alumno - a model defined in Swagger

        :param dni: The dni of this Alumno.
        :type dni: int
        :param nombre: The nombre of this Alumno.
        :type nombre: str
        :param apellidos: The apellidos of this Alumno.
        :type apellidos: str
        :param asignatura: The asignatura of this Alumno.
        :type asignatura: str
        """
        self.swagger_types = {
            'dni': int,
            'nombre': str,
            'apellidos': str,
            'asignatura': str
        }

        self.attribute_map = {
            'dni': 'dni',
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'asignatura': 'Asignatura'
        }

        self._dni = dni
        self._nombre = nombre
        self._apellidos = apellidos
        self._asignatura = asignatura

    @classmethod
    def from_dict(cls, dikt) -> 'Alumno':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The alumno of this Alumno.
        :rtype: Alumno
        """
        return deserialize_model(dikt, cls)

    @property
    def dni(self) -> int:
        """
        Gets the dni of this Alumno.

        :return: The dni of this Alumno.
        :rtype: int
        """
        return self._dni

    @dni.setter
    def dni(self, dni: int):
        """
        Sets the dni of this Alumno.

        :param dni: The dni of this Alumno.
        :type dni: int
        """

        self._dni = dni

    @property
    def nombre(self) -> str:
        """
        Gets the nombre of this Alumno.

        :return: The nombre of this Alumno.
        :rtype: str
        """
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        """
        Sets the nombre of this Alumno.

        :param nombre: The nombre of this Alumno.
        :type nombre: str
        """

        self._nombre = nombre

    @property
    def apellidos(self) -> str:
        """
        Gets the apellidos of this Alumno.

        :return: The apellidos of this Alumno.
        :rtype: str
        """
        return self._apellidos

    @apellidos.setter
    def apellidos(self, apellidos: str):
        """
        Sets the apellidos of this Alumno.

        :param apellidos: The apellidos of this Alumno.
        :type apellidos: str
        """

        self._apellidos = apellidos

    @property
    def asignatura(self) -> str:
        """
        Gets the asignatura of this Alumno.

        :return: The asignatura of this Alumno.
        :rtype: str
        """
        return self._asignatura

    @asignatura.setter
    def asignatura(self, asignatura: str):
        """
        Sets the asignatura of this Alumno.

        :param asignatura: The asignatura of this Alumno.
        :type asignatura: str
        """

        self._asignatura = asignatura

