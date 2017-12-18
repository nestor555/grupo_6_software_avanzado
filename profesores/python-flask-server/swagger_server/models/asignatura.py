# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Asignatura(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id: int=None, dni_profesor: int=None, nombre: str=None, departamento: str=None):
        """
        Asignatura - a model defined in Swagger

        :param id: The id of this Asignatura.
        :type id: int
        :param dni_profesor: The dni_profesor of this Asignatura.
        :type dni_profesor: int
        :param nombre: The nombre of this Asignatura.
        :type nombre: str
        :param departamento: The departamento of this Asignatura.
        :type departamento: str
        """
        self.swagger_types = {
            'id': int,
            'dni_profesor': int,
            'nombre': str,
            'departamento': str
        }

        self.attribute_map = {
            'id': 'id',
            'dni_profesor': 'dniProfesor',
            'nombre': 'nombre',
            'departamento': 'departamento'
        }

        self._id = id
        self._dni_profesor = dni_profesor
        self._nombre = nombre
        self._departamento = departamento

    @classmethod
    def from_dict(cls, dikt) -> 'Asignatura':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Asignatura of this Asignatura.
        :rtype: Asignatura
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """
        Gets the id of this Asignatura.

        :return: The id of this Asignatura.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """
        Sets the id of this Asignatura.

        :param id: The id of this Asignatura.
        :type id: int
        """

        self._id = id

    @property
    def dni_profesor(self) -> int:
        """
        Gets the dni_profesor of this Asignatura.

        :return: The dni_profesor of this Asignatura.
        :rtype: int
        """
        return self._dni_profesor

    @dni_profesor.setter
    def dni_profesor(self, dni_profesor: int):
        """
        Sets the dni_profesor of this Asignatura.

        :param dni_profesor: The dni_profesor of this Asignatura.
        :type dni_profesor: int
        """

        self._dni_profesor = dni_profesor

    @property
    def nombre(self) -> str:
        """
        Gets the nombre of this Asignatura.

        :return: The nombre of this Asignatura.
        :rtype: str
        """
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        """
        Sets the nombre of this Asignatura.

        :param nombre: The nombre of this Asignatura.
        :type nombre: str
        """

        self._nombre = nombre

    @property
    def departamento(self) -> str:
        """
        Gets the departamento of this Asignatura.

        :return: The departamento of this Asignatura.
        :rtype: str
        """
        return self._departamento

    @departamento.setter
    def departamento(self, departamento: str):
        """
        Sets the departamento of this Asignatura.

        :param departamento: The departamento of this Asignatura.
        :type departamento: str
        """

        self._departamento = departamento

