# -*- coding:utf-8 -*-

import re

rel = re.compile('a*ba')
for item in rel.finditer('abaccacbacbacabcabbacbbbbacbacbacb'):
    #print(item.span())
    #print(item.group())
    pass


rel2 = re.compile('21[1-5]\d{7}')
num = '2110505109'

if re.fullmatch(rel2,num):
    print('right')
else:
    print('wrong')