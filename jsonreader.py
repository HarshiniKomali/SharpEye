import json
import csv
import requests

#reading in the json file
with open("atlas_dataset.json", "r") as jsonfile:
    dataset = json.load(jsonfile)

# datapoint = dataset["images"][0]

# print(datapoint["title"])
# print(datapoint["sentences"][0]['tokens'])
# print(datapoint["image_url"])

def checkpoint(checkpoint_location):
    with open("CleanURLOnly{}.csv".format(count), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(output_list)



output_list = [["Name", "URL", "tokens"]]
count = 0

for datapoint in dataset["images"]:
    buffer = [str(datapoint["title"]).replace("\n", " "), "Error"]
    tokens = datapoint["sentences"][0]['tokens']
    buffer.extend(tokens)



    if "voonik" not in datapoint["image_url"]:
        url = datapoint["image_url"]

        try:
            response = requests.get(url)

            if (response.status_code == 200):
                buffer[1] = url
                output_list.append(buffer)
                count +=1

                if count % 5000 == 0:
                    checkpoint(count)
        except:
            pass

checkpoint("final")
