import requests

def downloadFile(fileName):
	# extract the filename
	filename = fileName.split("/")[-1] 
	# download image using GET
	image = requests.get(fileName, stream=True)
	# save the image received into the file
	with open(filename, 'wb') as fileDescryptor:
		i=0
		for chunk in image.iter_content(chunk_size=1024):
			i=i+1
			fileDescryptor.write(chunk)
	return
	
downloadFile("https://media.readthedocs.org/pdf/python-guide/latest/python-guide.pdf")
downloadFile("https://www.python.org/static/img/python-logo.png")
downloadFile("https://docs.python.org/3.11/archives/python-3.11.2-docs-pdf-letter.zip")


