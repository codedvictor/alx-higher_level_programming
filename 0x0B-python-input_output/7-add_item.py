#!/usr/bin/python3
"""Defines scripts that add all argument
   list and save them to a file
"""
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

myList = []
if os.path.exists('add_item.json'):
    myList = load_from_json_file('add_item.json')

for argt in sys.argv[1:]:
    myList.append(argt)

save_to_json_file(myList, 'add_item.json')
