import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.note import Note  # noqa: E501
from openapi_server.models.text_physical_address_annotations import TextPhysicalAddressAnnotations  # noqa: E501
from openapi_server import util


def create_text_physical_address_annotations(note=None):  # noqa: E501
    """Annotate physical addresses in a clinical note

    Return the physical addresse annotations found in a clinical note # noqa: E501

    :param note: 
    :type note: dict | bytes

    :rtype: TextPhysicalAddressAnnotations
    """
    if connexion.request.is_json:
        note = Note.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
