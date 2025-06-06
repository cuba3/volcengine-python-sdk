# coding: utf-8

"""
    httpdns

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AddDomainRequest(object):
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
        'client_token': 'str',
        'domain': 'str',
        'dry_run': 'bool'
    }

    attribute_map = {
        'client_token': 'ClientToken',
        'domain': 'Domain',
        'dry_run': 'DryRun'
    }

    def __init__(self, client_token=None, domain=None, dry_run=None, _configuration=None):  # noqa: E501
        """AddDomainRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_token = None
        self._domain = None
        self._dry_run = None
        self.discriminator = None

        if client_token is not None:
            self.client_token = client_token
        self.domain = domain
        if dry_run is not None:
            self.dry_run = dry_run

    @property
    def client_token(self):
        """Gets the client_token of this AddDomainRequest.  # noqa: E501


        :return: The client_token of this AddDomainRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this AddDomainRequest.


        :param client_token: The client_token of this AddDomainRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def domain(self):
        """Gets the domain of this AddDomainRequest.  # noqa: E501


        :return: The domain of this AddDomainRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this AddDomainRequest.


        :param domain: The domain of this AddDomainRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def dry_run(self):
        """Gets the dry_run of this AddDomainRequest.  # noqa: E501


        :return: The dry_run of this AddDomainRequest.  # noqa: E501
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this AddDomainRequest.


        :param dry_run: The dry_run of this AddDomainRequest.  # noqa: E501
        :type: bool
        """

        self._dry_run = dry_run

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
        if issubclass(AddDomainRequest, dict):
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
        if not isinstance(other, AddDomainRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddDomainRequest):
            return True

        return self.to_dict() != other.to_dict()
