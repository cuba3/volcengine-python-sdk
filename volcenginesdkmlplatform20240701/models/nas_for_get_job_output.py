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


class NasForGetJobOutput(object):
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
        'addr': 'str',
        'file_system_name': 'str',
        'id': 'str',
        'nas_type': 'str',
        'sub_path': 'str'
    }

    attribute_map = {
        'addr': 'Addr',
        'file_system_name': 'FileSystemName',
        'id': 'Id',
        'nas_type': 'NasType',
        'sub_path': 'SubPath'
    }

    def __init__(self, addr=None, file_system_name=None, id=None, nas_type=None, sub_path=None, _configuration=None):  # noqa: E501
        """NasForGetJobOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._addr = None
        self._file_system_name = None
        self._id = None
        self._nas_type = None
        self._sub_path = None
        self.discriminator = None

        if addr is not None:
            self.addr = addr
        if file_system_name is not None:
            self.file_system_name = file_system_name
        if id is not None:
            self.id = id
        if nas_type is not None:
            self.nas_type = nas_type
        if sub_path is not None:
            self.sub_path = sub_path

    @property
    def addr(self):
        """Gets the addr of this NasForGetJobOutput.  # noqa: E501


        :return: The addr of this NasForGetJobOutput.  # noqa: E501
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        """Sets the addr of this NasForGetJobOutput.


        :param addr: The addr of this NasForGetJobOutput.  # noqa: E501
        :type: str
        """

        self._addr = addr

    @property
    def file_system_name(self):
        """Gets the file_system_name of this NasForGetJobOutput.  # noqa: E501


        :return: The file_system_name of this NasForGetJobOutput.  # noqa: E501
        :rtype: str
        """
        return self._file_system_name

    @file_system_name.setter
    def file_system_name(self, file_system_name):
        """Sets the file_system_name of this NasForGetJobOutput.


        :param file_system_name: The file_system_name of this NasForGetJobOutput.  # noqa: E501
        :type: str
        """

        self._file_system_name = file_system_name

    @property
    def id(self):
        """Gets the id of this NasForGetJobOutput.  # noqa: E501


        :return: The id of this NasForGetJobOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NasForGetJobOutput.


        :param id: The id of this NasForGetJobOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def nas_type(self):
        """Gets the nas_type of this NasForGetJobOutput.  # noqa: E501


        :return: The nas_type of this NasForGetJobOutput.  # noqa: E501
        :rtype: str
        """
        return self._nas_type

    @nas_type.setter
    def nas_type(self, nas_type):
        """Sets the nas_type of this NasForGetJobOutput.


        :param nas_type: The nas_type of this NasForGetJobOutput.  # noqa: E501
        :type: str
        """

        self._nas_type = nas_type

    @property
    def sub_path(self):
        """Gets the sub_path of this NasForGetJobOutput.  # noqa: E501


        :return: The sub_path of this NasForGetJobOutput.  # noqa: E501
        :rtype: str
        """
        return self._sub_path

    @sub_path.setter
    def sub_path(self, sub_path):
        """Sets the sub_path of this NasForGetJobOutput.


        :param sub_path: The sub_path of this NasForGetJobOutput.  # noqa: E501
        :type: str
        """

        self._sub_path = sub_path

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
        if issubclass(NasForGetJobOutput, dict):
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
        if not isinstance(other, NasForGetJobOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NasForGetJobOutput):
            return True

        return self.to_dict() != other.to_dict()
