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

