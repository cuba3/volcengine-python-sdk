# coding: utf-8

"""
    vpc

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class RouterTableListForDescribeRouteTableListOutput(object):
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
        'account_id': 'str',
        'associate_type': 'str',
        'creation_time': 'str',
        'description': 'str',
        'ipv4_gateway_id': 'str',
        'ipv6_gateway_id': 'str',
        'project_name': 'str',
        'route_table_id': 'str',
        'route_table_name': 'str',
        'route_table_type': 'str',
        'subnet_ids': 'list[str]',
        'tags': 'list[TagForDescribeRouteTableListOutput]',
        'update_time': 'str',
        'vpc_id': 'str',
        'vpc_name': 'str'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'associate_type': 'AssociateType',
        'creation_time': 'CreationTime',
        'description': 'Description',
        'ipv4_gateway_id': 'Ipv4GatewayId',
        'ipv6_gateway_id': 'Ipv6GatewayId',
        'project_name': 'ProjectName',
        'route_table_id': 'RouteTableId',
        'route_table_name': 'RouteTableName',
        'route_table_type': 'RouteTableType',
        'subnet_ids': 'SubnetIds',
        'tags': 'Tags',
        'update_time': 'UpdateTime',
        'vpc_id': 'VpcId',
        'vpc_name': 'VpcName'
    }

    def __init__(self, account_id=None, associate_type=None, creation_time=None, description=None, ipv4_gateway_id=None, ipv6_gateway_id=None, project_name=None, route_table_id=None, route_table_name=None, route_table_type=None, subnet_ids=None, tags=None, update_time=None, vpc_id=None, vpc_name=None, _configuration=None):  # noqa: E501
        """RouterTableListForDescribeRouteTableListOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._associate_type = None
        self._creation_time = None
        self._description = None
        self._ipv4_gateway_id = None
        self._ipv6_gateway_id = None
        self._project_name = None
        self._route_table_id = None
        self._route_table_name = None
        self._route_table_type = None
        self._subnet_ids = None
        self._tags = None
        self._update_time = None
        self._vpc_id = None
        self._vpc_name = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if associate_type is not None:
            self.associate_type = associate_type
        if creation_time is not None:
            self.creation_time = creation_time
        if description is not None:
            self.description = description
        if ipv4_gateway_id is not None:
            self.ipv4_gateway_id = ipv4_gateway_id
        if ipv6_gateway_id is not None:
            self.ipv6_gateway_id = ipv6_gateway_id
        if project_name is not None:
            self.project_name = project_name
        if route_table_id is not None:
            self.route_table_id = route_table_id
        if route_table_name is not None:
            self.route_table_name = route_table_name
        if route_table_type is not None:
            self.route_table_type = route_table_type
        if subnet_ids is not None:
            self.subnet_ids = subnet_ids
        if tags is not None:
            self.tags = tags
        if update_time is not None:
            self.update_time = update_time
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if vpc_name is not None:
            self.vpc_name = vpc_name

    @property
    def account_id(self):
        """Gets the account_id of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501


        :return: The account_id of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this RouterTableListForDescribeRouteTableListOutput.


        :param account_id: The account_id of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def associate_type(self):
        """Gets the associate_type of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501


        :return: The associate_type of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :rtype: str
        """
        return self._associate_type

    @associate_type.setter
    def associate_type(self, associate_type):
        """Sets the associate_type of this RouterTableListForDescribeRouteTableListOutput.


        :param associate_type: The associate_type of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :type: str
        """

        self._associate_type = associate_type

    @property
    def creation_time(self):
        """Gets the creation_time of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501


        :return: The creation_time of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this RouterTableListForDescribeRouteTableListOutput.


        :param creation_time: The creation_time of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def description(self):
        """Gets the description of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501


        :return: The description of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RouterTableListForDescribeRouteTableListOutput.


        :param description: The description of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ipv4_gateway_id(self):
        """Gets the ipv4_gateway_id of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501


        :return: The ipv4_gateway_id of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :rtype: str
        """
        return self._ipv4_gateway_id

    @ipv4_gateway_id.setter
    def ipv4_gateway_id(self, ipv4_gateway_id):
        """Sets the ipv4_gateway_id of this RouterTableListForDescribeRouteTableListOutput.


        :param ipv4_gateway_id: The ipv4_gateway_id of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :type: str
        """

        self._ipv4_gateway_id = ipv4_gateway_id

    @property
    def ipv6_gateway_id(self):
        """Gets the ipv6_gateway_id of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501


        :return: The ipv6_gateway_id of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :rtype: str
        """
        return self._ipv6_gateway_id

    @ipv6_gateway_id.setter
    def ipv6_gateway_id(self, ipv6_gateway_id):
        """Sets the ipv6_gateway_id of this RouterTableListForDescribeRouteTableListOutput.


        :param ipv6_gateway_id: The ipv6_gateway_id of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :type: str
        """

        self._ipv6_gateway_id = ipv6_gateway_id

    @property
    def project_name(self):
        """Gets the project_name of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501


        :return: The project_name of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this RouterTableListForDescribeRouteTableListOutput.


        :param project_name: The project_name of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def route_table_id(self):
        """Gets the route_table_id of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501


        :return: The route_table_id of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """Sets the route_table_id of this RouterTableListForDescribeRouteTableListOutput.


        :param route_table_id: The route_table_id of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :type: str
        """

        self._route_table_id = route_table_id

    @property
    def route_table_name(self):
        """Gets the route_table_name of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501


        :return: The route_table_name of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :rtype: str
        """
        return self._route_table_name

    @route_table_name.setter
    def route_table_name(self, route_table_name):
        """Sets the route_table_name of this RouterTableListForDescribeRouteTableListOutput.


        :param route_table_name: The route_table_name of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :type: str
        """

        self._route_table_name = route_table_name

    @property
    def route_table_type(self):
        """Gets the route_table_type of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501


        :return: The route_table_type of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :rtype: str
        """
        return self._route_table_type

    @route_table_type.setter
    def route_table_type(self, route_table_type):
        """Sets the route_table_type of this RouterTableListForDescribeRouteTableListOutput.


        :param route_table_type: The route_table_type of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :type: str
        """

        self._route_table_type = route_table_type

    @property
    def subnet_ids(self):
        """Gets the subnet_ids of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501


        :return: The subnet_ids of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        """Sets the subnet_ids of this RouterTableListForDescribeRouteTableListOutput.


        :param subnet_ids: The subnet_ids of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :type: list[str]
        """

        self._subnet_ids = subnet_ids

    @property
    def tags(self):
        """Gets the tags of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501


        :return: The tags of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :rtype: list[TagForDescribeRouteTableListOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this RouterTableListForDescribeRouteTableListOutput.


        :param tags: The tags of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :type: list[TagForDescribeRouteTableListOutput]
        """

        self._tags = tags

    @property
    def update_time(self):
        """Gets the update_time of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501


        :return: The update_time of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this RouterTableListForDescribeRouteTableListOutput.


        :param update_time: The update_time of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

    @property
    def vpc_id(self):
        """Gets the vpc_id of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501


        :return: The vpc_id of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this RouterTableListForDescribeRouteTableListOutput.


        :param vpc_id: The vpc_id of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

    @property
    def vpc_name(self):
        """Gets the vpc_name of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501


        :return: The vpc_name of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        """Sets the vpc_name of this RouterTableListForDescribeRouteTableListOutput.


        :param vpc_name: The vpc_name of this RouterTableListForDescribeRouteTableListOutput.  # noqa: E501
        :type: str
        """

        self._vpc_name = vpc_name

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
        if issubclass(RouterTableListForDescribeRouteTableListOutput, dict):
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
        if not isinstance(other, RouterTableListForDescribeRouteTableListOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RouterTableListForDescribeRouteTableListOutput):
            return True

        return self.to_dict() != other.to_dict()
