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


class RoleForGetJobOutput(object):
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
        'name': 'str',
        'node_affinity_spec': 'NodeAffinitySpecForGetJobOutput',
        'replicas': 'int',
        'resource': 'ResourceForGetJobOutput'
    }

    attribute_map = {
        'name': 'Name',
        'node_affinity_spec': 'NodeAffinitySpec',
        'replicas': 'Replicas',
        'resource': 'Resource'
    }

    def __init__(self, name=None, node_affinity_spec=None, replicas=None, resource=None, _configuration=None):  # noqa: E501
        """RoleForGetJobOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._node_affinity_spec = None
        self._replicas = None
        self._resource = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if node_affinity_spec is not None:
            self.node_affinity_spec = node_affinity_spec
        if replicas is not None:
            self.replicas = replicas
        if resource is not None:
            self.resource = resource

    @property
    def name(self):
        """Gets the name of this RoleForGetJobOutput.  # noqa: E501


        :return: The name of this RoleForGetJobOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RoleForGetJobOutput.


        :param name: The name of this RoleForGetJobOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def node_affinity_spec(self):
        """Gets the node_affinity_spec of this RoleForGetJobOutput.  # noqa: E501


        :return: The node_affinity_spec of this RoleForGetJobOutput.  # noqa: E501
        :rtype: NodeAffinitySpecForGetJobOutput
        """
        return self._node_affinity_spec

    @node_affinity_spec.setter
    def node_affinity_spec(self, node_affinity_spec):
        """Sets the node_affinity_spec of this RoleForGetJobOutput.


        :param node_affinity_spec: The node_affinity_spec of this RoleForGetJobOutput.  # noqa: E501
        :type: NodeAffinitySpecForGetJobOutput
        """

        self._node_affinity_spec = node_affinity_spec

    @property
    def replicas(self):
        """Gets the replicas of this RoleForGetJobOutput.  # noqa: E501


        :return: The replicas of this RoleForGetJobOutput.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this RoleForGetJobOutput.


        :param replicas: The replicas of this RoleForGetJobOutput.  # noqa: E501
        :type: int
        """

        self._replicas = replicas

    @property
    def resource(self):
        """Gets the resource of this RoleForGetJobOutput.  # noqa: E501


        :return: The resource of this RoleForGetJobOutput.  # noqa: E501
        :rtype: ResourceForGetJobOutput
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this RoleForGetJobOutput.


        :param resource: The resource of this RoleForGetJobOutput.  # noqa: E501
        :type: ResourceForGetJobOutput
        """

        self._resource = resource

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
        if issubclass(RoleForGetJobOutput, dict):
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
        if not isinstance(other, RoleForGetJobOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RoleForGetJobOutput):
            return True

        return self.to_dict() != other.to_dict()
