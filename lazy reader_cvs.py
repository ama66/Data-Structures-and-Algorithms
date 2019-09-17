#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import os
import psutil
from collections import OrderedDict 


class Lazy_Read_Csv:
    """ a class to read in humungous csv file , group it by entity (like country) and dump each
    group data to a single csv file ..."""
    
    def __init__(self,file_path):
        self.file_path=file_path
        self.f=open(file_path) 
        self.gen=self._lazy_read()
        self.header=next(self.gen)
        self.countrydic=self._gen_unique_keys_dic()
        print("Input File Contains the following Countries:")
        print("UniqueCountry-----Number of rows")
        print(self.welldic)
            
    def _lazy_read(self):
        """A function to read a large csv file lazily. Returns a "row" generator """
        while True:
            row = self.f.readline()
            if not row:
                break
            yield row
            
    def _gen_unique_keys_dic(self):
        dic= OrderedDict() 
        for line in self.gen:
        ""Extract column from the stream then split it based on - " 
             country_name=line.split(",")[4].split("-")[0]
            
            if country_name in dic:
                dic[country_name] += 1
            else:
                dic[country_name] = 1
        return dic
    
    def dump_csv(self):
        
        List_of_Countries=list(self.countrydic)
        
        sumofrows=0
        skip_rows=0 
        
        for i in range(len(List_of_Countries)):
            ## Chunk to be read
            Num_rows=LR.countrydic[List_of_Countries[i]]

            if i==0:
                skip_rows=1
            else:
                ## Previous Chunk size
                Num_Prev_rows=LR.countrydic[List_of_Countries[i-1]]
                ## Update sum of rows to skip by adding previous chunk
                sumofrows+=Num_Prev_rows
                skip_rows=sumofrows+1 
                
               
            df=pd.read_csv(self.file_path,header=None, skiprows= skip_rows, nrows=Num_rows)
            file_name=os.path.dirname(self.file_path)+"/"+List_of_Countries[i]+"_Data.csv"
            print("Now Dumping CSV file ", file_name) 
            print("With Number of rows= ", len(df))
            df.to_csv(file_name)
            print("Now Dumping CSV file ", file_name, "Done!") 
                


# In[3]:


file_path="/Users/Ammar/FlightDataPerCountry.csv"



LR=Lazy_Read_Csv(file_path)
LR.dump_csv()

process = psutil.Process(os.getpid())
print("Current Memory usage in GB ", process.memory_info().rss/1e9)   





