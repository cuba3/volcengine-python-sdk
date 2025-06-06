# coding: utf-8

"""
    alb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AclForDescribeAclsOutput(object):
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
        'acl_entry_count': 'int',
        'acl_id': 'str',
        'acl_name': 'str',
        'create_time': 'str',
        'description': 'str',
        'listeners': 'list[str]',
        'project_name': 'str',
        'status': 'str',
        'tags': 'list[TagForDescribeAclsOutput]',
        'update_time': 'str'
    }

    attribute_map = {
        'acl_entry_count': 'AclEntryCount',
        'acl_id': 'AclId',
        'acl_name': 'AclName',
        'create_time': 'CreateTime',
        'description': 'Description',
        'listeners': 'Listeners',
        'project_name': 'ProjectName',
        'status': 'Status',
        'tags': 'Tags',
        'update_time': 'UpdateTime'
    }

    def __init__(self, acl_entry_count=None, acl_id=None, acl_name=None, create_time=None, description=None, listeners=None, project_name=None, status=None, tags=None, update_time=None, _configuration=None):  # noqa: E501
        """AclForDescribeAclsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._acl_entry_count = None
        self._acl_id = None
        self._acl_name = None
        self._create_time = None
        self._description = None
        self._listeners = None
        self._project_name = None
        self._status = None
        self._tags = None
        self._update_time = None
        self.discriminator = None

        if acl_entry_count is not None:
            self.acl_entry_count = acl_entry_count
        if acl_id is not None:
            self.acl_id = acl_id
        if acl_name is not None:
            self.acl_name = acl_name
        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description
        if listeners is not None:
            self.listeners = listeners
        if project_name is not None:
            self.project_name = project_name
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if update_time is not None:
            self.update_time = update_time

    @property
    def acl_entry_count(self):
        """Gets the acl_entry_count of this AclForDescribeAclsOutput.  # noqa: E501


        :return: The acl_entry_count of this AclForDescribeAclsOutput.  # noqa: E501
        :rtype: int
        """
        return self._acl_entry_count

    @acl_entry_count.setter
    def acl_entry_count(self, acl_entry_count):
        """Sets the acl_entry_count of this AclForDescribeAclsOutput.


        :param acl_entry_count: The acl_entry_count of this AclForDescribeAclsOutput.  # noqa: E501
        :type: int
        """

        self._acl_entry_count = acl_entry_count

    @property
    def acl_id(self):
        """Gets the acl_id of this AclForDescribeAclsOutput.  # noqa: E501


        :return: The acl_id of this AclForDescribeAclsOutput.  # noqa: E501
        :rtype: str
        """
        return self._acl_id

    @acl_id.setter
    def acl_id(self, acl_id):
        """Sets the acl_id of this AclForDescribeAclsOutput.


        :param acl_id: The acl_id of this AclForDescribeAclsOutput.  # noqa: E501
        :type: str
        """

        self._acl_id = acl_id

    @property
    def acl_name(self):
        """Gets the acl_name of this AclForDescribeAclsOutput.  # noqa: E501


        :return: The acl_name of this AclForDescribeAclsOutput.  # noqa: E501
        :rtype: str
        """
        return self._acl_name

    @acl_name.setter
    def acl_name(self, acl_name):
        """Sets the acl_name of this AclForDescribeAclsOutput.


        :param acl_name: The acl_name of this AclForDescribeAclsOutput.  # noqa: E501
        :type: str
        """

        self._acl_name = acl_name

    @property
    def create_time(self):
        """Gets the create_time of this AclForDescribeAclsOutput.  # noqa: E501


        :return: The create_time of this AclForDescribeAclsOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AclForDescribeAclsOutput.


        :param create_time: The create_time of this AclForDescribeAclsOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this AclForDescribeAclsOutput.  # noqa: E501


        :return: The description of this AclForDescribeAclsOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AclForDescribeAclsOutput.


        :param description: The description of this AclForDescribeAclsOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def listeners(self):
        """Gets the listeners of this AclForDescribeAclsOutput.  # noqa: E501


        :return: The listeners of this AclForDescribeAclsOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """Sets the listeners of this AclForDescribeAclsOutput.


        :param listeners: The listeners of this AclForDescribeAclsOutput.  # noqa: E501
        :type: list[str]
        """

        self._listeners = listeners

    @property
    def project_name(self):
        """Gets the project_name of this AclForDescribeAclsOutput.  # noqa: E501


        :return: The project_name of this AclForDescribeAclsOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this AclForDescribeAclsOutput.


        :param project_name: The project_name of this AclForDescribeAclsOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def status(self):
        """Gets the status of this AclForDescribeAclsOutput.  # noqa: E501


        :return: The status of this AclForDescribeAclsOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AclForDescribeAclsOutput.


        :param status: The status of this AclForDescribeAclsOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this AclForDescribeAclsOutput.  # noqa: E501


        :return: The tags of this AclForDescribeAclsOutput.  # noqa: E501
        :rtype: list[TagForDescribeAclsOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AclForDescribeAclsOutput.


        :param tags: The tags of this AclForDescribeAclsOutput.  # noqa: E501
        :type: list[TagForDescribeAclsOutput]
        """

        self._tags = tags

    @property
    def update_time(self):
        """Gets the update_time of this AclForDescribeAclsOutput.  # noqa: E501


        :return: The update_time of this AclForDescribeAclsOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this AclForDescribeAclsOutput.


        :param update_time: The update_time of this AclForDescribeAclsOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

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
        if issubclass(AclForDescribeAclsOutput, dict):
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
        if not isinstance(other, AclForDescribeAclsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AclForDescribeAclsOutput):
            return True

        return self.to_dict() != other.to_dict()
