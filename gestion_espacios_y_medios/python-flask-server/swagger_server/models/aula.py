# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Aula(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, codigo_asignatura: int=None, numero_aula: int=None, capacidad: int=None, precio: int=None, tipo: int=None):
        """
        Aula - a model defined in Swagger

        :param codigo_asignatura: The codigo_asignatura of this Aula.
        :type codigo_asignatura: int
        :param numero_aula: The numero_aula of this Aula.
        :type numero_aula: int
        :param capacidad: The capacidad of this Aula.
        :type capacidad: int
        :param precio: The precio of this Aula.
        :type precio: int
        :param tipo: The tipo of this Aula.
        :type tipo: int
        """
        self.swagger_types = {
            'codigo_asignatura': int,
            'numero_aula': int,
            'capacidad': int,
            'precio': int,
            'tipo': int
        }

        self.attribute_map = {
            'codigo_asignatura': 'codigo_asignatura',
            'numero_aula': 'numero_aula',
            'capacidad': 'capacidad',
            'precio': 'precio',
            'tipo': 'tipo'
        }

        self._codigo_asignatura = codigo_asignatura
        self._numero_aula = numero_aula
        self._capacidad = capacidad
        self._precio = precio
        self._tipo = tipo

    @classmethod
    def from_dict(cls, dikt) -> 'Aula':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Aula of this Aula.
        :rtype: Aula
        """
        return deserialize_model(dikt, cls)

    @property
    def codigo_asignatura(self) -> int:
        """
        Gets the codigo_asignatura of this Aula.

        :return: The codigo_asignatura of this Aula.
        :rtype: int
        """
        return self._codigo_asignatura

    @codigo_asignatura.setter
    def codigo_asignatura(self, codigo_asignatura: int):
        """
        Sets the codigo_asignatura of this Aula.

        :param codigo_asignatura: The codigo_asignatura of this Aula.
        :type codigo_asignatura: int
        """

        self._codigo_asignatura = codigo_asignatura

    @property
    def numero_aula(self) -> int:
        """
        Gets the numero_aula of this Aula.

        :return: The numero_aula of this Aula.
        :rtype: int
        """
        return self._numero_aula

    @numero_aula.setter
    def numero_aula(self, numero_aula: int):
        """
        Sets the numero_aula of this Aula.

        :param numero_aula: The numero_aula of this Aula.
        :type numero_aula: int
        """

        self._numero_aula = numero_aula

    @property
    def capacidad(self) -> int:
        """
        Gets the capacidad of this Aula.

        :return: The capacidad of this Aula.
        :rtype: int
        """
        return self._capacidad

    @capacidad.setter
    def capacidad(self, capacidad: int):
        """
        Sets the capacidad of this Aula.

        :param capacidad: The capacidad of this Aula.
        :type capacidad: int
        """

        self._capacidad = capacidad

    @property
    def precio(self) -> int:
        """
        Gets the precio of this Aula.

        :return: The precio of this Aula.
        :rtype: int
        """
        return self._precio

    @precio.setter
    def precio(self, precio: int):
        """
        Sets the precio of this Aula.

        :param precio: The precio of this Aula.
        :type precio: int
        """

        self._precio = precio

    @property
    def tipo(self) -> int:
        """
        Gets the tipo of this Aula.

        :return: The tipo of this Aula.
        :rtype: int
        """
        return self._tipo

    @tipo.setter
    def tipo(self, tipo: int):
        """
        Sets the tipo of this Aula.

        :param tipo: The tipo of this Aula.
        :type tipo: int
        """

        self._tipo = tipo

