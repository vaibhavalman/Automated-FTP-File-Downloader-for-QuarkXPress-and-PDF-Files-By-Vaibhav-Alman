# importing required libraries for this code 

from ftplib import FTP
import os 
import shutil

#FTP server details

ftp_server = '192.168.xx.xx'
ftp_username = 'xxx'
ftp_password = 'xxx'
remote_directory = '/mahape'

#Local directory destination

local_directory = r'J:\USER\MUM'

#separate directory and files in ftp server
def is_directory(ftp, name):
    #check if given name is a directory
    current = ftp.pwd()
    #So, this will check if given name is file or directory 
    #if its file it will raise error and jumps to except block
    #if its directory it will change to that name directory
    #again it will reset the path with current
    try:
        ftp.cwd(name)
        ftp.cwd(current)
        return True
    except:
        return False

#function to download quark pages and pdf files from mumbai server

def download_files():

    #creation of ftp connection
    ftp = FTP(ftp_server)
    ftp.login(ftp_username, ftp_password)
    #here you can use change with directory function to set directory 
    ftp.cwd(remote_directory)

    #It will provide List of all files in ftp server and print them on window
    files = ftp.nlst()
    print("Files available for download: ", files)

    for file in files:
        if is_directory(ftp, file):
            print(f"Skipping directory: {file}")
            continue

        # Check if the file has the desired extension
        if file.lower().endswith(('.pdf','.qxp')):
            #it will concat pathname and file name then assined to variable
            local_file = os.path.join(local_directory, file)

            #downloading files
            with open(local_file, 'wb') as f:
                ftp.retrbinary(f"RETR {file}", f.write)
                print(f"Downloaded {file} to {local_file}")
    
    ftp.quit()
    print("All files are downloaded")


if __name__ == "__main__":

    download_files()
