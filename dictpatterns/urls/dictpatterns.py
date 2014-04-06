from django.conf.urls import url
from django.utils import six

import re

class DictPatterns(object):

    def __init__(self, kwargs):

        self.dict = kwargs
        self.pattern_list = []

    def __recursion(self, base_regex, partial_dict):

        for k, v in partial_dict.items():
            if isinstance(v, (list, tuple)) and not v[0] is None:
                if isinstance(v[0], six.string_types):
                    v_url = url(base_regex + k + '$', v[0], name=v[1])
                    self.pattern_list.append(v_url)
                else:
                    v_url = url(base_regex + k, v[0], name=v[1])
                    self.pattern_list.append(v_url)
            if len(v) == 3:
                self.__recursion(base_regex + k, v[2])

    def __regex_parent_recursion(self, base_regex, partial_dict, parent_name):

        if self.parent:
            return

        for k, v in partial_dict.items():
            if isinstance(v, (list, tuple)):
                matched = re.compile(base_regex + k + '$').match(self.url)
                if matched:
                    parent_mached = re.compile(base_regex).match(self.url)
                    self.parent = parent_name
                    self.args = parent_mached.groups()
                elif len(v) == 3:
                    self.__regex_parent_recursion(base_regex + k, v[2], v[0])

    def to_patterns(self):

        self.__recursion("", self.dict)
        return self.pattern_list

    def find_parent_url(self, url):

        self.parent = ""
        self.args = ""
        self.url = url
        self.__regex_parent_recursion("", self.dict, "")

        v = {
            "name": self.parent,
            "args": self.args,
            }

        return v
