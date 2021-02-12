### Data imported from the TG Excel files  

import pandas as pd 
import numpy as np 
from matplotlib.pyplot import figure


### Loading the TG data from the excel files  
net_eu = pd.read_excel("C:/Users/27763/Documents/Masters/Thesis/Data/gig_re_country2country_europe.xlsx")
net_us = pd.read_excel("C:/Users/27763/Documents/Masters/Thesis/Data/gig_re_country2country_na.xlsx")
net_la = pd.read_excel("C:/Users/27763/Documents/Masters/Thesis/Data/gig_re_country2country_la.xlsx")
net_africa = pd.read_excel("C:/Users/27763/Documents/Masters/Thesis/Data/gig_re_country2country_africa.xlsx")
    


### Below functions are defined to extract the edges for each region. 
### Tried to call these functions in the Graph Class in network_oop.py, but to no avail. 

def edges_eu():
    return net_eu[["Node1", "Node2", "Weight"]]

def edges_us():
    return net_us[["Node1", "Node2", "Weight"]]

def edges_la():
    return net_la[["Node1", "Node2", "Weight"]]

def edges_africa():
    return net_africa[["Node1", "Node2", "Weight"]]





