# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class NoteAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, text=None, type=None):  # noqa: E501
        """NoteAllOf - a model defined in OpenAPI

        :param text: The text of this NoteAllOf.  # noqa: E501
        :type text: str
        :param type: The type of this NoteAllOf.  # noqa: E501
        :type type: str
        """
        self.openapi_types = {
            'text': str,
            'type': str
        }

        self.attribute_map = {
            'text': 'text',
            'type': 'type'
        }

        self._text = text
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'NoteAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Note_allOf of this NoteAllOf.  # noqa: E501
        :rtype: NoteAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def text(self):
        """Gets the text of this NoteAllOf.

        The content of the note  # noqa: E501

        :return: The text of this NoteAllOf.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this NoteAllOf.

        The content of the note  # noqa: E501

        :param text: The text of this NoteAllOf.
        :type text: str
        """

        self._text = text

    @property
    def type(self):
        """Gets the type of this NoteAllOf.

        The note type  # noqa: E501

        :return: The type of this NoteAllOf.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NoteAllOf.

        The note type  # noqa: E501

        :param type: The type of this NoteAllOf.
        :type type: str
        """
        allowed_values = ["pathology", "phone_call"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type