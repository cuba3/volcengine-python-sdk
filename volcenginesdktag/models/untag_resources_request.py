# coding: utf-8

"""
    tag

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UntagResourcesRequest(object):
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
        'resource_trn_list': 'list[str]',
        'tag_keys': 'list[str]'
    }

    attribute_map = {
        'resource_trn_list': 'ResourceTrnList',
        'tag_keys': 'TagKeys'
    }

    def __init__(self, resource_trn_list=None, tag_keys=None, _configuration=None):  # noqa: E501
        """UntagResourcesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._resource_trn_list = None
        self._tag_keys = None
        self.discriminator = None

        if resource_trn_list is not None:
            self.resource_trn_list = resource_trn_list
        if tag_keys is not None:
            self.tag_keys = tag_keys

    @property
    def resource_trn_list(self):
        """Gets the resource_trn_list of this UntagResourcesRequest.  # noqa: E501


        :return: The resource_trn_list of this UntagResourcesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._resource_trn_list

    @resource_trn_list.setter
    def resource_trn_list(self, resource_trn_list):
        """Sets the resource_trn_list of this UntagResourcesRequest.


        :param resource_trn_list: The resource_trn_list of this UntagResourcesRequest.  # noqa: E501
        :type: list[str]
        """

        self._resource_trn_list = resource_trn_list

    @property
    def tag_keys(self):
        """Gets the tag_keys of this UntagResourcesRequest.  # noqa: E501


        :return: The tag_keys of this UntagResourcesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag_keys

    @tag_keys.setter
    def tag_keys(self, tag_keys):
        """Sets the tag_keys of this UntagResourcesRequest.


        :param tag_keys: The tag_keys of this UntagResourcesRequest.  # noqa: E501
        :type: list[str]
        """

        self._tag_keys = tag_keys

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
        if issubclass(UntagResourcesRequest, dict):
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
        if not isinstance(other, UntagResourcesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UntagResourcesRequest):
            return True

        return self.to_dict() != other.to_dict()
