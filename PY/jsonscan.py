#!/Users/user/.pyenv/shims/python

import json
import sys


def scandict(dct):
	print(dct.keys())
	for j in dct:
		# if the element is not a list or dict, print element and move on
		if ((type(dct[j]) != list) and (type(dct[j]) != dict)):
			print(dct[j])
			continue
		
		# if the element is a list, go to that function to unpack
		if (type(dct[j]) == list):
			scanlist(dct[j])
		else:
		# if the element is another dict, recurse
			scandict(dct[j])


def scanlist(lst):
	for i in range(len(lst)):
		# if the element is not a list or dict, print element and move on
		if ((type(lst[i]) != list) and (type(lst[i]) != dict)):
			print(list[i])
			continue

		# if the element is another list, recurse
		if (type(lst[i]) == list):
			scanlist(lst[i])
		else:
		# if the element is a dict, go to that function to unpack
			scandict(lst[i])


def main():
	if (len(sys.argv) != 2):
		print("Usage: jsonscan.py <filename.json>")
		exit()

	with open(sys.argv[1], "r") as f:
		loaded_data = json.load(f)
		scanlist(loaded_data)


if __name__ == "__main__":
	main()
