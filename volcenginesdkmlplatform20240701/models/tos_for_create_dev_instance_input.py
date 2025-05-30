# coding: utf-8

"""
    ml_platform20240701

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class TosForCreateDevInstanceInput(object):
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
        'bucket': 'str',
        'prefix': 'str'
    }

    attribute_map = {
        'bucket': 'Bucket',
        'prefix': 'Prefix'
    }

    def __init__(self, bucket=None, prefix=None, _configuration=None):  # noqa: E501
        """TosForCreateDevInstanceInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bucket = None
        self._prefix = None
        self.discriminator = None

        if bucket is not None:
            self.bucket = bucket
        if prefix is not None:
            self.prefix = prefix

    @property
    def bucket(self):
        """Gets the bucket of this TosForCreateDevInstanceInput.  # noqa: E501


        :return: The bucket of this TosForCreateDevInstanceInput.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this TosForCreateDevInstanceInput.


        :param bucket: The bucket of this TosForCreateDevInstanceInput.  # noqa: E501
        :type: str
        """

        self._bucket = bucket

    @property
    def prefix(self):
        """Gets the prefix of this TosForCreateDevInstanceInput.  # noqa: E501


        :return: The prefix of this TosForCreateDevInstanceInput.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this TosForCreateDevInstanceInput.


        :param prefix: The prefix of this TosForCreateDevInstanceInput.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

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
        if issubclass(TosForCreateDevInstanceInput, dict):
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
        if not isinstance(other, TosForCreateDevInstanceInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TosForCreateDevInstanceInput):
            return True

        return self.to_dict() != other.to_dict()
