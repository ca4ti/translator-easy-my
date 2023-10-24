#pip install requests~=2.27 python-lokalise-api~=1.6 python-dotenv~=0.20 googletrans==3.1.0a0 translators~=5.4 deep-translator~=1.9
import json
from googletrans import Translator
translator = Translator()

with open('data.json') as user_file:
  file_contents = user_file.read()

json_object = json.loads(file_contents)
all = list(json_object.keys())
for i in all:
    print(type(i),i,json_object[i])
    if type(json_object[i]) == str:
            print(i,json_object[i])
            r = translator.translate(json_object[i], dest='it').text
            json_object[i] = r 
            print(i,json_object[i])
    elif type(json_object[i]) == dict:
            for j in list(json_object[i].keys()):
                print(i,j,json_object[i][j])
                r = translator.translate(json_object[i][j], dest='it').text
                json_object[i][j] = r
                print(j,json_object[i][j])
    elif type(json_object[i]) == list:
            print("kkkkkkkkk <<<<<<<<")
            for id,k in enumerate(json_object[i]):
                print(i,idjson_object[i][id])
                r = translator.translate(json_object[i][id], dest='it').text
                json_object[i][id] = r
                print(i,idjson_object[i][id])
    else:
        print(type(i),i)
        print(json_object[i])
        print("file ===fix====")    
        break

print("file <<<<<<<<")  


# Writing JSON data to a file using a file object
with open("data_out.json", "w") as outfile:
    # json_data refers to the above JSON
    json.dump(json_object, outfile, indent=2)
