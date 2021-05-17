if __name__ == "__main__":
    #########################################
    #              Procedure 2              #
    #########################################
    # Add print statement here
    print("Hello world")
# Import modules
import sys
# from helper import *
from ruamel import yaml
import yaml
print('###### YAML ######')
# Open the user.yaml file as read only
with open('yaml_example.yml','r') as file1:
    data = yaml.safe_load(file1)
#    print type 
print("Type of user_yaml variable:")
print(type(data))
#
print('Keys in sample_yaml:')
for key in data:
    print(key)
#    
print('End of Keys in sample_yaml')
user = data['user']
print(user['name'])
for role in user['roles']:
    print(role)
#
user['location']['city'] = 'Capracotta'
user['location']['state'] = 'Molise'
print(data)
with open('yaml_example_edited.yml','w') as file2:
    yaml.dump(data,file2,default_flow_style=False)
    