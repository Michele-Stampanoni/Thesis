### Data imported from the TG Excel files  

import pandas as pd 
import numpy as np 
from matplotlib.pyplot import figure


### Loading the TG data from the excel files  
net_eu = pd.read_excel("C:/Users/27763/Documents/Masters/Thesis/Data/gig_re_country2country_europe.xlsx")
net_us = pd.read_excel("C:/Users/27763/Documents/Masters/Thesis/Data/gig_re_country2country_na.xlsx")
net_la = pd.read_excel("C:/Users/27763/Documents/Masters/Thesis/Data/gig_re_country2country_la.xlsx")
net_africa = pd.read_excel("C:/Users/27763/Documents/Masters/Thesis/Data/gig_re_country2country_africa.xlsx")
    


### Defining the edges as functions so they can be used in the class object, 
### but it doesnt run smoothly as of yet

def edges_eu():
    return net_eu[["Node1", "Node2", "Weight"]]

def edges_us():
    return net_us[["Node1", "Node2", "Weight"]]

def edges_la():
    return net_la[["Node1", "Node2", "Weight"]]

def edges_africa():
    return net_africa[["Node1", "Node2", "Weight"]]





