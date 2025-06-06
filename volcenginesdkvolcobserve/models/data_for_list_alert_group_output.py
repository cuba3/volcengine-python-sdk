# coding: utf-8

"""
    volc_observe

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DataForListAlertGroupOutput(object):
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
        'alert_state': 'str',
        'alert_type': 'str',
        'dimension': 'str',
        'duration': 'str',
        'end_at': 'str',
        'id': 'str',
        'level': 'str',
        'namespace': 'str',
        'region': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_type': 'str',
        'rule_id': 'str',
        'rule_name': 'str',
        'start_at': 'str',
        'sub_namespace': 'str'
    }

    attribute_map = {
        'alert_state': 'AlertState',
        'alert_type': 'AlertType',
        'dimension': 'Dimension',
        'duration': 'Duration',
        'end_at': 'EndAt',
        'id': 'Id',
        'level': 'Level',
        'namespace': 'Namespace',
        'region': 'Region',
        'resource_id': 'ResourceId',
        'resource_name': 'ResourceName',
        'resource_type': 'ResourceType',
        'rule_id': 'RuleId',
        'rule_name': 'RuleName',
        'start_at': 'StartAt',
        'sub_namespace': 'SubNamespace'
    }

    def __init__(self, alert_state=None, alert_type=None, dimension=None, duration=None, end_at=None, id=None, level=None, namespace=None, region=None, resource_id=None, resource_name=None, resource_type=None, rule_id=None, rule_name=None, start_at=None, sub_namespace=None, _configuration=None):  # noqa: E501
        """DataForListAlertGroupOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alert_state = None
        self._alert_type = None
        self._dimension = None
        self._duration = None
        self._end_at = None
        self._id = None
        self._level = None
        self._namespace = None
        self._region = None
        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self._rule_id = None
        self._rule_name = None
        self._start_at = None
        self._sub_namespace = None
        self.discriminator = None

        if alert_state is not None:
            self.alert_state = alert_state
        if alert_type is not None:
            self.alert_type = alert_type
        if dimension is not None:
            self.dimension = dimension
        if duration is not None:
            self.duration = duration
        if end_at is not None:
            self.end_at = end_at
        if id is not None:
            self.id = id
        if level is not None:
            self.level = level
        if namespace is not None:
            self.namespace = namespace
        if region is not None:
            self.region = region
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_type is not None:
            self.resource_type = resource_type
        if rule_id is not None:
            self.rule_id = rule_id
        if rule_name is not None:
            self.rule_name = rule_name
        if start_at is not None:
            self.start_at = start_at
        if sub_namespace is not None:
            self.sub_namespace = sub_namespace

    @property
    def alert_state(self):
        """Gets the alert_state of this DataForListAlertGroupOutput.  # noqa: E501


        :return: The alert_state of this DataForListAlertGroupOutput.  # noqa: E501
        :rtype: str
        """
        return self._alert_state

    @alert_state.setter
    def alert_state(self, alert_state):
        """Sets the alert_state of this DataForListAlertGroupOutput.


        :param alert_state: The alert_state of this DataForListAlertGroupOutput.  # noqa: E501
        :type: str
        """

        self._alert_state = alert_state

    @property
    def alert_type(self):
        """Gets the alert_type of this DataForListAlertGroupOutput.  # noqa: E501


        :return: The alert_type of this DataForListAlertGroupOutput.  # noqa: E501
        :rtype: str
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """Sets the alert_type of this DataForListAlertGroupOutput.


        :param alert_type: The alert_type of this DataForListAlertGroupOutput.  # noqa: E501
        :type: str
        """

        self._alert_type = alert_type

    @property
    def dimension(self):
        """Gets the dimension of this DataForListAlertGroupOutput.  # noqa: E501


        :return: The dimension of this DataForListAlertGroupOutput.  # noqa: E501
        :rtype: str
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        """Sets the dimension of this DataForListAlertGroupOutput.


        :param dimension: The dimension of this DataForListAlertGroupOutput.  # noqa: E501
        :type: str
        """

        self._dimension = dimension

    @property
    def duration(self):
        """Gets the duration of this DataForListAlertGroupOutput.  # noqa: E501


        :return: The duration of this DataForListAlertGroupOutput.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this DataForListAlertGroupOutput.


        :param duration: The duration of this DataForListAlertGroupOutput.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def end_at(self):
        """Gets the end_at of this DataForListAlertGroupOutput.  # noqa: E501


        :return: The end_at of this DataForListAlertGroupOutput.  # noqa: E501
        :rtype: str
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        """Sets the end_at of this DataForListAlertGroupOutput.


        :param end_at: The end_at of this DataForListAlertGroupOutput.  # noqa: E501
        :type: str
        """

        self._end_at = end_at

    @property
    def id(self):
        """Gets the id of this DataForListAlertGroupOutput.  # noqa: E501


        :return: The id of this DataForListAlertGroupOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataForListAlertGroupOutput.


        :param id: The id of this DataForListAlertGroupOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def level(self):
        """Gets the level of this DataForListAlertGroupOutput.  # noqa: E501


        :return: The level of this DataForListAlertGroupOutput.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this DataForListAlertGroupOutput.


        :param level: The level of this DataForListAlertGroupOutput.  # noqa: E501
        :type: str
        """

        self._level = level

    @property
    def namespace(self):
        """Gets the namespace of this DataForListAlertGroupOutput.  # noqa: E501


        :return: The namespace of this DataForListAlertGroupOutput.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this DataForListAlertGroupOutput.


        :param namespace: The namespace of this DataForListAlertGroupOutput.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def region(self):
        """Gets the region of this DataForListAlertGroupOutput.  # noqa: E501


        :return: The region of this DataForListAlertGroupOutput.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this DataForListAlertGroupOutput.


        :param region: The region of this DataForListAlertGroupOutput.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def resource_id(self):
        """Gets the resource_id of this DataForListAlertGroupOutput.  # noqa: E501


        :return: The resource_id of this DataForListAlertGroupOutput.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this DataForListAlertGroupOutput.


        :param resource_id: The resource_id of this DataForListAlertGroupOutput.  # noqa: E501
        :type: str
        """

        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this DataForListAlertGroupOutput.  # noqa: E501


        :return: The resource_name of this DataForListAlertGroupOutput.  # noqa: E501
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this DataForListAlertGroupOutput.


        :param resource_name: The resource_name of this DataForListAlertGroupOutput.  # noqa: E501
        :type: str
        """

        self._resource_name = resource_name

    @property
    def resource_type(self):
        """Gets the resource_type of this DataForListAlertGroupOutput.  # noqa: E501


        :return: The resource_type of this DataForListAlertGroupOutput.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this DataForListAlertGroupOutput.


        :param resource_type: The resource_type of this DataForListAlertGroupOutput.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def rule_id(self):
        """Gets the rule_id of this DataForListAlertGroupOutput.  # noqa: E501


        :return: The rule_id of this DataForListAlertGroupOutput.  # noqa: E501
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this DataForListAlertGroupOutput.


        :param rule_id: The rule_id of this DataForListAlertGroupOutput.  # noqa: E501
        :type: str
        """

        self._rule_id = rule_id

    @property
    def rule_name(self):
        """Gets the rule_name of this DataForListAlertGroupOutput.  # noqa: E501


        :return: The rule_name of this DataForListAlertGroupOutput.  # noqa: E501
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this DataForListAlertGroupOutput.


        :param rule_name: The rule_name of this DataForListAlertGroupOutput.  # noqa: E501
        :type: str
        """

        self._rule_name = rule_name

    @property
    def start_at(self):
        """Gets the start_at of this DataForListAlertGroupOutput.  # noqa: E501


        :return: The start_at of this DataForListAlertGroupOutput.  # noqa: E501
        :rtype: str
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        """Sets the start_at of this DataForListAlertGroupOutput.


        :param start_at: The start_at of this DataForListAlertGroupOutput.  # noqa: E501
        :type: str
        """

        self._start_at = start_at

    @property
    def sub_namespace(self):
        """Gets the sub_namespace of this DataForListAlertGroupOutput.  # noqa: E501


        :return: The sub_namespace of this DataForListAlertGroupOutput.  # noqa: E501
        :rtype: str
        """
        return self._sub_namespace

    @sub_namespace.setter
    def sub_namespace(self, sub_namespace):
        """Sets the sub_namespace of this DataForListAlertGroupOutput.


        :param sub_namespace: The sub_namespace of this DataForListAlertGroupOutput.  # noqa: E501
        :type: str
        """

        self._sub_namespace = sub_namespace

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
        if issubclass(DataForListAlertGroupOutput, dict):
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
        if not isinstance(other, DataForListAlertGroupOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForListAlertGroupOutput):
            return True

        return self.to_dict() != other.to_dict()
