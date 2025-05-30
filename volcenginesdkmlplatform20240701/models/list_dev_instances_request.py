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


class ListDevInstancesRequest(object):
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
        'create_user_ids': 'list[int]',
        'id_contains': 'str',
        'ids': 'list[str]',
        'name_contains': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'relationship': 'str',
        'resource_group_ids': 'list[str]',
        'resource_queue_ids': 'list[str]',
        'sort_by': 'str',
        'sort_order': 'str',
        'states': 'list[str]'
    }

    attribute_map = {
        'create_user_ids': 'CreateUserIds',
        'id_contains': 'IdContains',
        'ids': 'Ids',
        'name_contains': 'NameContains',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'relationship': 'Relationship',
        'resource_group_ids': 'ResourceGroupIds',
        'resource_queue_ids': 'ResourceQueueIds',
        'sort_by': 'SortBy',
        'sort_order': 'SortOrder',
        'states': 'States'
    }

    def __init__(self, create_user_ids=None, id_contains=None, ids=None, name_contains=None, page_number=None, page_size=None, relationship=None, resource_group_ids=None, resource_queue_ids=None, sort_by=None, sort_order=None, states=None, _configuration=None):  # noqa: E501
        """ListDevInstancesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create_user_ids = None
        self._id_contains = None
        self._ids = None
        self._name_contains = None
        self._page_number = None
        self._page_size = None
        self._relationship = None
        self._resource_group_ids = None
        self._resource_queue_ids = None
        self._sort_by = None
        self._sort_order = None
        self._states = None
        self.discriminator = None

        if create_user_ids is not None:
            self.create_user_ids = create_user_ids
        if id_contains is not None:
            self.id_contains = id_contains
        if ids is not None:
            self.ids = ids
        if name_contains is not None:
            self.name_contains = name_contains
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if relationship is not None:
            self.relationship = relationship
        if resource_group_ids is not None:
            self.resource_group_ids = resource_group_ids
        if resource_queue_ids is not None:
            self.resource_queue_ids = resource_queue_ids
        if sort_by is not None:
            self.sort_by = sort_by
        if sort_order is not None:
            self.sort_order = sort_order
        if states is not None:
            self.states = states

    @property
    def create_user_ids(self):
        """Gets the create_user_ids of this ListDevInstancesRequest.  # noqa: E501


        :return: The create_user_ids of this ListDevInstancesRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._create_user_ids

    @create_user_ids.setter
    def create_user_ids(self, create_user_ids):
        """Sets the create_user_ids of this ListDevInstancesRequest.


        :param create_user_ids: The create_user_ids of this ListDevInstancesRequest.  # noqa: E501
        :type: list[int]
        """

        self._create_user_ids = create_user_ids

    @property
    def id_contains(self):
        """Gets the id_contains of this ListDevInstancesRequest.  # noqa: E501


        :return: The id_contains of this ListDevInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._id_contains

    @id_contains.setter
    def id_contains(self, id_contains):
        """Sets the id_contains of this ListDevInstancesRequest.


        :param id_contains: The id_contains of this ListDevInstancesRequest.  # noqa: E501
        :type: str
        """

        self._id_contains = id_contains

    @property
    def ids(self):
        """Gets the ids of this ListDevInstancesRequest.  # noqa: E501


        :return: The ids of this ListDevInstancesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this ListDevInstancesRequest.


        :param ids: The ids of this ListDevInstancesRequest.  # noqa: E501
        :type: list[str]
        """

        self._ids = ids

    @property
    def name_contains(self):
        """Gets the name_contains of this ListDevInstancesRequest.  # noqa: E501


        :return: The name_contains of this ListDevInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._name_contains

    @name_contains.setter
    def name_contains(self, name_contains):
        """Sets the name_contains of this ListDevInstancesRequest.


        :param name_contains: The name_contains of this ListDevInstancesRequest.  # noqa: E501
        :type: str
        """

        self._name_contains = name_contains

    @property
    def page_number(self):
        """Gets the page_number of this ListDevInstancesRequest.  # noqa: E501


        :return: The page_number of this ListDevInstancesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ListDevInstancesRequest.


        :param page_number: The page_number of this ListDevInstancesRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this ListDevInstancesRequest.  # noqa: E501


        :return: The page_size of this ListDevInstancesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListDevInstancesRequest.


        :param page_size: The page_size of this ListDevInstancesRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                page_size is not None and page_size > 100):  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value less than or equal to `100`")  # noqa: E501
        if (self._configuration.client_side_validation and
                page_size is not None and page_size < 10):  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value greater than or equal to `10`")  # noqa: E501

        self._page_size = page_size

    @property
    def relationship(self):
        """Gets the relationship of this ListDevInstancesRequest.  # noqa: E501


        :return: The relationship of this ListDevInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._relationship

    @relationship.setter
    def relationship(self, relationship):
        """Sets the relationship of this ListDevInstancesRequest.


        :param relationship: The relationship of this ListDevInstancesRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Created", "Owned"]  # noqa: E501
        if (self._configuration.client_side_validation and
                relationship not in allowed_values):
            raise ValueError(
                "Invalid value for `relationship` ({0}), must be one of {1}"  # noqa: E501
                .format(relationship, allowed_values)
            )

        self._relationship = relationship

    @property
    def resource_group_ids(self):
        """Gets the resource_group_ids of this ListDevInstancesRequest.  # noqa: E501


        :return: The resource_group_ids of this ListDevInstancesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._resource_group_ids

    @resource_group_ids.setter
    def resource_group_ids(self, resource_group_ids):
        """Sets the resource_group_ids of this ListDevInstancesRequest.


        :param resource_group_ids: The resource_group_ids of this ListDevInstancesRequest.  # noqa: E501
        :type: list[str]
        """

        self._resource_group_ids = resource_group_ids

    @property
    def resource_queue_ids(self):
        """Gets the resource_queue_ids of this ListDevInstancesRequest.  # noqa: E501


        :return: The resource_queue_ids of this ListDevInstancesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._resource_queue_ids

    @resource_queue_ids.setter
    def resource_queue_ids(self, resource_queue_ids):
        """Sets the resource_queue_ids of this ListDevInstancesRequest.


        :param resource_queue_ids: The resource_queue_ids of this ListDevInstancesRequest.  # noqa: E501
        :type: list[str]
        """

        self._resource_queue_ids = resource_queue_ids

    @property
    def sort_by(self):
        """Gets the sort_by of this ListDevInstancesRequest.  # noqa: E501


        :return: The sort_by of this ListDevInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this ListDevInstancesRequest.


        :param sort_by: The sort_by of this ListDevInstancesRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["CreateTime"]  # noqa: E501
        if (self._configuration.client_side_validation and
                sort_by not in allowed_values):
            raise ValueError(
                "Invalid value for `sort_by` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_by, allowed_values)
            )

        self._sort_by = sort_by

    @property
    def sort_order(self):
        """Gets the sort_order of this ListDevInstancesRequest.  # noqa: E501


        :return: The sort_order of this ListDevInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this ListDevInstancesRequest.


        :param sort_order: The sort_order of this ListDevInstancesRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Ascend", "Descend"]  # noqa: E501
        if (self._configuration.client_side_validation and
                sort_order not in allowed_values):
            raise ValueError(
                "Invalid value for `sort_order` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_order, allowed_values)
            )

        self._sort_order = sort_order

    @property
    def states(self):
        """Gets the states of this ListDevInstancesRequest.  # noqa: E501


        :return: The states of this ListDevInstancesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._states

    @states.setter
    def states(self, states):
        """Sets the states of this ListDevInstancesRequest.


        :param states: The states of this ListDevInstancesRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Pending", "Deploying", "Running", "Stopping", "Stopped", "Deleting", "Abnormal", "Failed", "Upgrading"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(states).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `states` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(states) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._states = states

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
        if issubclass(ListDevInstancesRequest, dict):
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
        if not isinstance(other, ListDevInstancesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListDevInstancesRequest):
            return True

        return self.to_dict() != other.to_dict()
