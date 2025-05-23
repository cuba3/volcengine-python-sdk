# coding: utf-8

"""
    cloud_trail

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class RelatedResourceForLookupEventsOutput(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'integrated_trn': 'str',
        'resource_id': 'str',
        'resource_type': 'str',
        'resource_type_display': 'str',
        'service_code': 'str',
        'source_type': 'str'
    }

    attribute_map = {
        'integrated_trn': 'IntegratedTrn',
        'resource_id': 'ResourceID',
        'resource_type': 'ResourceType',
        'resource_type_display': 'ResourceTypeDisplay',
        'service_code': 'ServiceCode',
        'source_type': 'SourceType'
    }

    def __init__(self, integrated_trn=None, resource_id=None, resource_type=None, resource_type_display=None, service_code=None, source_type=None, _configuration=None):  # noqa: E501
        """RelatedResourceForLookupEventsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._integrated_trn = None
        self._resource_id = None
        self._resource_type = None
        self._resource_type_display = None
        self._service_code = None
        self._source_type = None
        self.discriminator = None

        if integrated_trn is not None:
            self.integrated_trn = integrated_trn
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_type_display is not None:
            self.resource_type_display = resource_type_display
        if service_code is not None:
            self.service_code = service_code
        if source_type is not None:
            self.source_type = source_type

    @property
    def integrated_trn(self):
        """Gets the integrated_trn of this RelatedResourceForLookupEventsOutput.  # noqa: E501


        :return: The integrated_trn of this RelatedResourceForLookupEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._integrated_trn

    @integrated_trn.setter
    def integrated_trn(self, integrated_trn):
        """Sets the integrated_trn of this RelatedResourceForLookupEventsOutput.


        :param integrated_trn: The integrated_trn of this RelatedResourceForLookupEventsOutput.  # noqa: E501
        :type: str
        """

        self._integrated_trn = integrated_trn

    @property
    def resource_id(self):
        """Gets the resource_id of this RelatedResourceForLookupEventsOutput.  # noqa: E501


        :return: The resource_id of this RelatedResourceForLookupEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this RelatedResourceForLookupEventsOutput.


        :param resource_id: The resource_id of this RelatedResourceForLookupEventsOutput.  # noqa: E501
        :type: str
        """

        self._resource_id = resource_id

    @property
    def resource_type(self):
        """Gets the resource_type of this RelatedResourceForLookupEventsOutput.  # noqa: E501


        :return: The resource_type of this RelatedResourceForLookupEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this RelatedResourceForLookupEventsOutput.


        :param resource_type: The resource_type of this RelatedResourceForLookupEventsOutput.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def resource_type_display(self):
        """Gets the resource_type_display of this RelatedResourceForLookupEventsOutput.  # noqa: E501


        :return: The resource_type_display of this RelatedResourceForLookupEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._resource_type_display

    @resource_type_display.setter
    def resource_type_display(self, resource_type_display):
        """Sets the resource_type_display of this RelatedResourceForLookupEventsOutput.


        :param resource_type_display: The resource_type_display of this RelatedResourceForLookupEventsOutput.  # noqa: E501
        :type: str
        """

        self._resource_type_display = resource_type_display

    @property
    def service_code(self):
        """Gets the service_code of this RelatedResourceForLookupEventsOutput.  # noqa: E501


        :return: The service_code of this RelatedResourceForLookupEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._service_code

    @service_code.setter
    def service_code(self, service_code):
        """Sets the service_code of this RelatedResourceForLookupEventsOutput.


        :param service_code: The service_code of this RelatedResourceForLookupEventsOutput.  # noqa: E501
        :type: str
        """

        self._service_code = service_code

    @property
    def source_type(self):
        """Gets the source_type of this RelatedResourceForLookupEventsOutput.  # noqa: E501


        :return: The source_type of this RelatedResourceForLookupEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this RelatedResourceForLookupEventsOutput.


        :param source_type: The source_type of this RelatedResourceForLookupEventsOutput.  # noqa: E501
        :type: str
        """

        self._source_type = source_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(RelatedResourceForLookupEventsOutput, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RelatedResourceForLookupEventsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RelatedResourceForLookupEventsOutput):
            return True

        return self.to_dict() != other.to_dict()
