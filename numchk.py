import os.path

num_tsts = int(input("Number of answers to check: "))

for i in range(num_tsts):
    # Stats
    right, wrong = 0, 0

    fnum = str(i).zfill(3)
    fname1 = 'q_{}.txt'.format(fnum) # Generated numbers
    fname2 = 'a_{}.txt'.format(fnum) # Subject answers

    if not os.path.isfile(fname1):
        print('Missing file: {}'.format(fname1))
        continue
    elif not os.path.isfile(fname2):
        # End of inputs
        break

    with open(fname1, 'r') as f1:
        with open(fname2, 'r') as f2:
            tot = 0

            for line in f2:
                # Add digit to running total
                tot += int(f1.readline())

                # Compare total with subject answer
                if tot == int(line):
                    right += 1
                else:
                    # Replace total
                    wrong += 1
                    tot = int(line)

    # Print stats
    print(fnum, right, wrong, right+wrong)
