### Reading the config file 

from configparser import ConfigParser

## Inputting data into the config file 

config = ConfigParser()


config['metcalfe network value'] = {
    'africa': '81',
    'asia': '81',
    'europe': '64',
    'latin america': '81',
    'middle east': '81',
    'north america': '121',
    'oceania': '81',
    'global': '49'
    }

config['reed network value'] = {
    'africa': '511',
    'asia': '511',
    'europe': '255',
    'latin america': '511',
    'middle east': '511',
    'north america': '2047',
    'oceania': '511',
    'global': '127'
    }

with open('data.ini', 'w') as f:
    config.write(f)



## Accessing the data
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
    








