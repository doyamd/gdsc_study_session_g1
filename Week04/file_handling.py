import os
import time

def identify(file):
    curr_time = time.time()
    new_time = os.path.getmtime(file)
    creation_time = os.path.getctime(file)
    if curr_time - new_time <= 24 * 3600 or curr_time - creation_time <= 24 * 3600:
        return True
    else:
        return False
def update(file):
    with open(file, 'a') as f:
        timestamp = time.strftime("[%Y-%m-%d %H:%M:%S] ")
        f.write('#')
        f.write(timestamp)

current_directory = os.getcwd()
all_files = []
for root, dirs, files in os.walk(current_directory):
    if '.git' in dirs:
        dirs.remove('.git')

    for file in files:
        file_path = os.path.join(root, file)
        all_files.append(file_path)

for file in all_files:
    if identify(file):
        update(file)
        print(file)

folder_name = "last_24hours"
folder_path = os.path.join(os.getcwd(), folder_name)

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
else:
    print('Exists')


#[2023-12-13 12:10:07] #[2023-12-13 12:13:19] 