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


class ModelForGetDeploymentOutput(object):
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
        'model_id': 'str',
        'model_version_id': 'str'
    }

    attribute_map = {
        'model_id': 'ModelID',
        'model_version_id': 'ModelVersionID'
    }

    def __init__(self, model_id=None, model_version_id=None, _configuration=None):  # noqa: E501
        """ModelForGetDeploymentOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._model_id = None
        self._model_version_id = None
        self.discriminator = None

        if model_id is not None:
            self.model_id = model_id
        if model_version_id is not None:
            self.model_version_id = model_version_id

    @property
    def model_id(self):
        """Gets the model_id of this ModelForGetDeploymentOutput.  # noqa: E501


        :return: The model_id of this ModelForGetDeploymentOutput.  # noqa: E501
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this ModelForGetDeploymentOutput.


        :param model_id: The model_id of this ModelForGetDeploymentOutput.  # noqa: E501
        :type: str
        """

        self._model_id = model_id

    @property
    def model_version_id(self):
        """Gets the model_version_id of this ModelForGetDeploymentOutput.  # noqa: E501


        :return: The model_version_id of this ModelForGetDeploymentOutput.  # noqa: E501
        :rtype: str
        """
        return self._model_version_id

    @model_version_id.setter
    def model_version_id(self, model_version_id):
        """Sets the model_version_id of this ModelForGetDeploymentOutput.


        :param model_version_id: The model_version_id of this ModelForGetDeploymentOutput.  # noqa: E501
        :type: str
        """

        self._model_version_id = model_version_id

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
        if issubclass(ModelForGetDeploymentOutput, dict):
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
        if not isinstance(other, ModelForGetDeploymentOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelForGetDeploymentOutput):
            return True

        return self.to_dict() != other.to_dict()
