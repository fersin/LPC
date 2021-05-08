from ftplib import FTP, FTP_PORT
from typing import List

 

def save_file(con: FTP, remote_file_path:str, local_file_path:str):
    with open(local_file_path,'wb') as local_file:
        con.retrbinary(f'RETR {remote_file_path}', local_file.write)

 

def get_txt_file(con: FTP, file_path:str):
    listado = []
    con.retrlines(f'RETR {file_path}', listado.append)
    return listado

 

def list_folder(con: FTP, directory:str):
    print(directory)
    listado = []
    con.retrlines(f'LIST {directory}', listado.append)
    return listado

 


def get_file_dir(con: FTP, directory:str):
    listado = list_folder(con,directory)
    return [file_info for file_info in listado if file_info.startswith('-')],  \
        [file_info for file_info in listado if not file_info.startswith('-')]
        



 

def get_file_name(file_info:str) -> str:
    return ''.join(file_info.split()[8:])

 

def connect_ftp(host:str, port:int = FTP_PORT, usr:str = '', pwd:str = '', save_path:str = ''):
    connection = FTP()
    connection.connect(host=host, port=port, timeout=3)
    connection.login(usr,pwd)
    actual_path = ''
    l_file, l_dir = get_file_dir(connection, actual_path)
    files_info = '\n'.join(l_file)
    dirs_info = '\n'.join(l_dir)
    print(f'files:\n{files_info}\ndirs:\n{dirs_info}')
    print(get_txt_file(connection, 'welcome.msg'))
    #save_file(connection, arc, f'{save_path}/archivos')
    a=list_folder(connection, 'debian')
    arc=[]
    for i in range(len(a)):
      if "txt" in a[i] or "README" in a[i] or ".msg" in a[i]:
        arc.append(a[i])
        print(arc[i])
    for file_info in arc:
        file_name = get_file_name(file_info)
        print("aqui wey",file_name)
        save_file(connection, f'{actual_path}/{file_name}', f'{save_path}/{file_name}')
  



    connection.close()

if __name__ == '__main__':
    #connect_ftp('192.168.11.3', 8022)
    connect_ftp(host='ftp.mirror.nl', save_path='/home/runner/ftp/tar') 
