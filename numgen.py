from random import randint
import os.path

num_tsts = int(input("Number of tests to generate: "))
num_digs = int(input("Number of digits per test:"))

for i in range(num_tsts):
    # Generate name
    fnum = str(i).zfill(3)
    fname = 'q_{}.txt'.format(fnum)

    # Make sure files are not overwritten
    if os.path.isfile(fname):
        print('Skipping: {}'.format(fnum))
        continue

    with open(fname, 'w+') as f:
        # Write digits
        for i in range(num_digs):
            f.write(str(randint(0, 9)) + '\n')
