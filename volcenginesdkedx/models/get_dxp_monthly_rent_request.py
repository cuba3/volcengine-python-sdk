# coding: utf-8

"""
    edx

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class GetDXPMonthlyRentRequest(object):
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
        'billing_mode': 'str',
        'buy_duration': 'int',
        'port_type': 'str'
    }

    attribute_map = {
        'billing_mode': 'BillingMode',
        'buy_duration': 'BuyDuration',
        'port_type': 'PortType'
    }

    def __init__(self, billing_mode=None, buy_duration=None, port_type=None, _configuration=None):  # noqa: E501
        """GetDXPMonthlyRentRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._billing_mode = None
        self._buy_duration = None
        self._port_type = None
        self.discriminator = None

        self.billing_mode = billing_mode
        self.buy_duration = buy_duration
        self.port_type = port_type

    @property
    def billing_mode(self):
        """Gets the billing_mode of this GetDXPMonthlyRentRequest.  # noqa: E501


        :return: The billing_mode of this GetDXPMonthlyRentRequest.  # noqa: E501
        :rtype: str
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        """Sets the billing_mode of this GetDXPMonthlyRentRequest.


        :param billing_mode: The billing_mode of this GetDXPMonthlyRentRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and billing_mode is None:
            raise ValueError("Invalid value for `billing_mode`, must not be `None`")  # noqa: E501

        self._billing_mode = billing_mode

    @property
    def buy_duration(self):
        """Gets the buy_duration of this GetDXPMonthlyRentRequest.  # noqa: E501


        :return: The buy_duration of this GetDXPMonthlyRentRequest.  # noqa: E501
        :rtype: int
        """
        return self._buy_duration

    @buy_duration.setter
    def buy_duration(self, buy_duration):
        """Sets the buy_duration of this GetDXPMonthlyRentRequest.


        :param buy_duration: The buy_duration of this GetDXPMonthlyRentRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and buy_duration is None:
            raise ValueError("Invalid value for `buy_duration`, must not be `None`")  # noqa: E501

        self._buy_duration = buy_duration

    @property
    def port_type(self):
        """Gets the port_type of this GetDXPMonthlyRentRequest.  # noqa: E501


        :return: The port_type of this GetDXPMonthlyRentRequest.  # noqa: E501
        :rtype: str
        """
        return self._port_type

    @port_type.setter
    def port_type(self, port_type):
        """Sets the port_type of this GetDXPMonthlyRentRequest.


        :param port_type: The port_type of this GetDXPMonthlyRentRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and port_type is None:
            raise ValueError("Invalid value for `port_type`, must not be `None`")  # noqa: E501

        self._port_type = port_type

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
        if issubclass(GetDXPMonthlyRentRequest, dict):
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
        if not isinstance(other, GetDXPMonthlyRentRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetDXPMonthlyRentRequest):
            return True

        return self.to_dict() != other.to_dict()
