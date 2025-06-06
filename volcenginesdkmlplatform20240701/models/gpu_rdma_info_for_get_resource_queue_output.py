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


class GpuRdmaInfoForGetResourceQueueOutput(object):
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
        'count': 'int',
        'gpu_type': 'str'
    }

    attribute_map = {
        'count': 'Count',
        'gpu_type': 'GpuType'
    }

    def __init__(self, count=None, gpu_type=None, _configuration=None):  # noqa: E501
        """GpuRdmaInfoForGetResourceQueueOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._count = None
        self._gpu_type = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if gpu_type is not None:
            self.gpu_type = gpu_type

    @property
    def count(self):
        """Gets the count of this GpuRdmaInfoForGetResourceQueueOutput.  # noqa: E501


        :return: The count of this GpuRdmaInfoForGetResourceQueueOutput.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this GpuRdmaInfoForGetResourceQueueOutput.


        :param count: The count of this GpuRdmaInfoForGetResourceQueueOutput.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def gpu_type(self):
        """Gets the gpu_type of this GpuRdmaInfoForGetResourceQueueOutput.  # noqa: E501


        :return: The gpu_type of this GpuRdmaInfoForGetResourceQueueOutput.  # noqa: E501
        :rtype: str
        """
        return self._gpu_type

    @gpu_type.setter
    def gpu_type(self, gpu_type):
        """Sets the gpu_type of this GpuRdmaInfoForGetResourceQueueOutput.


        :param gpu_type: The gpu_type of this GpuRdmaInfoForGetResourceQueueOutput.  # noqa: E501
        :type: str
        """

        self._gpu_type = gpu_type

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
        if issubclass(GpuRdmaInfoForGetResourceQueueOutput, dict):
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
        if not isinstance(other, GpuRdmaInfoForGetResourceQueueOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GpuRdmaInfoForGetResourceQueueOutput):
            return True

        return self.to_dict() != other.to_dict()
