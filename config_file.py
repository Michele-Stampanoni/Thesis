### Reading the config file 

import os 
from configparser import ConfigParser

pwd
os.chdir("C:/Users/27763/Documents/Masters/Thesis/Data")
pwd


## Inputting data into the config file 

config = ConfigParser()



# Nodes per country

config["africa_nodes"] = {
    1: 'Algeria',
    2: 'Egypt', 
    3: 'Morocco',
    4: 'Nigeria',
    5: "South Africa"}

config['asia_nodes'] = {
    1: 'China', 
    2: 'India', 
    3: 'Indonesia', 
    4: 'Japan', 
    5: 'Singapore', 
    6: 'Thailand', 
    7: 'Vietnam'}

config['eu_nodes'] = {
    1: 'Austria',
    2: 'Bulgaria', 
    3: 'France',
    4: "Germany", 
    5: 'Italy',
    6: 'Netherlands',
    7: 'Russia',
    8: 'Spain',
    9: 'United Kingdom'}

config['latam_nodes'] = {
    1: 'Argentina',
    2: 'Brazile', 
    3: 'Chile',
    4: 'Cololmiba', 
    5: 'Ecuador', 
    6: 'Mexico',
    7: 'Panama', 
    8: 'Peru'}

config['mideast_nodes'] = {
    1: 'Iraq', 
    2: 'Saudi Arabia', 
    3: 'Turkey'}

config['northam_nodes'] = {
    1:'Canada', 
    2: 'United States'}

config['oceania_nodes'] = {
    1: 'Australia', 
    2: 'Fiji', 
    3: 'New Zealand', 
    4: 'Papa New Guinea'}


# Number of nodes

config["no_nodes"] = {
    'africa':  9,
    'asia': 9,
    'europe': 8,
    'latin america': 9,
    'middle east': 9,
    'north america': 11,
    'oceania': 9,
    'global': 7
    }


# Network types

config['network_type'] = {
    1: 'test', 
    2: 'ordered',
    3: 'random'}



# Network values 

config['metcalfe_network_value'] = {
    'africa': '81',
    'asia': '81',
    'europe': '64',
    'latin america': '81',
    'middle east': '81',
    'north america': '121',
    'oceania': '81',
    'global': '49'
    }

config['reed_network_value'] = {
    'africa': '511',
    'asia': '511',
    'europe': '255',
    'latin america': '511',
    'middle east': '511',
    'north america': '2047',
    'oceania': '511',
    'global': '127'
    }


with open('input_data.ini', 'w') as file:
    config.write(file)


## Accessing the data
    
print(config.sections())
print(list(config['num_nodes']))
config['num_nodes']['africa']
config['num_nodes']['europe']    
    
    
print(config.sections())
print(config['metcalfe network value'])
print(list(config['metcalfe network value']))
print(config['metcalfe network value']['africa'])
for i in config['metcalfe network value']:  
    print(i)

print(config['reed network value'])
print(list(config['reed network value']))
print(config['reed network value']['africa'])
for i in config['reed network value']:  
    print(i)
    
    


    








