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


class GetDXPMonthlyRentResponse(object):
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
        'coupon_amount': 'float',
        'currency': 'str',
        'discount_amount': 'float',
        'original_amount': 'float',
        'payable_amount': 'float'
    }

    attribute_map = {
        'coupon_amount': 'CouponAmount',
        'currency': 'Currency',
        'discount_amount': 'DiscountAmount',
        'original_amount': 'OriginalAmount',
        'payable_amount': 'PayableAmount'
    }

    def __init__(self, coupon_amount=None, currency=None, discount_amount=None, original_amount=None, payable_amount=None, _configuration=None):  # noqa: E501
        """GetDXPMonthlyRentResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._coupon_amount = None
        self._currency = None
        self._discount_amount = None
        self._original_amount = None
        self._payable_amount = None
        self.discriminator = None

        if coupon_amount is not None:
            self.coupon_amount = coupon_amount
        if currency is not None:
            self.currency = currency
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if original_amount is not None:
            self.original_amount = original_amount
        if payable_amount is not None:
            self.payable_amount = payable_amount

    @property
    def coupon_amount(self):
        """Gets the coupon_amount of this GetDXPMonthlyRentResponse.  # noqa: E501


        :return: The coupon_amount of this GetDXPMonthlyRentResponse.  # noqa: E501
        :rtype: float
        """
        return self._coupon_amount

    @coupon_amount.setter
    def coupon_amount(self, coupon_amount):
        """Sets the coupon_amount of this GetDXPMonthlyRentResponse.


        :param coupon_amount: The coupon_amount of this GetDXPMonthlyRentResponse.  # noqa: E501
        :type: float
        """

        self._coupon_amount = coupon_amount

    @property
    def currency(self):
        """Gets the currency of this GetDXPMonthlyRentResponse.  # noqa: E501


        :return: The currency of this GetDXPMonthlyRentResponse.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this GetDXPMonthlyRentResponse.


        :param currency: The currency of this GetDXPMonthlyRentResponse.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def discount_amount(self):
        """Gets the discount_amount of this GetDXPMonthlyRentResponse.  # noqa: E501


        :return: The discount_amount of this GetDXPMonthlyRentResponse.  # noqa: E501
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this GetDXPMonthlyRentResponse.


        :param discount_amount: The discount_amount of this GetDXPMonthlyRentResponse.  # noqa: E501
        :type: float
        """

        self._discount_amount = discount_amount

    @property
    def original_amount(self):
        """Gets the original_amount of this GetDXPMonthlyRentResponse.  # noqa: E501


        :return: The original_amount of this GetDXPMonthlyRentResponse.  # noqa: E501
        :rtype: float
        """
        return self._original_amount

    @original_amount.setter
    def original_amount(self, original_amount):
        """Sets the original_amount of this GetDXPMonthlyRentResponse.


        :param original_amount: The original_amount of this GetDXPMonthlyRentResponse.  # noqa: E501
        :type: float
        """

        self._original_amount = original_amount

    @property
    def payable_amount(self):
        """Gets the payable_amount of this GetDXPMonthlyRentResponse.  # noqa: E501


        :return: The payable_amount of this GetDXPMonthlyRentResponse.  # noqa: E501
        :rtype: float
        """
        return self._payable_amount

    @payable_amount.setter
    def payable_amount(self, payable_amount):
        """Sets the payable_amount of this GetDXPMonthlyRentResponse.


        :param payable_amount: The payable_amount of this GetDXPMonthlyRentResponse.  # noqa: E501
        :type: float
        """

        self._payable_amount = payable_amount

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
        if issubclass(GetDXPMonthlyRentResponse, dict):
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
        if not isinstance(other, GetDXPMonthlyRentResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetDXPMonthlyRentResponse):
            return True

        return self.to_dict() != other.to_dict()
