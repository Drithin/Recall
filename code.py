# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import rake
import operator
import csv
from collections import defaultdict



rake_object = rake.Rake("SmartStoplist.txt", 3, 3, 1)
text = " Python is prerequisite of big data "
keywords = rake_object.run(text)

f = defaultdict(list)

for n,v in keywords:
 f[n].append(v)

g = max(f, key=f.get)

with open("tags.csv") as file:
   reader = csv.reader(file)
   
   for row in reader:
          for i in row:
               if g == i:
                   print i
    