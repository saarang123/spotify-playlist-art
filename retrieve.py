import argparse
import json
import requests

def pull(num, album_link):
	response = requests.get(album_link)
	file = open("albumart/album" + str(num) + ".jpeg", "wb")
	file.write(response.content)
	file.close()

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--data", help="path to the data file")
parser.add_argument("-n", "--start-num", type=int, default=0, help="minimum file ID")
args = vars(parser.parse_args())

if args.get("data", None) is None:
	exit()
else:
	file_name = args["data"]
	start = args["start_num"]

file = open(file_name,)
data = json.load(file)

n = start
for details in data["items"]:
	album_link = str(details["track"]["album"]["images"][0]["url"])
	pull(n, album_link)
	print(album_link)
	n += 1

print(n)
