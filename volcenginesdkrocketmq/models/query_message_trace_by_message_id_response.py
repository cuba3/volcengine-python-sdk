# coding: utf-8

"""
    rocketmq

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class QueryMessageTraceByMessageIdResponse(object):
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
        'consumer_trace_infos': 'list[ConsumerTraceInfoForQueryMessageTraceByMessageIdOutput]',
        'producer_trace_info': 'list[ProducerTraceInfoForQueryMessageTraceByMessageIdOutput]'
    }

    attribute_map = {
        'consumer_trace_infos': 'ConsumerTraceInfos',
        'producer_trace_info': 'ProducerTraceInfo'
    }

    def __init__(self, consumer_trace_infos=None, producer_trace_info=None, _configuration=None):  # noqa: E501
        """QueryMessageTraceByMessageIdResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._consumer_trace_infos = None
        self._producer_trace_info = None
        self.discriminator = None

        if consumer_trace_infos is not None:
            self.consumer_trace_infos = consumer_trace_infos
        if producer_trace_info is not None:
            self.producer_trace_info = producer_trace_info

    @property
    def consumer_trace_infos(self):
        """Gets the consumer_trace_infos of this QueryMessageTraceByMessageIdResponse.  # noqa: E501


        :return: The consumer_trace_infos of this QueryMessageTraceByMessageIdResponse.  # noqa: E501
        :rtype: list[ConsumerTraceInfoForQueryMessageTraceByMessageIdOutput]
        """
        return self._consumer_trace_infos

    @consumer_trace_infos.setter
    def consumer_trace_infos(self, consumer_trace_infos):
        """Sets the consumer_trace_infos of this QueryMessageTraceByMessageIdResponse.


        :param consumer_trace_infos: The consumer_trace_infos of this QueryMessageTraceByMessageIdResponse.  # noqa: E501
        :type: list[ConsumerTraceInfoForQueryMessageTraceByMessageIdOutput]
        """

        self._consumer_trace_infos = consumer_trace_infos

    @property
    def producer_trace_info(self):
        """Gets the producer_trace_info of this QueryMessageTraceByMessageIdResponse.  # noqa: E501


        :return: The producer_trace_info of this QueryMessageTraceByMessageIdResponse.  # noqa: E501
        :rtype: list[ProducerTraceInfoForQueryMessageTraceByMessageIdOutput]
        """
        return self._producer_trace_info

    @producer_trace_info.setter
    def producer_trace_info(self, producer_trace_info):
        """Sets the producer_trace_info of this QueryMessageTraceByMessageIdResponse.


        :param producer_trace_info: The producer_trace_info of this QueryMessageTraceByMessageIdResponse.  # noqa: E501
        :type: list[ProducerTraceInfoForQueryMessageTraceByMessageIdOutput]
        """

        self._producer_trace_info = producer_trace_info

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
        if issubclass(QueryMessageTraceByMessageIdResponse, dict):
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
        if not isinstance(other, QueryMessageTraceByMessageIdResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryMessageTraceByMessageIdResponse):
            return True

        return self.to_dict() != other.to_dict()
