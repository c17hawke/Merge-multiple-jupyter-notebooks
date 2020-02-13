'''
# Author: Sunny Bhaveen Chandra
# Contact: sunny.c17hawke@gmail.com
'''

# import required files
import json
import os

def create_baseFile():
	'''This creates a base file in which we merge all the files'''
	baseData = '''{
	"cells": [{"cell_type": "markdown", "metadata": {},
	"source": ["# *Merged Jupyter Notebook*"]}],
	
	"metadata": {
	"kernelspec": {
	"display_name": "Python 3",
	"language": "python",
	"name": "python3"},
	"language_info": {
	"codemirror_mode": {"name": "ipython","version": 3},
	"file_extension": ".py",
	"mimetype": "text/x-python",
	"name": "python",
	"nbconvert_exporter": "python",
	"pygments_lexer": "ipython3",
	"version": "3.7.4"}
	},
	
	"nbformat": 4,
	"nbformat_minor": 2}'''

	Filename = 'baseFile.ipynb'
	with open(Filename,'w+') as f:
	    f.write(baseData)

def read_file_as_json(Filename):
    with open(Filename,'r') as f:
        whole_file = f.read()
    data = json.loads(whole_file)
    return data
    
def mergeAllJupyterFile(file=None):
    if not os.path.exists('baseFile.ipynb'):
        create_baseFile()

    # read files
    base_file = read_file_as_json('baseFile.ipynb')
    next_files = read_file_as_json(file)

    '''Create a header with each file to make a clear boundry among files'''
    FileBoundry =   {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Merged Jupyter Notebook"
   ]
   }
    
    FileBoundry['source'] = f'<hr><font color="green"><h1>from file: {file[:-6]}</h1></font>'

    # merge cells of second file into base_file one with Name of file as a header
    base_file['cells'] = base_file['cells'] + [FileBoundry] + next_files['cells']

    # dump data in baseFile
    Filename = 'baseFile.ipynb'
    with open(Filename,'w+') as f:
            f.write(json.dumps(base_file))


def main():
	# get the list of all the files
	listOfFiles = os.listdir()
	try:
		'''works incase you are using in Jupyter notebook
		then you need to remove the following files'''
		listOfFiles.remove('.ipynb_checkpoints')
		listOfFiles.remove('mainExperiment.ipynb')
		listOfFiles.remove('mergeJupyterFiles.py')
	except:
		'''when you are running as a python script'''
		listOfFiles.remove('mergeJupyterFiles.py')

	# sort the list 
	listOfFiles.sort()

	# iterate over the list of files to merge them
	for file in listOfFiles:
		if ".ipynb" in file:
			mergeAllJupyterFile(file)

        
if __name__=="__main__":
	try:
		main()
	except Exception as e:
		print(e)
		contact_statement = "\n** Please contact the author at sunny.c17hawke@gmail.com **\n"
		print("#"*len(contact_statement))
		print(contact_statement)
		print("#"*len(contact_statement))
	else:
		print("\n** your file is ready by name baseFile.ipynb **")	
