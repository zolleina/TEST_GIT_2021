if __name__ == "__main__":
    #########################################
    #              Procedure 1              #
    #########################################
    # Add print statement here
    print("Hello world")
import json
with open('json_example2.json','r') as file1:
    data = json.load(file1)
#    print(type(data))
print(data)
address = data['address']
print(address[0])
print(address[1])
for city in address['city']:
    print(city)
#
user['location']['city'] = 'Capracotta'
user['location']['state'] = 'Molise'
print(data)
with open('json_example_edited.json','w') as file2:
    json.dump(data,file2,indent=4)
    