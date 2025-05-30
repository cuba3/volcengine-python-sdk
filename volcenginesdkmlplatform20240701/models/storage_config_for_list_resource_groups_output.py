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


class StorageConfigForListResourceGroupsOutput(object):
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
        'sfcs': 'SfcsForListResourceGroupsOutput',
        'storage_network_config': 'StorageNetworkConfigForListResourceGroupsOutput',
        'vepfs': 'VepfsForListResourceGroupsOutput'
    }

    attribute_map = {
        'sfcs': 'Sfcs',
        'storage_network_config': 'StorageNetworkConfig',
        'vepfs': 'Vepfs'
    }

    def __init__(self, sfcs=None, storage_network_config=None, vepfs=None, _configuration=None):  # noqa: E501
        """StorageConfigForListResourceGroupsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._sfcs = None
        self._storage_network_config = None
        self._vepfs = None
        self.discriminator = None

        if sfcs is not None:
            self.sfcs = sfcs
        if storage_network_config is not None:
            self.storage_network_config = storage_network_config
        if vepfs is not None:
            self.vepfs = vepfs

    @property
    def sfcs(self):
        """Gets the sfcs of this StorageConfigForListResourceGroupsOutput.  # noqa: E501


        :return: The sfcs of this StorageConfigForListResourceGroupsOutput.  # noqa: E501
        :rtype: SfcsForListResourceGroupsOutput
        """
        return self._sfcs

    @sfcs.setter
    def sfcs(self, sfcs):
        """Sets the sfcs of this StorageConfigForListResourceGroupsOutput.


        :param sfcs: The sfcs of this StorageConfigForListResourceGroupsOutput.  # noqa: E501
        :type: SfcsForListResourceGroupsOutput
        """

        self._sfcs = sfcs

    @property
    def storage_network_config(self):
        """Gets the storage_network_config of this StorageConfigForListResourceGroupsOutput.  # noqa: E501


        :return: The storage_network_config of this StorageConfigForListResourceGroupsOutput.  # noqa: E501
        :rtype: StorageNetworkConfigForListResourceGroupsOutput
        """
        return self._storage_network_config

    @storage_network_config.setter
    def storage_network_config(self, storage_network_config):
        """Sets the storage_network_config of this StorageConfigForListResourceGroupsOutput.


        :param storage_network_config: The storage_network_config of this StorageConfigForListResourceGroupsOutput.  # noqa: E501
        :type: StorageNetworkConfigForListResourceGroupsOutput
        """

        self._storage_network_config = storage_network_config

    @property
    def vepfs(self):
        """Gets the vepfs of this StorageConfigForListResourceGroupsOutput.  # noqa: E501


        :return: The vepfs of this StorageConfigForListResourceGroupsOutput.  # noqa: E501
        :rtype: VepfsForListResourceGroupsOutput
        """
        return self._vepfs

    @vepfs.setter
    def vepfs(self, vepfs):
        """Sets the vepfs of this StorageConfigForListResourceGroupsOutput.


        :param vepfs: The vepfs of this StorageConfigForListResourceGroupsOutput.  # noqa: E501
        :type: VepfsForListResourceGroupsOutput
        """

        self._vepfs = vepfs

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
        if issubclass(StorageConfigForListResourceGroupsOutput, dict):
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
        if not isinstance(other, StorageConfigForListResourceGroupsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageConfigForListResourceGroupsOutput):
            return True

        return self.to_dict() != other.to_dict()
