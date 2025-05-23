# coding: utf-8

"""
    waf

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ModuleQuickConfForCreateDomainOutput(object):
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
        'api': 'APIForCreateDomainOutput',
        'auto_cc': 'AutoCCForCreateDomainOutput',
        'bot_sequence': 'BotSequenceForCreateDomainOutput',
        'system_bot': 'SystemBotForCreateDomainOutput',
        'vul': 'VulForCreateDomainOutput'
    }

    attribute_map = {
        'api': 'API',
        'auto_cc': 'AutoCC',
        'bot_sequence': 'BotSequence',
        'system_bot': 'SystemBot',
        'vul': 'Vul'
    }

    def __init__(self, api=None, auto_cc=None, bot_sequence=None, system_bot=None, vul=None, _configuration=None):  # noqa: E501
        """ModuleQuickConfForCreateDomainOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._api = None
        self._auto_cc = None
        self._bot_sequence = None
        self._system_bot = None
        self._vul = None
        self.discriminator = None

        if api is not None:
            self.api = api
        if auto_cc is not None:
            self.auto_cc = auto_cc
        if bot_sequence is not None:
            self.bot_sequence = bot_sequence
        if system_bot is not None:
            self.system_bot = system_bot
        if vul is not None:
            self.vul = vul

    @property
    def api(self):
        """Gets the api of this ModuleQuickConfForCreateDomainOutput.  # noqa: E501


        :return: The api of this ModuleQuickConfForCreateDomainOutput.  # noqa: E501
        :rtype: APIForCreateDomainOutput
        """
        return self._api

    @api.setter
    def api(self, api):
        """Sets the api of this ModuleQuickConfForCreateDomainOutput.


        :param api: The api of this ModuleQuickConfForCreateDomainOutput.  # noqa: E501
        :type: APIForCreateDomainOutput
        """

        self._api = api

    @property
    def auto_cc(self):
        """Gets the auto_cc of this ModuleQuickConfForCreateDomainOutput.  # noqa: E501


        :return: The auto_cc of this ModuleQuickConfForCreateDomainOutput.  # noqa: E501
        :rtype: AutoCCForCreateDomainOutput
        """
        return self._auto_cc

    @auto_cc.setter
    def auto_cc(self, auto_cc):
        """Sets the auto_cc of this ModuleQuickConfForCreateDomainOutput.


        :param auto_cc: The auto_cc of this ModuleQuickConfForCreateDomainOutput.  # noqa: E501
        :type: AutoCCForCreateDomainOutput
        """

        self._auto_cc = auto_cc

    @property
    def bot_sequence(self):
        """Gets the bot_sequence of this ModuleQuickConfForCreateDomainOutput.  # noqa: E501


        :return: The bot_sequence of this ModuleQuickConfForCreateDomainOutput.  # noqa: E501
        :rtype: BotSequenceForCreateDomainOutput
        """
        return self._bot_sequence

    @bot_sequence.setter
    def bot_sequence(self, bot_sequence):
        """Sets the bot_sequence of this ModuleQuickConfForCreateDomainOutput.


        :param bot_sequence: The bot_sequence of this ModuleQuickConfForCreateDomainOutput.  # noqa: E501
        :type: BotSequenceForCreateDomainOutput
        """

        self._bot_sequence = bot_sequence

    @property
    def system_bot(self):
        """Gets the system_bot of this ModuleQuickConfForCreateDomainOutput.  # noqa: E501


        :return: The system_bot of this ModuleQuickConfForCreateDomainOutput.  # noqa: E501
        :rtype: SystemBotForCreateDomainOutput
        """
        return self._system_bot

    @system_bot.setter
    def system_bot(self, system_bot):
        """Sets the system_bot of this ModuleQuickConfForCreateDomainOutput.


        :param system_bot: The system_bot of this ModuleQuickConfForCreateDomainOutput.  # noqa: E501
        :type: SystemBotForCreateDomainOutput
        """

        self._system_bot = system_bot

    @property
    def vul(self):
        """Gets the vul of this ModuleQuickConfForCreateDomainOutput.  # noqa: E501


        :return: The vul of this ModuleQuickConfForCreateDomainOutput.  # noqa: E501
        :rtype: VulForCreateDomainOutput
        """
        return self._vul

    @vul.setter
    def vul(self, vul):
        """Sets the vul of this ModuleQuickConfForCreateDomainOutput.


        :param vul: The vul of this ModuleQuickConfForCreateDomainOutput.  # noqa: E501
        :type: VulForCreateDomainOutput
        """

        self._vul = vul

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
        if issubclass(ModuleQuickConfForCreateDomainOutput, dict):
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
        if not isinstance(other, ModuleQuickConfForCreateDomainOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModuleQuickConfForCreateDomainOutput):
            return True

        return self.to_dict() != other.to_dict()
