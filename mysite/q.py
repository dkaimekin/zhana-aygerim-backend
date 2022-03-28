import os
temp_ip = 'http://192.168.68.164:8000'
pwd = '/home/adilkhan/Documents/coding/editor-right-version-1/back/mysite/media/main-catalog'
os.chdir(pwd)

file = open("/home/adilkhan/Documents/coding/editor-right-version-1/back/mysite/queries.sql", 'w')

# access main directory:

for f in os.listdir():
    # ignore .DS_Store folder: 

    if(f!='.DS_Store'):
        print(f)
        cur_dir = pwd+'/'+f
        os.chdir(cur_dir)
        # change current directory subdirectory: 

        print(cur_dir, "have the following files:")
        for x in os.listdir():
            file_name, file_ext = os.path.splitext(x)
            filename_array = file_name.split(' ')
            if(len(filename_array) >= 1):
                print("Found copy!")
                new_name = '{}{}'.format(filename_array[0], file_ext)
                print(new_name)
                name_query = new_name.split(".")[0]
                category_query = name_query.split('-')[0]
                url = temp_ip+"/"+cur_dir+"/"+name_query+file_ext
                query = "INSERT INTO editor_image (sku, url, name, category) VALUES ('{}', '{}', '{}', '{}');\n".format(name_query, url, name_query, category_query)
                print(query)
                file.write(query)
        
    else:
        print("Encountered DS_Store")
file.close()


"/Users/daniilkaimekin/Documents/coding_projects/zhana-aygerim/zhana-aygerim/back/mysite/queries.sql"