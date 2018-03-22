import os.path

num_tsts = 10

for i in range(num_tsts):
    # Stats
    right, wrong = 0, 0

    fnum = str(i).zfill(3)
    f1n = 'q_{}.txt'.format(fnum) # Generated numbers
    f2n = 'a_{}.txt'.format(fnum) # Subject answers

    if not os.path.isfile(f1n):
        print('Missing file {}'.format(f1n))
        continue
    elif not os.path.isfile(f2n):
        # End of inputs
        break

    with open(f1n, 'r') as f1:
        with open(f2n, 'r') as f2:
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
