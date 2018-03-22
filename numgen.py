from random import randint
import os.path

num_tsts = 10
num_digs = 100

for i in range(num_tsts):
    # Generate name
    fnum = str(i).zfill(3)
    fn = 'q_{}.txt'.format(fnum)

    # Make sure files are not overwritten
    if os.path.isfile(fn):
        print('Skipping {}'.format(fnum))
        continue

    with open(fn, 'w+') as f:
        # Write digits
        for i in range(num_digs):
            f.write(str(randint(0, 9)) + '\n')
