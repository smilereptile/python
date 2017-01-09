# -*-coding:utf8 -*
import yaml
import logging
import Singleton

__author__ = 'wingel-m'
logger = logging


class Config(object):

    __metaclass__ = Singleton

    def __init__(self, path=None):
        """
        Load a yaml config file
        :param path : path to config file
        :type path: str
        """

        try:
            self._conf = yaml.load(file(path, 'r'))

        except yaml.YAMLError as e:
            logger.error("Error when loading config file : %s", e)
            raise e

    def getValue(self, key):
        """
        Allows to get a value according to the set key
        :param key: the key to get the value
        :type key : str
        :return str : the value of the key
        """

        if key is None or key == '':
            raise KeyError("You must provide the key parameter")

        if self._conf is None:
            raise Exception("You must load the config file first")

        if key in self._conf:
            return self._conf[key]
        else:
            return None

    def setValue(self, key, value):
        """
        Allows to set a value to the key parameter
        :param key : the key
        :param value : the value to set on the key
        :type key : str
        :type value :str
        """

        if key is None or key == '':
            raise KeyError("You must provide the key parameter")

        if self._conf is None:
            raise Exception("You must load the conf file first")

        self._conf[key] = value
