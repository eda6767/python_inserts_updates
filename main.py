
def create_dict_pkg(dict_name, user):

    import os
    import pandas as pd
    version = input("Number of package: ")

    path_dict_excel ="/Users/{}/Documents".format(user)
    path_dict_target ="/Users/{}/Documents/dictionaries".format(user)

    os.chdir(path_dict_excel)
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    pd.options.display.float_format ='{:.0f}'.format


    dir_list = os.listdir(path_dict_excel)

    dictionaries_files =[x for x in dir_list if dict_name in x and 'xlsx' in x]
    versions =[x[-9:len(x ) -5] for x in dictionaries_files if dict_name in x]


    current_version =max(versions)
    print("Current version of dicionary to actualization: {}".format(current_version))

    file_name =[x for x in dir_list if dict_name in x if current_version in x]
    print("Version of dictionary for actualization: ")
    print(file_name[0])


    column_list = []
    df_column = pd.read_excel(file_name[0], skiprows=0 ).columns
    for i in df_column:
        column_list.append(i)
    converter = {col: str for col in column_list}

    KMB = pd.read_excel(file_name[0], skiprows=0, converters=converter)

    print(current_version)
    f=float(current_version)
    f=format(f, '.2f')
    print("Version {}".format(f))

    global file
    file=KMB[KMB['VERSION']==f]

    file=file.reset_index()
    file=file.fillna('NA')
    print(file)

    n=len(file.index)

    print('\n\n' + "Numbers of updates in T11001_PRD_HRCHY_DIM: {} ".format(n))

    print('\n\n' + "Creating file with updates for {}".format(dict_name))

    column_list=KMB.columns

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

    sql_text=[]
    target='KPR_11_PRD.T11001_PRD_HRCHY_DIM'
    df=file

    line_start="---[CHANGE START]DCT-KOMB-01.01."+version+"- FIX"
    line_end="---[CHANGE END]DCT-KOMB-01.01."+version+"- FIX"


    os.chdir(path_dict_target)

    directory="DCT-KOMB-01.01." + str(version) + "-FIX"
    parent_dir = path_dict_target
    path = os.path.join(parent_dir, directory)
    try:
        os.mkdir(path)
        print("Folder has been created {}".format(directory))
    except FileExistsError as error:
        print(error)

    print(path)
    os.chdir(path)



    for index, row in df.iterrows():
        x='UPDATE ' + target + ' SET '

        for key, value in update_column_dict.items():
            x = x + str(key + "='" + str(df.iloc[index, update_column_dict[key]]) + "', ")
        x = x[:-2]
        x = x + " WHERE PRD_KEY= '" + str(df.iloc[index, dict_all_columns['PRD_KEY']]) + "' AND END_DT = '" + str(
            df.iloc[index, dict_all_columns['END_DT']]) + "';"
        sql_text.append(x)
        new = '\n'.join(sql_text)
        new = '----' *50 + '\n' + line_start + '\n\n' + new + '\n\n' + 'COMMIT;' + '\n\n'  + line_end + '\n' + '----' *50
        with open('{}.sql'.format(dict_name) , 'wt')as output:
            output.write(new)

    print("\n\n File has been created \n\n")

    c=0
    try:
        with open('{}.sql'.format(dict_name), 'r') as file:

            for line in file:
                c+=1
        print("Numbers of updates in file: {}".format(c-8))
    except FileNotFoundError as error:
        print(error)





if __name__ == "__main__":
    dict_name = input("Give a dictionary name: ")
    user = input("User name: ")
    create_dict_pkg(dict_name, user, version)
