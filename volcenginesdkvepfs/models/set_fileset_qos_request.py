# coding: utf-8

"""
    vepfs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class SetFilesetQosRequest(object):
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
        'file_system_id': 'str',
        'fileset_id': 'str',
        'max_bandwidth': 'int',
        'max_iops': 'int'
    }

    attribute_map = {
        'file_system_id': 'FileSystemId',
        'fileset_id': 'FilesetId',
        'max_bandwidth': 'MaxBandwidth',
        'max_iops': 'MaxIops'
    }

    def __init__(self, file_system_id=None, fileset_id=None, max_bandwidth=None, max_iops=None, _configuration=None):  # noqa: E501
        """SetFilesetQosRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._file_system_id = None
        self._fileset_id = None
        self._max_bandwidth = None
        self._max_iops = None
        self.discriminator = None

        self.file_system_id = file_system_id
        self.fileset_id = fileset_id
        if max_bandwidth is not None:
            self.max_bandwidth = max_bandwidth
        if max_iops is not None:
            self.max_iops = max_iops

    @property
    def file_system_id(self):
        """Gets the file_system_id of this SetFilesetQosRequest.  # noqa: E501


        :return: The file_system_id of this SetFilesetQosRequest.  # noqa: E501
        :rtype: str
        """
        return self._file_system_id

    @file_system_id.setter
    def file_system_id(self, file_system_id):
        """Sets the file_system_id of this SetFilesetQosRequest.


        :param file_system_id: The file_system_id of this SetFilesetQosRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and file_system_id is None:
            raise ValueError("Invalid value for `file_system_id`, must not be `None`")  # noqa: E501

        self._file_system_id = file_system_id

    @property
    def fileset_id(self):
        """Gets the fileset_id of this SetFilesetQosRequest.  # noqa: E501


        :return: The fileset_id of this SetFilesetQosRequest.  # noqa: E501
        :rtype: str
        """
        return self._fileset_id

    @fileset_id.setter
    def fileset_id(self, fileset_id):
        """Sets the fileset_id of this SetFilesetQosRequest.


        :param fileset_id: The fileset_id of this SetFilesetQosRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and fileset_id is None:
            raise ValueError("Invalid value for `fileset_id`, must not be `None`")  # noqa: E501

        self._fileset_id = fileset_id

    @property
    def max_bandwidth(self):
        """Gets the max_bandwidth of this SetFilesetQosRequest.  # noqa: E501


        :return: The max_bandwidth of this SetFilesetQosRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_bandwidth

    @max_bandwidth.setter
    def max_bandwidth(self, max_bandwidth):
        """Sets the max_bandwidth of this SetFilesetQosRequest.


        :param max_bandwidth: The max_bandwidth of this SetFilesetQosRequest.  # noqa: E501
        :type: int
        """

        self._max_bandwidth = max_bandwidth

    @property
    def max_iops(self):
        """Gets the max_iops of this SetFilesetQosRequest.  # noqa: E501


        :return: The max_iops of this SetFilesetQosRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_iops

    @max_iops.setter
    def max_iops(self, max_iops):
        """Sets the max_iops of this SetFilesetQosRequest.


        :param max_iops: The max_iops of this SetFilesetQosRequest.  # noqa: E501
        :type: int
        """

        self._max_iops = max_iops

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
        if issubclass(SetFilesetQosRequest, dict):
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
        if not isinstance(other, SetFilesetQosRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SetFilesetQosRequest):
            return True

        return self.to_dict() != other.to_dict()
