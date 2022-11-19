import json
import csv

#reading in the json file
with open("atlas_dataset.json", "r") as jsonfile:
    dataset = json.load(jsonfile)

# datapoint = dataset["images"][0]

# print(datapoint["title"])
# print(datapoint["sentences"][0]['tokens'])
# print(datapoint["image_url"])

output_list = [["Name", "URL", "tokens"]]


for datapoint in dataset["images"]:
    buffer = [str(datapoint["title"]).replace("\n", " "), "Error"]
    tokens = datapoint["sentences"][0]['tokens']
    buffer.extend(tokens)

    if "voonik" not in datapoint["image_url"]:
        buffer[1] = datapoint["image_url"]

        output_list.append(buffer)


with open("CleanURLOnly.csv", 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_list)
