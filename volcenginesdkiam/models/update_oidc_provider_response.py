# coding: utf-8

"""
    iam

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UpdateOIDCProviderResponse(object):
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
        'create_date': 'str',
        'description': 'str',
        'oidc_provider_name': 'str',
        'trn': 'str',
        'update_date': 'str'
    }

    attribute_map = {
        'create_date': 'CreateDate',
        'description': 'Description',
        'oidc_provider_name': 'OIDCProviderName',
        'trn': 'Trn',
        'update_date': 'UpdateDate'
    }

    def __init__(self, create_date=None, description=None, oidc_provider_name=None, trn=None, update_date=None, _configuration=None):  # noqa: E501
        """UpdateOIDCProviderResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create_date = None
        self._description = None
        self._oidc_provider_name = None
        self._trn = None
        self._update_date = None
        self.discriminator = None

        if create_date is not None:
            self.create_date = create_date
        if description is not None:
            self.description = description
        if oidc_provider_name is not None:
            self.oidc_provider_name = oidc_provider_name
        if trn is not None:
            self.trn = trn
        if update_date is not None:
            self.update_date = update_date

    @property
    def create_date(self):
        """Gets the create_date of this UpdateOIDCProviderResponse.  # noqa: E501


        :return: The create_date of this UpdateOIDCProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this UpdateOIDCProviderResponse.


        :param create_date: The create_date of this UpdateOIDCProviderResponse.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

    @property
    def description(self):
        """Gets the description of this UpdateOIDCProviderResponse.  # noqa: E501


        :return: The description of this UpdateOIDCProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateOIDCProviderResponse.


        :param description: The description of this UpdateOIDCProviderResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def oidc_provider_name(self):
        """Gets the oidc_provider_name of this UpdateOIDCProviderResponse.  # noqa: E501


        :return: The oidc_provider_name of this UpdateOIDCProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._oidc_provider_name

    @oidc_provider_name.setter
    def oidc_provider_name(self, oidc_provider_name):
        """Sets the oidc_provider_name of this UpdateOIDCProviderResponse.


        :param oidc_provider_name: The oidc_provider_name of this UpdateOIDCProviderResponse.  # noqa: E501
        :type: str
        """

        self._oidc_provider_name = oidc_provider_name

    @property
    def trn(self):
        """Gets the trn of this UpdateOIDCProviderResponse.  # noqa: E501


        :return: The trn of this UpdateOIDCProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._trn

    @trn.setter
    def trn(self, trn):
        """Sets the trn of this UpdateOIDCProviderResponse.


        :param trn: The trn of this UpdateOIDCProviderResponse.  # noqa: E501
        :type: str
        """

        self._trn = trn

    @property
    def update_date(self):
        """Gets the update_date of this UpdateOIDCProviderResponse.  # noqa: E501


        :return: The update_date of this UpdateOIDCProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this UpdateOIDCProviderResponse.


        :param update_date: The update_date of this UpdateOIDCProviderResponse.  # noqa: E501
        :type: str
        """

        self._update_date = update_date

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
        if issubclass(UpdateOIDCProviderResponse, dict):
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
        if not isinstance(other, UpdateOIDCProviderResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateOIDCProviderResponse):
            return True

        return self.to_dict() != other.to_dict()
