# coding: utf-8

"""
    cloud_detect

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AssertionForGetTaskResultOutput(object):
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
        'condition_message': 'str',
        'result_value': 'str',
        'success': 'bool'
    }

    attribute_map = {
        'condition_message': 'ConditionMessage',
        'result_value': 'ResultValue',
        'success': 'Success'
    }

    def __init__(self, condition_message=None, result_value=None, success=None, _configuration=None):  # noqa: E501
        """AssertionForGetTaskResultOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._condition_message = None
        self._result_value = None
        self._success = None
        self.discriminator = None

        if condition_message is not None:
            self.condition_message = condition_message
        if result_value is not None:
            self.result_value = result_value
        if success is not None:
            self.success = success

    @property
    def condition_message(self):
        """Gets the condition_message of this AssertionForGetTaskResultOutput.  # noqa: E501


        :return: The condition_message of this AssertionForGetTaskResultOutput.  # noqa: E501
        :rtype: str
        """
        return self._condition_message

    @condition_message.setter
    def condition_message(self, condition_message):
        """Sets the condition_message of this AssertionForGetTaskResultOutput.


        :param condition_message: The condition_message of this AssertionForGetTaskResultOutput.  # noqa: E501
        :type: str
        """

        self._condition_message = condition_message

    @property
    def result_value(self):
        """Gets the result_value of this AssertionForGetTaskResultOutput.  # noqa: E501


        :return: The result_value of this AssertionForGetTaskResultOutput.  # noqa: E501
        :rtype: str
        """
        return self._result_value

    @result_value.setter
    def result_value(self, result_value):
        """Sets the result_value of this AssertionForGetTaskResultOutput.


        :param result_value: The result_value of this AssertionForGetTaskResultOutput.  # noqa: E501
        :type: str
        """

        self._result_value = result_value

    @property
    def success(self):
        """Gets the success of this AssertionForGetTaskResultOutput.  # noqa: E501


        :return: The success of this AssertionForGetTaskResultOutput.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this AssertionForGetTaskResultOutput.


        :param success: The success of this AssertionForGetTaskResultOutput.  # noqa: E501
        :type: bool
        """

        self._success = success

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
        if issubclass(AssertionForGetTaskResultOutput, dict):
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
        if not isinstance(other, AssertionForGetTaskResultOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssertionForGetTaskResultOutput):
            return True

        return self.to_dict() != other.to_dict()
