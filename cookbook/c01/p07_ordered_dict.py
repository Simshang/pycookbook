#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 排序字典
Desc : 
"""

from collections import OrderedDict
import json


d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

# order test
d['foo'] = 5

# Outputs "foo 1", "bar 2", "spam 3", "grok 4"

for key in d:
    print(key, d[key])

d_j = json.dumps(d)

print(d_j)


