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
        
def create_base_for_results():
    '''This moves the merged file to log folder created for it'''
    # path to root log directory 
    root_logDir = os.path.join(os.curdir, "results_folder")

    def move_file_sub_log_dir():
        '''This moves the baseFile to sub log directory'''
        # generate run id based on current time
        import time
        run_id = time.strftime("mergedFile_%Y_%m_%d-%H_%M_%S")
        
        # path to move baseFile
        move_to_path = os.path.join(root_logDir, run_id)
        if not os.path.isdir(move_to_path):
            os.makedirs(move_to_path)
        base_file = 'baseFile.ipynb'
        
        # finally move baseFile
        import shutil
        shutil.move(base_file, move_to_path)
        print(f"\n## Access merged file at \
the following location ##\n{move_to_path}")
    
    move_file_sub_log_dir()

class CleanExit(Exception):
    '''Protects program from stopping abruptly'''
    def __init__(self):
        print("\n## No jupyter notebooks found to merge ##")
        print("\nexiting program....")


def safelyExit():
    '''safely exit when target notebooks are not present'''
    import sys
    try:
        sys.exit()
    except:
        raise CleanExit

def is_target_notebooks_exists(listOfFiles):
    for file in listOfFiles:
        if ".ipynb" in file:
            return True
    return False

def main():
	# get the list of all the files
    listOfFiles = os.listdir()

    # remove unwanted files from list of files
    if '.ipynb_checkpoints' in listOfFiles:
        listOfFiles.remove('.ipynb_checkpoints')
    if "mergeJupyterFiles.ipynb" in listOfFiles:
        listOfFiles.remove('mergeJupyterFiles.ipynb')
            
    # check the existence of taget notebook files
    if not is_target_notebooks_exists(listOfFiles):
    	safelyExit()
    	
	# iterate over the list of files to merge them
    listOfFiles.sort()
    for file in listOfFiles:
        if ".ipynb" in file:
            mergeAllJupyterFile(file)
    create_base_for_results()
        
if __name__=="__main__":
    try:
        main()
        print("\n## Attempt Successfull!! ##")
    except Exception as e:
        print(e)
    finally:
        print("## For any feedbacks mail-to: <sunny.c17hawke@gmail.com> ##\n")
