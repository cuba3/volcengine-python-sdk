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


class ListFunctionElasticScaleStrategyResponse(object):
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
        'scale_strategies': 'list[ScaleStrategyForListFunctionElasticScaleStrategyOutput]'
    }

    attribute_map = {
        'scale_strategies': 'ScaleStrategies'
    }

    def __init__(self, scale_strategies=None, _configuration=None):  # noqa: E501
        """ListFunctionElasticScaleStrategyResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._scale_strategies = None
        self.discriminator = None

        if scale_strategies is not None:
            self.scale_strategies = scale_strategies

    @property
    def scale_strategies(self):
        """Gets the scale_strategies of this ListFunctionElasticScaleStrategyResponse.  # noqa: E501


        :return: The scale_strategies of this ListFunctionElasticScaleStrategyResponse.  # noqa: E501
        :rtype: list[ScaleStrategyForListFunctionElasticScaleStrategyOutput]
        """
        return self._scale_strategies

    @scale_strategies.setter
    def scale_strategies(self, scale_strategies):
        """Sets the scale_strategies of this ListFunctionElasticScaleStrategyResponse.


        :param scale_strategies: The scale_strategies of this ListFunctionElasticScaleStrategyResponse.  # noqa: E501
        :type: list[ScaleStrategyForListFunctionElasticScaleStrategyOutput]
        """

        self._scale_strategies = scale_strategies

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
        if issubclass(ListFunctionElasticScaleStrategyResponse, dict):
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
        if not isinstance(other, ListFunctionElasticScaleStrategyResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListFunctionElasticScaleStrategyResponse):
            return True

        return self.to_dict() != other.to_dict()
