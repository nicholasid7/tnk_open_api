# coding: utf-8

"""
    OpenAPI

    tinkoff.ru/invest OpenAPI.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: n.v.melnikov@tinkoff.ru
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Candle(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'figi': 'str',
        'interval': 'CandleResolution',
        'o': 'float',
        'c': 'float',
        'h': 'float',
        'l': 'float',
        'v': 'int',
        'time': 'datetime'
    }

    attribute_map = {
        'figi': 'figi',
        'interval': 'interval',
        'o': 'o',
        'c': 'c',
        'h': 'h',
        'l': 'l',
        'v': 'v',
        'time': 'time'
    }

    def __init__(self, figi=None, interval=None, o=None, c=None, h=None, l=None, v=None, time=None):  # noqa: E501
        """Candle - a model defined in OpenAPI"""  # noqa: E501

        self._figi = None
        self._interval = None
        self._o = None
        self._c = None
        self._h = None
        self._l = None
        self._v = None
        self._time = None
        self.discriminator = None

        self.figi = figi
        self.interval = interval
        self.o = o
        self.c = c
        self.h = h
        self.l = l
        self.v = v
        self.time = time

    @property
    def figi(self):
        """Gets the figi of this Candle.  # noqa: E501


        :return: The figi of this Candle.  # noqa: E501
        :rtype: str
        """
        return self._figi

    @figi.setter
    def figi(self, figi):
        """Sets the figi of this Candle.


        :param figi: The figi of this Candle.  # noqa: E501
        :type: str
        """
        if figi is None:
            raise ValueError("Invalid value for `figi`, must not be `None`")  # noqa: E501

        self._figi = figi

    @property
    def interval(self):
        """Gets the interval of this Candle.  # noqa: E501


        :return: The interval of this Candle.  # noqa: E501
        :rtype: CandleResolution
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this Candle.


        :param interval: The interval of this Candle.  # noqa: E501
        :type: CandleResolution
        """
        if interval is None:
            raise ValueError("Invalid value for `interval`, must not be `None`")  # noqa: E501

        self._interval = interval

    @property
    def o(self):
        """Gets the o of this Candle.  # noqa: E501


        :return: The o of this Candle.  # noqa: E501
        :rtype: float
        """
        return self._o

    @o.setter
    def o(self, o):
        """Sets the o of this Candle.


        :param o: The o of this Candle.  # noqa: E501
        :type: float
        """
        if o is None:
            raise ValueError("Invalid value for `o`, must not be `None`")  # noqa: E501

        self._o = o

    @property
    def c(self):
        """Gets the c of this Candle.  # noqa: E501


        :return: The c of this Candle.  # noqa: E501
        :rtype: float
        """
        return self._c

    @c.setter
    def c(self, c):
        """Sets the c of this Candle.


        :param c: The c of this Candle.  # noqa: E501
        :type: float
        """
        if c is None:
            raise ValueError("Invalid value for `c`, must not be `None`")  # noqa: E501

        self._c = c

    @property
    def h(self):
        """Gets the h of this Candle.  # noqa: E501


        :return: The h of this Candle.  # noqa: E501
        :rtype: float
        """
        return self._h

    @h.setter
    def h(self, h):
        """Sets the h of this Candle.


        :param h: The h of this Candle.  # noqa: E501
        :type: float
        """
        if h is None:
            raise ValueError("Invalid value for `h`, must not be `None`")  # noqa: E501

        self._h = h

    @property
    def l(self):
        """Gets the l of this Candle.  # noqa: E501


        :return: The l of this Candle.  # noqa: E501
        :rtype: float
        """
        return self._l

    @l.setter
    def l(self, l):
        """Sets the l of this Candle.


        :param l: The l of this Candle.  # noqa: E501
        :type: float
        """
        if l is None:
            raise ValueError("Invalid value for `l`, must not be `None`")  # noqa: E501

        self._l = l

    @property
    def v(self):
        """Gets the v of this Candle.  # noqa: E501


        :return: The v of this Candle.  # noqa: E501
        :rtype: int
        """
        return self._v

    @v.setter
    def v(self, v):
        """Sets the v of this Candle.


        :param v: The v of this Candle.  # noqa: E501
        :type: int
        """
        if v is None:
            raise ValueError("Invalid value for `v`, must not be `None`")  # noqa: E501

        self._v = v

    @property
    def time(self):
        """Gets the time of this Candle.  # noqa: E501

        ISO8601  # noqa: E501

        :return: The time of this Candle.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Candle.

        ISO8601  # noqa: E501

        :param time: The time of this Candle.  # noqa: E501
        :type: datetime
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Candle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
