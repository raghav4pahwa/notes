import os
for folder,subfolder,filename in os.walk('./'):
    #print(folder + " " + str(subfolder) + " " + str(filename) + "\n")
    for files in filename:
        if (files.endswith('.vtt')):
            #print (files + '\n')
            path = os.path.join(folder,files)
            #print(path + '\n')
            os.remove(path)
