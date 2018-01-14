# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class InlineResponse200(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, dni: int=None):
        """
        InlineResponse200 - a model defined in Swagger

        :param dni: The dni of this InlineResponse200.
        :type dni: int
        """
        self.swagger_types = {
            'dni': int
        }

        self.attribute_map = {
            'dni': 'dni'
        }

        self._dni = dni

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.
        :rtype: InlineResponse200
        """
        return deserialize_model(dikt, cls)

    @property
    def dni(self) -> int:
        """
        Gets the dni of this InlineResponse200.

        :return: The dni of this InlineResponse200.
        :rtype: int
        """
        return self._dni

    @dni.setter
    def dni(self, dni: int):
        """
        Sets the dni of this InlineResponse200.

        :param dni: The dni of this InlineResponse200.
        :type dni: int
        """
        if dni is None:
            raise ValueError("Invalid value for `dni`, must not be `None`")

        self._dni = dni
