import os
path = 'C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\feature_vectors\\'
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.txt'))
    i = i+1
