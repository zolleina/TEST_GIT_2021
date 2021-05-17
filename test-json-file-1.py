if __name__ == "__main__":
    #########################################
    #              Procedure 1              #
    #########################################
    # Add print statement here
    print("Hello world")
import json
with open('json_example.json','r') as file1:
    data = json.load(file1)
#    print(type(data))
print(data)
user = data['user']
print(user['name'])
for role in user['roles']:
    print(role)
#
user['location']['city'] = 'Capracotta'
user['location']['state'] = 'Molise'
print(data)
with open('json_example_edited.json','w') as file2:
    json.dump(data,file2,indent=4)
    