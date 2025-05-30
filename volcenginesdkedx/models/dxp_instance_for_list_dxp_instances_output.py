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


class DXPInstanceForListDXPInstancesOutput(object):
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
        'ap': 'str',
        'advice': 'str',
        'area': 'str',
        'auto_renew': 'bool',
        'bandwidth': 'int',
        'begin_time': 'str',
        'end_time': 'str',
        'health_status': 'bool',
        'isp': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'module_type': 'str',
        'monthly_rent_id': 'str',
        'port_fee_id': 'str',
        'port_type': 'str',
        'status': 'str'
    }

    attribute_map = {
        'ap': 'AP',
        'advice': 'Advice',
        'area': 'Area',
        'auto_renew': 'AutoRenew',
        'bandwidth': 'Bandwidth',
        'begin_time': 'BeginTime',
        'end_time': 'EndTime',
        'health_status': 'HealthStatus',
        'isp': 'ISP',
        'instance_id': 'InstanceId',
        'instance_name': 'InstanceName',
        'module_type': 'ModuleType',
        'monthly_rent_id': 'MonthlyRentId',
        'port_fee_id': 'PortFeeId',
        'port_type': 'PortType',
        'status': 'Status'
    }

    def __init__(self, ap=None, advice=None, area=None, auto_renew=None, bandwidth=None, begin_time=None, end_time=None, health_status=None, isp=None, instance_id=None, instance_name=None, module_type=None, monthly_rent_id=None, port_fee_id=None, port_type=None, status=None, _configuration=None):  # noqa: E501
        """DXPInstanceForListDXPInstancesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ap = None
        self._advice = None
        self._area = None
        self._auto_renew = None
        self._bandwidth = None
        self._begin_time = None
        self._end_time = None
        self._health_status = None
        self._isp = None
        self._instance_id = None
        self._instance_name = None
        self._module_type = None
        self._monthly_rent_id = None
        self._port_fee_id = None
        self._port_type = None
        self._status = None
        self.discriminator = None

        if ap is not None:
            self.ap = ap
        if advice is not None:
            self.advice = advice
        if area is not None:
            self.area = area
        if auto_renew is not None:
            self.auto_renew = auto_renew
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if health_status is not None:
            self.health_status = health_status
        if isp is not None:
            self.isp = isp
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if module_type is not None:
            self.module_type = module_type
        if monthly_rent_id is not None:
            self.monthly_rent_id = monthly_rent_id
        if port_fee_id is not None:
            self.port_fee_id = port_fee_id
        if port_type is not None:
            self.port_type = port_type
        if status is not None:
            self.status = status

    @property
    def ap(self):
        """Gets the ap of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501


        :return: The ap of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._ap

    @ap.setter
    def ap(self, ap):
        """Sets the ap of this DXPInstanceForListDXPInstancesOutput.


        :param ap: The ap of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :type: str
        """

        self._ap = ap

    @property
    def advice(self):
        """Gets the advice of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501


        :return: The advice of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._advice

    @advice.setter
    def advice(self, advice):
        """Sets the advice of this DXPInstanceForListDXPInstancesOutput.


        :param advice: The advice of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :type: str
        """

        self._advice = advice

    @property
    def area(self):
        """Gets the area of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501


        :return: The area of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this DXPInstanceForListDXPInstancesOutput.


        :param area: The area of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :type: str
        """

        self._area = area

    @property
    def auto_renew(self):
        """Gets the auto_renew of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501


        :return: The auto_renew of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this DXPInstanceForListDXPInstancesOutput.


        :param auto_renew: The auto_renew of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :type: bool
        """

        self._auto_renew = auto_renew

    @property
    def bandwidth(self):
        """Gets the bandwidth of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501


        :return: The bandwidth of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this DXPInstanceForListDXPInstancesOutput.


        :param bandwidth: The bandwidth of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :type: int
        """

        self._bandwidth = bandwidth

    @property
    def begin_time(self):
        """Gets the begin_time of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501


        :return: The begin_time of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this DXPInstanceForListDXPInstancesOutput.


        :param begin_time: The begin_time of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :type: str
        """

        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501


        :return: The end_time of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DXPInstanceForListDXPInstancesOutput.


        :param end_time: The end_time of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def health_status(self):
        """Gets the health_status of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501


        :return: The health_status of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._health_status

    @health_status.setter
    def health_status(self, health_status):
        """Sets the health_status of this DXPInstanceForListDXPInstancesOutput.


        :param health_status: The health_status of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :type: bool
        """

        self._health_status = health_status

    @property
    def isp(self):
        """Gets the isp of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501


        :return: The isp of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this DXPInstanceForListDXPInstancesOutput.


        :param isp: The isp of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :type: str
        """

        self._isp = isp

    @property
    def instance_id(self):
        """Gets the instance_id of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501


        :return: The instance_id of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DXPInstanceForListDXPInstancesOutput.


        :param instance_id: The instance_id of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501


        :return: The instance_name of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this DXPInstanceForListDXPInstancesOutput.


        :param instance_name: The instance_name of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def module_type(self):
        """Gets the module_type of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501


        :return: The module_type of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._module_type

    @module_type.setter
    def module_type(self, module_type):
        """Sets the module_type of this DXPInstanceForListDXPInstancesOutput.


        :param module_type: The module_type of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :type: str
        """

        self._module_type = module_type

    @property
    def monthly_rent_id(self):
        """Gets the monthly_rent_id of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501


        :return: The monthly_rent_id of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._monthly_rent_id

    @monthly_rent_id.setter
    def monthly_rent_id(self, monthly_rent_id):
        """Sets the monthly_rent_id of this DXPInstanceForListDXPInstancesOutput.


        :param monthly_rent_id: The monthly_rent_id of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :type: str
        """

        self._monthly_rent_id = monthly_rent_id

    @property
    def port_fee_id(self):
        """Gets the port_fee_id of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501


        :return: The port_fee_id of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._port_fee_id

    @port_fee_id.setter
    def port_fee_id(self, port_fee_id):
        """Sets the port_fee_id of this DXPInstanceForListDXPInstancesOutput.


        :param port_fee_id: The port_fee_id of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :type: str
        """

        self._port_fee_id = port_fee_id

    @property
    def port_type(self):
        """Gets the port_type of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501


        :return: The port_type of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._port_type

    @port_type.setter
    def port_type(self, port_type):
        """Sets the port_type of this DXPInstanceForListDXPInstancesOutput.


        :param port_type: The port_type of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :type: str
        """

        self._port_type = port_type

    @property
    def status(self):
        """Gets the status of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501


        :return: The status of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DXPInstanceForListDXPInstancesOutput.


        :param status: The status of this DXPInstanceForListDXPInstancesOutput.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(DXPInstanceForListDXPInstancesOutput, dict):
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
        if not isinstance(other, DXPInstanceForListDXPInstancesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DXPInstanceForListDXPInstancesOutput):
            return True

        return self.to_dict() != other.to_dict()
