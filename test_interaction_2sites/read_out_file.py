# read QUEST output

import numpy as np
import os
import math

# non blank lines
# ================= #


def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line


#========= load files ============#
cwd = os.path.dirname(os.path.abspath(__file__)) + "\\"
vals = np.linspace(-1.0, 1.0, num=11)
#============= output file, write titles ==============#
out_name = '11pts.result'
#os.system('touch '+cwd+out_name)
with open(cwd+out_name, 'x') as fp:
    fp.write('T mu_up mu_dn n_up n_up_err n_dn n_dn_err \n')

for val in vals:
    #============= input file(s) ==============#
    file_name = 'out_files\out_file_mu_{}.out'.format(val)
    #============= read input file ==============#
    with open(cwd+file_name, 'r') as fp:
        for i, line in enumerate(nonblank_lines(fp)):
            data = line.split()
            if data[0] == 'beta':
                beta = float(data[2])
                T = 1.0/beta

            if data[0] == 'mu_up':
                mu_up = float(data[2])
                mu_up_err = float(data[3])

            if data[0] == 'mu_dn':
                mu_dn = float(data[2])
                mu_dn_err = float(data[3])

            if len(data) >= 3:
                if (data[0], data[1], data[2]) == ('spin', 'up', 'density'):
                    n_up = float(data[4])
                    n_up_err = float(data[6])

                if (data[0], data[1], data[2]) == ('spin', 'down', 'density'):
                    n_dn = float(data[4])
                    n_dn_err = float(data[6])

    with open(cwd+out_name, 'a') as fp:
        line = f"{T} {mu_up} {mu_dn} {n_up} {n_up_err} {n_dn} {n_dn_err} \n"
        fp.write('')
        fp.write(line)
