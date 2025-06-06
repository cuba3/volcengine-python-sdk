# coding: utf-8

"""
    vefaas

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ScaleStrategyForListFunctionElasticScaleStrategyOutput(object):
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
        'create_time': 'str',
        'rules': 'list[RuleForListFunctionElasticScaleStrategyOutput]',
        'type': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'create_time': 'CreateTime',
        'rules': 'Rules',
        'type': 'Type',
        'update_time': 'UpdateTime'
    }

    def __init__(self, create_time=None, rules=None, type=None, update_time=None, _configuration=None):  # noqa: E501
        """ScaleStrategyForListFunctionElasticScaleStrategyOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create_time = None
        self._rules = None
        self._type = None
        self._update_time = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if rules is not None:
            self.rules = rules
        if type is not None:
            self.type = type
        if update_time is not None:
            self.update_time = update_time

    @property
    def create_time(self):
        """Gets the create_time of this ScaleStrategyForListFunctionElasticScaleStrategyOutput.  # noqa: E501


        :return: The create_time of this ScaleStrategyForListFunctionElasticScaleStrategyOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ScaleStrategyForListFunctionElasticScaleStrategyOutput.


        :param create_time: The create_time of this ScaleStrategyForListFunctionElasticScaleStrategyOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def rules(self):
        """Gets the rules of this ScaleStrategyForListFunctionElasticScaleStrategyOutput.  # noqa: E501


        :return: The rules of this ScaleStrategyForListFunctionElasticScaleStrategyOutput.  # noqa: E501
        :rtype: list[RuleForListFunctionElasticScaleStrategyOutput]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this ScaleStrategyForListFunctionElasticScaleStrategyOutput.


        :param rules: The rules of this ScaleStrategyForListFunctionElasticScaleStrategyOutput.  # noqa: E501
        :type: list[RuleForListFunctionElasticScaleStrategyOutput]
        """

        self._rules = rules

    @property
    def type(self):
        """Gets the type of this ScaleStrategyForListFunctionElasticScaleStrategyOutput.  # noqa: E501


        :return: The type of this ScaleStrategyForListFunctionElasticScaleStrategyOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ScaleStrategyForListFunctionElasticScaleStrategyOutput.


        :param type: The type of this ScaleStrategyForListFunctionElasticScaleStrategyOutput.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def update_time(self):
        """Gets the update_time of this ScaleStrategyForListFunctionElasticScaleStrategyOutput.  # noqa: E501


        :return: The update_time of this ScaleStrategyForListFunctionElasticScaleStrategyOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ScaleStrategyForListFunctionElasticScaleStrategyOutput.


        :param update_time: The update_time of this ScaleStrategyForListFunctionElasticScaleStrategyOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

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
        if issubclass(ScaleStrategyForListFunctionElasticScaleStrategyOutput, dict):
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
        if not isinstance(other, ScaleStrategyForListFunctionElasticScaleStrategyOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScaleStrategyForListFunctionElasticScaleStrategyOutput):
            return True

        return self.to_dict() != other.to_dict()
