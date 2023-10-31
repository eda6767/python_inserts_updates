# Python inserts & updates

<sub/>
In this project I will show solution how prepare in automatically way inserts or updates to database based on data in excel. It is helpful if you have to frequently make updates on databse like on table with parameters or on dictionary, otherwise you have to create testing data and feed with data table on database. </sub>

<br/>
</br>

<p align="center">
<img width="901" alt="Zrzut ekranu 2023-10-31 o 16 17 18" src="https://github.com/eda6767/python_inserts_updates/assets/102791467/c32c52a6-6951-46d6-98db-d53ce526a3e6">
</p>


<sub/> Let's say that we have couples of files with dictionaries in various versions in location _dir_list_ . We can find all files for given _dict_name_ in this repository as a list as also find all version for given dictionaries assuming that file's name meets the standards.</sub>


<sub/>

```python
dictionaries_files =[x for x in dir_list if dict_name in x and 'xlsx' in x]
versions =[x[-9:len(x ) -5] for x in dictionaries_files if dict_name in x]
```

</sub>

<sub>
As far we got list of files names for given dictionary and list of available versions. For us the most important is the newest version, beacuse for that we want to create updates. So, let's choose file with the highest version. </sub> 

<br/>
</br>

<sub/>

```python
current_version =max(versions)
print("Current version of dicionary to actualization: {}".format(current_version))

file_name =[x for x in dir_list if dict_name in x if current_version in x]
print("Version of dictionary for actualization: ")
print(file_name[0])

```
</sub>




<sub/>
Now, having accurate file, we can load data into dataframe using a converter. Sometimes you can have values for columns which you want to update like '02' as a string, not as number. For this purpose we will use, a converter as below: </sub>

<br/>
</br>

<sub/>

```python
column_list = []
df_column = pd.read_excel(file_name[0], skiprows=0).columns
for i in df_column:
    column_list.append(i)
converter = {col: str for col in column_list}

input_data = pd.read_excel(file_name[0], skiprows=0, converters=converter)
```
<br/>
</br>

</sub>


<sub/> Next step, when we have loaded data is choosing accurate rows to updates based on version column. </sub>


<sub/> 

```python
f=float(current_version)
file=input_data[input_data['VERSION']==f]
file=file.reset_index()
file=file.fillna('NA')
n=len(file.index)
print('\n\n' + "Numbers of updates in {}: {} ".format(dict_name, n))
```

</sub>


<sub/> To make updates for given dataframe, we need to know the order of columns. For this let's create a dictionary with a key - column's name, and value - position of given columns. Therefore we will create a dictionary with columns, where there is a 'CAT' in column's name - these will be columns for updates. </sub>


<sub/>

```python
column_list=input_data.columns

dict_all_columns={}
index=0
for i in column_list:
    index+=1
    dict_all_columns[i]=index

for key, value in dict_all_columns.items():
    print("Column name: {} | position : {}".format(key, value))

update_column_dict={}
for key, value in dict_all_columns.items():
    if 'CAT' in key:
        update_column_dict[key]=value

for key, value in update_column_dict.items():
    print("Column name: {} | position : {}".format(key, value))

```

</sub>


<sub/> Each code for updates has to be kept in separate folder, and file for update has to start and end with format as below, where XXX is a number of version for specific package. </sub>


<img width="1162" alt="Zrzut ekranu 2023-10-31 o 20 44 49" src="https://github.com/eda6767/python_inserts_updates/assets/102791467/511ac299-9aa6-45d9-a3be-8608b7f9db9c">


<sub/>

```python

os.chdir(path_dict_target)
directory="DCT-KOMB-01.01." + str(version) + "-FIX"
parent_dir = path_dict_target
path = os.path.join(parent_dir, directory)
try:
    os.mkdir(path)
    print("Folder has been created {}".format(directory))
except FileExistsError as error:
    print(error)

```

</sub>
