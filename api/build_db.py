import os
from fnmatch import fnmatch

content_folder = "/home/pi/git/funmasokonet.github.io/content/posts"
pattern = "*.md"

def get_file_names(content_folder, pattern):
	joke_files = []
	for path, subdirs, files in os.walk(content_folder):
		for name in files:
			if fnmatch(name, pattern):
				joke_files.append(os.path.join(path, name))
	return joke_files

joke_files = get_file_names(content_folder, pattern)

for joke_file in joke_files:
	with open(joke_file) as f:
		lines = f.readlines()
		print("".join(lines).replace("&minus;","-"))
