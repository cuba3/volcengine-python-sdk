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


class UpstreamConfigForUpdateServiceInput(object):
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
        'consistent_hash_config': 'ConsistentHashConfigForUpdateServiceInput',
        'load_balance_policy': 'str'
    }

    attribute_map = {
        'consistent_hash_config': 'ConsistentHashConfig',
        'load_balance_policy': 'LoadBalancePolicy'
    }

    def __init__(self, consistent_hash_config=None, load_balance_policy=None, _configuration=None):  # noqa: E501
        """UpstreamConfigForUpdateServiceInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._consistent_hash_config = None
        self._load_balance_policy = None
        self.discriminator = None

        if consistent_hash_config is not None:
            self.consistent_hash_config = consistent_hash_config
        if load_balance_policy is not None:
            self.load_balance_policy = load_balance_policy

    @property
    def consistent_hash_config(self):
        """Gets the consistent_hash_config of this UpstreamConfigForUpdateServiceInput.  # noqa: E501


        :return: The consistent_hash_config of this UpstreamConfigForUpdateServiceInput.  # noqa: E501
        :rtype: ConsistentHashConfigForUpdateServiceInput
        """
        return self._consistent_hash_config

    @consistent_hash_config.setter
    def consistent_hash_config(self, consistent_hash_config):
        """Sets the consistent_hash_config of this UpstreamConfigForUpdateServiceInput.


        :param consistent_hash_config: The consistent_hash_config of this UpstreamConfigForUpdateServiceInput.  # noqa: E501
        :type: ConsistentHashConfigForUpdateServiceInput
        """

        self._consistent_hash_config = consistent_hash_config

    @property
    def load_balance_policy(self):
        """Gets the load_balance_policy of this UpstreamConfigForUpdateServiceInput.  # noqa: E501


        :return: The load_balance_policy of this UpstreamConfigForUpdateServiceInput.  # noqa: E501
        :rtype: str
        """
        return self._load_balance_policy

    @load_balance_policy.setter
    def load_balance_policy(self, load_balance_policy):
        """Sets the load_balance_policy of this UpstreamConfigForUpdateServiceInput.


        :param load_balance_policy: The load_balance_policy of this UpstreamConfigForUpdateServiceInput.  # noqa: E501
        :type: str
        """
        allowed_values = ["ROUND_ROBIN", "LEAST_CONN", "RANDOM", "CONSISTENT_HASH"]  # noqa: E501
        if (self._configuration.client_side_validation and
                load_balance_policy not in allowed_values):
            raise ValueError(
                "Invalid value for `load_balance_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(load_balance_policy, allowed_values)
            )

        self._load_balance_policy = load_balance_policy

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
        if issubclass(UpstreamConfigForUpdateServiceInput, dict):
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
        if not isinstance(other, UpstreamConfigForUpdateServiceInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpstreamConfigForUpdateServiceInput):
            return True

        return self.to_dict() != other.to_dict()
