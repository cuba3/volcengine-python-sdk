# coding: utf-8

"""
    vefaas

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ItemForListFunctionsOutput(object):
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
        'code_size': 'int',
        'code_size_limit': 'int',
        'command': 'str',
        'cpu_strategy': 'str',
        'creation_time': 'str',
        'description': 'str',
        'envs': 'list[EnvForListFunctionsOutput]',
        'exclusive_mode': 'bool',
        'id': 'str',
        'initializer_sec': 'int',
        'instance_type': 'str',
        'last_update_time': 'str',
        'max_concurrency': 'int',
        'memory_mb': 'int',
        'name': 'str',
        'nas_storage': 'NasStorageForListFunctionsOutput',
        'owner': 'str',
        'port': 'int',
        'project_name': 'str',
        'request_timeout': 'int',
        'runtime': 'str',
        'source_location': 'str',
        'source_type': 'str',
        'tags': 'list[TagForListFunctionsOutput]',
        'tls_config': 'TlsConfigForListFunctionsOutput',
        'tos_mount_config': 'TosMountConfigForListFunctionsOutput',
        'triggers_count': 'int',
        'vpc_config': 'VpcConfigForListFunctionsOutput'
    }

    attribute_map = {
        'code_size': 'CodeSize',
        'code_size_limit': 'CodeSizeLimit',
        'command': 'Command',
        'cpu_strategy': 'CpuStrategy',
        'creation_time': 'CreationTime',
        'description': 'Description',
        'envs': 'Envs',
        'exclusive_mode': 'ExclusiveMode',
        'id': 'Id',
        'initializer_sec': 'InitializerSec',
        'instance_type': 'InstanceType',
        'last_update_time': 'LastUpdateTime',
        'max_concurrency': 'MaxConcurrency',
        'memory_mb': 'MemoryMB',
        'name': 'Name',
        'nas_storage': 'NasStorage',
        'owner': 'Owner',
        'port': 'Port',
        'project_name': 'ProjectName',
        'request_timeout': 'RequestTimeout',
        'runtime': 'Runtime',
        'source_location': 'SourceLocation',
        'source_type': 'SourceType',
        'tags': 'Tags',
        'tls_config': 'TlsConfig',
        'tos_mount_config': 'TosMountConfig',
        'triggers_count': 'TriggersCount',
        'vpc_config': 'VpcConfig'
    }

    def __init__(self, code_size=None, code_size_limit=None, command=None, cpu_strategy=None, creation_time=None, description=None, envs=None, exclusive_mode=None, id=None, initializer_sec=None, instance_type=None, last_update_time=None, max_concurrency=None, memory_mb=None, name=None, nas_storage=None, owner=None, port=None, project_name=None, request_timeout=None, runtime=None, source_location=None, source_type=None, tags=None, tls_config=None, tos_mount_config=None, triggers_count=None, vpc_config=None, _configuration=None):  # noqa: E501
        """ItemForListFunctionsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._code_size = None
        self._code_size_limit = None
        self._command = None
        self._cpu_strategy = None
        self._creation_time = None
        self._description = None
        self._envs = None
        self._exclusive_mode = None
        self._id = None
        self._initializer_sec = None
        self._instance_type = None
        self._last_update_time = None
        self._max_concurrency = None
        self._memory_mb = None
        self._name = None
        self._nas_storage = None
        self._owner = None
        self._port = None
        self._project_name = None
        self._request_timeout = None
        self._runtime = None
        self._source_location = None
        self._source_type = None
        self._tags = None
        self._tls_config = None
        self._tos_mount_config = None
        self._triggers_count = None
        self._vpc_config = None
        self.discriminator = None

        if code_size is not None:
            self.code_size = code_size
        if code_size_limit is not None:
            self.code_size_limit = code_size_limit
        if command is not None:
            self.command = command
        if cpu_strategy is not None:
            self.cpu_strategy = cpu_strategy
        if creation_time is not None:
            self.creation_time = creation_time
        if description is not None:
            self.description = description
        if envs is not None:
            self.envs = envs
        if exclusive_mode is not None:
            self.exclusive_mode = exclusive_mode
        if id is not None:
            self.id = id
        if initializer_sec is not None:
            self.initializer_sec = initializer_sec
        if instance_type is not None:
            self.instance_type = instance_type
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if max_concurrency is not None:
            self.max_concurrency = max_concurrency
        if memory_mb is not None:
            self.memory_mb = memory_mb
        if name is not None:
            self.name = name
        if nas_storage is not None:
            self.nas_storage = nas_storage
        if owner is not None:
            self.owner = owner
        if port is not None:
            self.port = port
        if project_name is not None:
            self.project_name = project_name
        if request_timeout is not None:
            self.request_timeout = request_timeout
        if runtime is not None:
            self.runtime = runtime
        if source_location is not None:
            self.source_location = source_location
        if source_type is not None:
            self.source_type = source_type
        if tags is not None:
            self.tags = tags
        if tls_config is not None:
            self.tls_config = tls_config
        if tos_mount_config is not None:
            self.tos_mount_config = tos_mount_config
        if triggers_count is not None:
            self.triggers_count = triggers_count
        if vpc_config is not None:
            self.vpc_config = vpc_config

    @property
    def code_size(self):
        """Gets the code_size of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The code_size of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: int
        """
        return self._code_size

    @code_size.setter
    def code_size(self, code_size):
        """Sets the code_size of this ItemForListFunctionsOutput.


        :param code_size: The code_size of this ItemForListFunctionsOutput.  # noqa: E501
        :type: int
        """

        self._code_size = code_size

    @property
    def code_size_limit(self):
        """Gets the code_size_limit of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The code_size_limit of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: int
        """
        return self._code_size_limit

    @code_size_limit.setter
    def code_size_limit(self, code_size_limit):
        """Sets the code_size_limit of this ItemForListFunctionsOutput.


        :param code_size_limit: The code_size_limit of this ItemForListFunctionsOutput.  # noqa: E501
        :type: int
        """

        self._code_size_limit = code_size_limit

    @property
    def command(self):
        """Gets the command of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The command of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this ItemForListFunctionsOutput.


        :param command: The command of this ItemForListFunctionsOutput.  # noqa: E501
        :type: str
        """

        self._command = command

    @property
    def cpu_strategy(self):
        """Gets the cpu_strategy of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The cpu_strategy of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._cpu_strategy

    @cpu_strategy.setter
    def cpu_strategy(self, cpu_strategy):
        """Sets the cpu_strategy of this ItemForListFunctionsOutput.


        :param cpu_strategy: The cpu_strategy of this ItemForListFunctionsOutput.  # noqa: E501
        :type: str
        """

        self._cpu_strategy = cpu_strategy

    @property
    def creation_time(self):
        """Gets the creation_time of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The creation_time of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this ItemForListFunctionsOutput.


        :param creation_time: The creation_time of this ItemForListFunctionsOutput.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def description(self):
        """Gets the description of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The description of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ItemForListFunctionsOutput.


        :param description: The description of this ItemForListFunctionsOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def envs(self):
        """Gets the envs of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The envs of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: list[EnvForListFunctionsOutput]
        """
        return self._envs

    @envs.setter
    def envs(self, envs):
        """Sets the envs of this ItemForListFunctionsOutput.


        :param envs: The envs of this ItemForListFunctionsOutput.  # noqa: E501
        :type: list[EnvForListFunctionsOutput]
        """

        self._envs = envs

    @property
    def exclusive_mode(self):
        """Gets the exclusive_mode of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The exclusive_mode of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: bool
        """
        return self._exclusive_mode

    @exclusive_mode.setter
    def exclusive_mode(self, exclusive_mode):
        """Sets the exclusive_mode of this ItemForListFunctionsOutput.


        :param exclusive_mode: The exclusive_mode of this ItemForListFunctionsOutput.  # noqa: E501
        :type: bool
        """

        self._exclusive_mode = exclusive_mode

    @property
    def id(self):
        """Gets the id of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The id of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ItemForListFunctionsOutput.


        :param id: The id of this ItemForListFunctionsOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def initializer_sec(self):
        """Gets the initializer_sec of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The initializer_sec of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: int
        """
        return self._initializer_sec

    @initializer_sec.setter
    def initializer_sec(self, initializer_sec):
        """Sets the initializer_sec of this ItemForListFunctionsOutput.


        :param initializer_sec: The initializer_sec of this ItemForListFunctionsOutput.  # noqa: E501
        :type: int
        """

        self._initializer_sec = initializer_sec

    @property
    def instance_type(self):
        """Gets the instance_type of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The instance_type of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this ItemForListFunctionsOutput.


        :param instance_type: The instance_type of this ItemForListFunctionsOutput.  # noqa: E501
        :type: str
        """

        self._instance_type = instance_type

    @property
    def last_update_time(self):
        """Gets the last_update_time of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The last_update_time of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this ItemForListFunctionsOutput.


        :param last_update_time: The last_update_time of this ItemForListFunctionsOutput.  # noqa: E501
        :type: str
        """

        self._last_update_time = last_update_time

    @property
    def max_concurrency(self):
        """Gets the max_concurrency of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The max_concurrency of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: int
        """
        return self._max_concurrency

    @max_concurrency.setter
    def max_concurrency(self, max_concurrency):
        """Sets the max_concurrency of this ItemForListFunctionsOutput.


        :param max_concurrency: The max_concurrency of this ItemForListFunctionsOutput.  # noqa: E501
        :type: int
        """

        self._max_concurrency = max_concurrency

    @property
    def memory_mb(self):
        """Gets the memory_mb of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The memory_mb of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: int
        """
        return self._memory_mb

    @memory_mb.setter
    def memory_mb(self, memory_mb):
        """Sets the memory_mb of this ItemForListFunctionsOutput.


        :param memory_mb: The memory_mb of this ItemForListFunctionsOutput.  # noqa: E501
        :type: int
        """

        self._memory_mb = memory_mb

    @property
    def name(self):
        """Gets the name of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The name of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ItemForListFunctionsOutput.


        :param name: The name of this ItemForListFunctionsOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def nas_storage(self):
        """Gets the nas_storage of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The nas_storage of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: NasStorageForListFunctionsOutput
        """
        return self._nas_storage

    @nas_storage.setter
    def nas_storage(self, nas_storage):
        """Sets the nas_storage of this ItemForListFunctionsOutput.


        :param nas_storage: The nas_storage of this ItemForListFunctionsOutput.  # noqa: E501
        :type: NasStorageForListFunctionsOutput
        """

        self._nas_storage = nas_storage

    @property
    def owner(self):
        """Gets the owner of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The owner of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ItemForListFunctionsOutput.


        :param owner: The owner of this ItemForListFunctionsOutput.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def port(self):
        """Gets the port of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The port of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ItemForListFunctionsOutput.


        :param port: The port of this ItemForListFunctionsOutput.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def project_name(self):
        """Gets the project_name of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The project_name of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ItemForListFunctionsOutput.


        :param project_name: The project_name of this ItemForListFunctionsOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def request_timeout(self):
        """Gets the request_timeout of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The request_timeout of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: int
        """
        return self._request_timeout

    @request_timeout.setter
    def request_timeout(self, request_timeout):
        """Sets the request_timeout of this ItemForListFunctionsOutput.


        :param request_timeout: The request_timeout of this ItemForListFunctionsOutput.  # noqa: E501
        :type: int
        """

        self._request_timeout = request_timeout

    @property
    def runtime(self):
        """Gets the runtime of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The runtime of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this ItemForListFunctionsOutput.


        :param runtime: The runtime of this ItemForListFunctionsOutput.  # noqa: E501
        :type: str
        """

        self._runtime = runtime

    @property
    def source_location(self):
        """Gets the source_location of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The source_location of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._source_location

    @source_location.setter
    def source_location(self, source_location):
        """Sets the source_location of this ItemForListFunctionsOutput.


        :param source_location: The source_location of this ItemForListFunctionsOutput.  # noqa: E501
        :type: str
        """

        self._source_location = source_location

    @property
    def source_type(self):
        """Gets the source_type of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The source_type of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this ItemForListFunctionsOutput.


        :param source_type: The source_type of this ItemForListFunctionsOutput.  # noqa: E501
        :type: str
        """

        self._source_type = source_type

    @property
    def tags(self):
        """Gets the tags of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The tags of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: list[TagForListFunctionsOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ItemForListFunctionsOutput.


        :param tags: The tags of this ItemForListFunctionsOutput.  # noqa: E501
        :type: list[TagForListFunctionsOutput]
        """

        self._tags = tags

    @property
    def tls_config(self):
        """Gets the tls_config of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The tls_config of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: TlsConfigForListFunctionsOutput
        """
        return self._tls_config

    @tls_config.setter
    def tls_config(self, tls_config):
        """Sets the tls_config of this ItemForListFunctionsOutput.


        :param tls_config: The tls_config of this ItemForListFunctionsOutput.  # noqa: E501
        :type: TlsConfigForListFunctionsOutput
        """

        self._tls_config = tls_config

    @property
    def tos_mount_config(self):
        """Gets the tos_mount_config of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The tos_mount_config of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: TosMountConfigForListFunctionsOutput
        """
        return self._tos_mount_config

    @tos_mount_config.setter
    def tos_mount_config(self, tos_mount_config):
        """Sets the tos_mount_config of this ItemForListFunctionsOutput.


        :param tos_mount_config: The tos_mount_config of this ItemForListFunctionsOutput.  # noqa: E501
        :type: TosMountConfigForListFunctionsOutput
        """

        self._tos_mount_config = tos_mount_config

    @property
    def triggers_count(self):
        """Gets the triggers_count of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The triggers_count of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: int
        """
        return self._triggers_count

    @triggers_count.setter
    def triggers_count(self, triggers_count):
        """Sets the triggers_count of this ItemForListFunctionsOutput.


        :param triggers_count: The triggers_count of this ItemForListFunctionsOutput.  # noqa: E501
        :type: int
        """

        self._triggers_count = triggers_count

    @property
    def vpc_config(self):
        """Gets the vpc_config of this ItemForListFunctionsOutput.  # noqa: E501


        :return: The vpc_config of this ItemForListFunctionsOutput.  # noqa: E501
        :rtype: VpcConfigForListFunctionsOutput
        """
        return self._vpc_config

    @vpc_config.setter
    def vpc_config(self, vpc_config):
        """Sets the vpc_config of this ItemForListFunctionsOutput.


        :param vpc_config: The vpc_config of this ItemForListFunctionsOutput.  # noqa: E501
        :type: VpcConfigForListFunctionsOutput
        """

        self._vpc_config = vpc_config

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
        if issubclass(ItemForListFunctionsOutput, dict):
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
        if not isinstance(other, ItemForListFunctionsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemForListFunctionsOutput):
            return True

        return self.to_dict() != other.to_dict()
