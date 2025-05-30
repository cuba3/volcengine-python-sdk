# coding: utf-8

"""
    rocketmq

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeInstanceDetailResponse(object):
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
        'basic_info': 'BasicInfoForDescribeInstanceDetailOutput',
        'charge_detail': 'ChargeDetailForDescribeInstanceDetailOutput',
        'connection_info': 'list[ConnectionInfoForDescribeInstanceDetailOutput]',
        'file_reserved_time': 'int'
    }

    attribute_map = {
        'basic_info': 'BasicInfo',
        'charge_detail': 'ChargeDetail',
        'connection_info': 'ConnectionInfo',
        'file_reserved_time': 'FileReservedTime'
    }

    def __init__(self, basic_info=None, charge_detail=None, connection_info=None, file_reserved_time=None, _configuration=None):  # noqa: E501
        """DescribeInstanceDetailResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._basic_info = None
        self._charge_detail = None
        self._connection_info = None
        self._file_reserved_time = None
        self.discriminator = None

        if basic_info is not None:
            self.basic_info = basic_info
        if charge_detail is not None:
            self.charge_detail = charge_detail
        if connection_info is not None:
            self.connection_info = connection_info
        if file_reserved_time is not None:
            self.file_reserved_time = file_reserved_time

    @property
    def basic_info(self):
        """Gets the basic_info of this DescribeInstanceDetailResponse.  # noqa: E501


        :return: The basic_info of this DescribeInstanceDetailResponse.  # noqa: E501
        :rtype: BasicInfoForDescribeInstanceDetailOutput
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        """Sets the basic_info of this DescribeInstanceDetailResponse.


        :param basic_info: The basic_info of this DescribeInstanceDetailResponse.  # noqa: E501
        :type: BasicInfoForDescribeInstanceDetailOutput
        """

        self._basic_info = basic_info

    @property
    def charge_detail(self):
        """Gets the charge_detail of this DescribeInstanceDetailResponse.  # noqa: E501


        :return: The charge_detail of this DescribeInstanceDetailResponse.  # noqa: E501
        :rtype: ChargeDetailForDescribeInstanceDetailOutput
        """
        return self._charge_detail

    @charge_detail.setter
    def charge_detail(self, charge_detail):
        """Sets the charge_detail of this DescribeInstanceDetailResponse.


        :param charge_detail: The charge_detail of this DescribeInstanceDetailResponse.  # noqa: E501
        :type: ChargeDetailForDescribeInstanceDetailOutput
        """

        self._charge_detail = charge_detail

    @property
    def connection_info(self):
        """Gets the connection_info of this DescribeInstanceDetailResponse.  # noqa: E501


        :return: The connection_info of this DescribeInstanceDetailResponse.  # noqa: E501
        :rtype: list[ConnectionInfoForDescribeInstanceDetailOutput]
        """
        return self._connection_info

    @connection_info.setter
    def connection_info(self, connection_info):
        """Sets the connection_info of this DescribeInstanceDetailResponse.


        :param connection_info: The connection_info of this DescribeInstanceDetailResponse.  # noqa: E501
        :type: list[ConnectionInfoForDescribeInstanceDetailOutput]
        """

        self._connection_info = connection_info

    @property
    def file_reserved_time(self):
        """Gets the file_reserved_time of this DescribeInstanceDetailResponse.  # noqa: E501


        :return: The file_reserved_time of this DescribeInstanceDetailResponse.  # noqa: E501
        :rtype: int
        """
        return self._file_reserved_time

    @file_reserved_time.setter
    def file_reserved_time(self, file_reserved_time):
        """Sets the file_reserved_time of this DescribeInstanceDetailResponse.


        :param file_reserved_time: The file_reserved_time of this DescribeInstanceDetailResponse.  # noqa: E501
        :type: int
        """

        self._file_reserved_time = file_reserved_time

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
        if issubclass(DescribeInstanceDetailResponse, dict):
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
        if not isinstance(other, DescribeInstanceDetailResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeInstanceDetailResponse):
            return True

        return self.to_dict() != other.to_dict()
