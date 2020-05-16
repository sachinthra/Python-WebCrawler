import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('creating project'+directory)
        os.makedirs(directory)
#create_project_dir('newFile')

# create queue and crawled files
def create_data_files(project_name, base_url):
    #create_project_dir(project_name)
    queue = os.path.join(project_name , 'queue.txt')
    crawled = os.path.join(project_name, 'crawled.txt')
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

#create a new file

def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)
    # f.close()

# add data to exesting file

def append_to_file(path,data):
    with open(path,'a') as file:
        file.write(data + '\n')
    
#delete the content of a file
def delete_file_content(path):
    open(path, 'w').close()
        


# read a fle and convert a each lines toset items
def file_to_set(filename):
    results = set()
    with open (filename,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

#itrate through a set eeach item will be a new line in the file
def set_to_file(links, file_name):
    with open(file_name,"w") as f:
        for l in sorted(links):
            f.write(l + "\n")


#create_data_files('newFile', 'https://www.digitalocean.com/community/tutorials/how-to-make-a-simple-calculator-program-in-python-3')