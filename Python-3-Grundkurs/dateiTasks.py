'''Datei öffnen und was reinschreiben'''
datei=open('C:/temp/Workspace/datei.txt','w')
datei.write('Nemo')
datei.close()

'''Daetei auslesen'''
datei=open('C:/temp/Workspace/datei.txt')
zeile=datei.readline()
print(zeile)
datei.close()
