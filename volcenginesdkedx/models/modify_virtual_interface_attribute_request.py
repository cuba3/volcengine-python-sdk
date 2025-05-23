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


class ModifyVirtualInterfaceAttributeRequest(object):
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
        'local_ip': 'str',
        'max_bandwidth': 'int',
        'name': 'str',
        'peer_ip': 'str',
        'vif_instance_id': 'str',
        'vlan_id': 'int'
    }

    attribute_map = {
        'local_ip': 'LocalIP',
        'max_bandwidth': 'MaxBandwidth',
        'name': 'Name',
        'peer_ip': 'PeerIP',
        'vif_instance_id': 'VIFInstanceId',
        'vlan_id': 'VlanId'
    }

    def __init__(self, local_ip=None, max_bandwidth=None, name=None, peer_ip=None, vif_instance_id=None, vlan_id=None, _configuration=None):  # noqa: E501
        """ModifyVirtualInterfaceAttributeRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._local_ip = None
        self._max_bandwidth = None
        self._name = None
        self._peer_ip = None
        self._vif_instance_id = None
        self._vlan_id = None
        self.discriminator = None

        if local_ip is not None:
            self.local_ip = local_ip
        if max_bandwidth is not None:
            self.max_bandwidth = max_bandwidth
        if name is not None:
            self.name = name
        self.peer_ip = peer_ip
        self.vif_instance_id = vif_instance_id
        if vlan_id is not None:
            self.vlan_id = vlan_id

    @property
    def local_ip(self):
        """Gets the local_ip of this ModifyVirtualInterfaceAttributeRequest.  # noqa: E501


        :return: The local_ip of this ModifyVirtualInterfaceAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._local_ip

    @local_ip.setter
    def local_ip(self, local_ip):
        """Sets the local_ip of this ModifyVirtualInterfaceAttributeRequest.


        :param local_ip: The local_ip of this ModifyVirtualInterfaceAttributeRequest.  # noqa: E501
        :type: str
        """

        self._local_ip = local_ip

    @property
    def max_bandwidth(self):
        """Gets the max_bandwidth of this ModifyVirtualInterfaceAttributeRequest.  # noqa: E501


        :return: The max_bandwidth of this ModifyVirtualInterfaceAttributeRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_bandwidth

    @max_bandwidth.setter
    def max_bandwidth(self, max_bandwidth):
        """Sets the max_bandwidth of this ModifyVirtualInterfaceAttributeRequest.


        :param max_bandwidth: The max_bandwidth of this ModifyVirtualInterfaceAttributeRequest.  # noqa: E501
        :type: int
        """

        self._max_bandwidth = max_bandwidth

    @property
    def name(self):
        """Gets the name of this ModifyVirtualInterfaceAttributeRequest.  # noqa: E501


        :return: The name of this ModifyVirtualInterfaceAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModifyVirtualInterfaceAttributeRequest.


        :param name: The name of this ModifyVirtualInterfaceAttributeRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def peer_ip(self):
        """Gets the peer_ip of this ModifyVirtualInterfaceAttributeRequest.  # noqa: E501


        :return: The peer_ip of this ModifyVirtualInterfaceAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._peer_ip

    @peer_ip.setter
    def peer_ip(self, peer_ip):
        """Sets the peer_ip of this ModifyVirtualInterfaceAttributeRequest.


        :param peer_ip: The peer_ip of this ModifyVirtualInterfaceAttributeRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and peer_ip is None:
            raise ValueError("Invalid value for `peer_ip`, must not be `None`")  # noqa: E501

        self._peer_ip = peer_ip

    @property
    def vif_instance_id(self):
        """Gets the vif_instance_id of this ModifyVirtualInterfaceAttributeRequest.  # noqa: E501


        :return: The vif_instance_id of this ModifyVirtualInterfaceAttributeRequest.  # noqa: E501
        :rtype: str
        """
        return self._vif_instance_id

    @vif_instance_id.setter
    def vif_instance_id(self, vif_instance_id):
        """Sets the vif_instance_id of this ModifyVirtualInterfaceAttributeRequest.


        :param vif_instance_id: The vif_instance_id of this ModifyVirtualInterfaceAttributeRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and vif_instance_id is None:
            raise ValueError("Invalid value for `vif_instance_id`, must not be `None`")  # noqa: E501

        self._vif_instance_id = vif_instance_id

    @property
    def vlan_id(self):
        """Gets the vlan_id of this ModifyVirtualInterfaceAttributeRequest.  # noqa: E501


        :return: The vlan_id of this ModifyVirtualInterfaceAttributeRequest.  # noqa: E501
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this ModifyVirtualInterfaceAttributeRequest.


        :param vlan_id: The vlan_id of this ModifyVirtualInterfaceAttributeRequest.  # noqa: E501
        :type: int
        """

        self._vlan_id = vlan_id

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
        if issubclass(ModifyVirtualInterfaceAttributeRequest, dict):
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
        if not isinstance(other, ModifyVirtualInterfaceAttributeRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyVirtualInterfaceAttributeRequest):
            return True

        return self.to_dict() != other.to_dict()
