#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import csv
from num2words import num2words
from unicodedata import normalize
from io import open

def vi_num2words(num):
   return num2words(num, lang='vi')

def convert_time_to_text(time_string):
   # Support only hh:mm format
   try:
       h, m = time_string.split(":")
       time_string = vi_num2words(int(h)) + " giờ " + vi_num2words(int(m)) + " phút"
       return time_string
   except:
       return None

def replace_time(text):
   # Define regex to time hh:mm
   result = re.findall(r'\d{1,2}:\d{1,2}|', text)
   match_list = list(filter(lambda x : len(x), result))

   for match in match_list:
       if convert_time_to_text(match):
           text = text.replace(match, convert_time_to_text(match))
   return text

def replace_number(text):
   return re.sub('(?P<id>\d+)', lambda m: vi_num2words(int(m.group('id'))), text)

def normalize_text(text):
   text = normalize("NFC", text)
   text = text.lower()
   text = replace_time(text)
   text = replace_number(text)
   return text.encode("utf-8")

f_obj = open('output.csv','rb')
g_obj = open('outputrefactor.csv','wb')
csv_reader = csv.reader(f_obj)
csv_writer = csv.writer(g_obj)

for line in csv_reader:
    textneed = line[0].split('|')[1]
    text = normalize_text(unicode(textneed, "utf-8"))
    textouput = line[0].split('|')[0] + '|' + text
    csv_writer.writerow([textouput])
