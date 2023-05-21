# -*- coding: utf-8 -*-
"""
Created on Thu May  6 23:32:15 2021


//
@author: Shubh
"""
#%%
import requests
import xml.etree.ElementTree as ET
import re 
import pandas as pd
import numpy as np 
from datetime import datetime
#import dateparser

headers={'User-Agent': 'Mozilla/5.0'}
#headers above make sure the scrapper is blocked by antiscrapper bots on the SEC website. 

terms_df = pd.read_excel(r'/Users/shubhpatel/Documents/SEC_filing_terms_library.xlsx')
xml_terms = terms_df['elementName'].tolist()
terms = terms_df['elementLabel'].tolist()

#%%
#basically a list of all the possible attributes of financial data listed on a excel file.

initial_frame = {'XML Terms': xml_terms, 'Full Terms': terms}

main_data = pd.DataFrame(initial_frame)

text = requests.get("https://www.sec.gov/Archives/edgar/data/1629210/0001564590-21-004382.txt", headers=headers).text

regex = r"\<\?xml(\s\S*)+</XBRL>"

x = re.search("\<\?xml(\s\S*?)+</xbrli:xbrl>", text, re.MULTILINE | re.IGNORECASE | re.DOTALL).group()
#</xbrli:xbrl>
out = open("testxml.xml","w+")
out.write(x)


tree = ET.parse('testxml.xml')
root = tree.getroot()

file_xml = []
file_values = []
period_start = []
period_end = []


#%%

for child in root: 
    for i in xml_terms:
        if i in child.tag: 
            file_xml.append(i)
            file_values.append(child.text)
            date_regex = r"(?<!\d)(\d{8})(?!\d)"
            collect_date = re.findall(date_regex, child.attrib['contextRef'])
            try:
                res1 = datetime.strptime(collect_date[0], '%Y%m%d').date()
                res2 = datetime.strptime(collect_date[1], '%Y%m%d').date()
                period_start.append(res1)
                period_end.append(res2)

            except:
                res1 = datetime.strptime(collect_date[0], '%Y%m%d').date()
                period_start.append(res1)
                period_start.append("NA")
            

            

data_tuples = list(zip(file_xml, file_values, period_start, period_end))

df = pd.DataFrame(data_tuples, columns=['XML Terms', 'Values', 'Period Start', 'Period End' ])



   # obtains the tag which is the relevant information
