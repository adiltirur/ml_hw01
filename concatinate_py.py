for i in range(5660):

    filenames = [i]
    with open('C:\\Users\\adilt\\Desktop\\ML_HW\\drebin\\malware\\', 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
