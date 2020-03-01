# Merge-multiple-jupyter-notebooks
This code is intended to merge multiple jupyter notebooks into one notebook. final notebook will also contain the parent file names

## Kindly follow below instructions -
**1.** Download mergeJupyterFiles.py or mergeJupyterFiles.ipynb

**2.** Now place this downloaded.py file or ipynb file into a folder containing other jupyer notebooks

**3.** Now if you have copied .py file then use following command in terminal

```
		python  mergeJupyterFiles.py
```
<p align="center">
<img src="https://raw.githubusercontent.com/c17hawke/Merge-multiple-jupyter-notebooks/master/screeenshots/command.png" alt="command">
</p>
	
	[NOTE: make sure you are in the same location as this py file exists]
	
	And in case you are using ipynb then you can directly run it in your jupyter notebook


**4.** After completing step 4 you'll see a message of success and a baseFile.ipynb file will be created which is the merged file of all the files present inside a result folder 

<p align="center">
<img src="https://raw.githubusercontent.com/c17hawke/Merge-multiple-jupyter-notebooks/master/screeenshots/mergedNotebook.png" alt="mergedNotebook">
</p>
<hr>

## Common advise for the best results -
**1.** In case of non existence of notebook you'll get the following error. Hence one should make sure that your target notebooks are present at the same loaction. 

<p align="center">
<img src="https://raw.githubusercontent.com/c17hawke/Merge-multiple-jupyter-notebooks/master/screeenshots/error.png" alt="error">
</p>

**2.** Make sure your notebooks contain ordered prefixes like file 01, file 02 etc in their names such that they can be arranged. This will help you to merge them serially. Some examples of file name are like -
	* "Session 1.01 topicName", "Session 1.02 another topic Name"
