import os.path
import time
import shutil

datei='C:/temp/Workspace/datei.txt'
kopie='C:/temp/Workspace/datei2.txt'

if os.path.exists(datei):
    print(datei,'original ist vorhanden')
else:
    print('original existiert nicht!')
    
if os.path.exists(kopie):
    print(kopie,'ist vorhanden')
    if os.path.isfile(kopie):
        print('Es handelt sich um eine Datei')
        print('Grösse in Bytes:', os.path.getsize(kopie))
        print('Änderungsdatum', time.ctime(os.path.getmtime(kopie)))
else:
    print('kopie existiert nicht!')

'''prüft ob ein pfad existiert'''
p='C:/temp/Workspace/datei.txt'
if os.path.exists(p):
    print(p,'ist vorhanden')
    if os.path.isfile(p):
        print('Es handelt sich um eine Datei')
        print('Grösse in Bytes:', os.path.getsize(p))
        print('Änderungsdatum', time.ctime(os.path.getmtime(p)))

'''datei kopieren'''
#shutil.move(datei,kopie)
shutil.move(datei,kopie)

if os.path.exists(kopie):
    print(kopie,'ist vorhanden')
    if os.path.isfile(kopie):
        print('Es handelt sich um eine Datei')
        print('Grösse in Bytes:', os.path.getsize(kopie))
        print('Änderungsdatum', time.ctime(os.path.getmtime(kopie)))
else:
    print('kopie existiert nicht!')

if os.path.exists(datei):
    print(datei,'original ist vorhanden')
else:
    print('original existiert nicht!')
    
