# generate input file, geometry file, job script file, and job.sh file
# for QUEST jobs
# example for sweeping beta on square lattice


import os
#import numpy as np

# Parameters*******************************
#machine = 'puma'

n_max = 10  # number of random seed used for each run

dtau = 0.10  # dtau
L_min = 6   # number of time slices min
L_max = 20  # number of time slices max
L_step = 2  # time slices step
# L = int(beta/dtau)

warms = 50000   # number of warm up sweeps
sweeps = 100000  # number of measurement sweeps

S = 8  # lattice size
U = 2  # Hubbard U

# Parameters*******************************

f3 = open('job.sh', 'w+')

here = os.path.dirname(os.path.realpath(__file__))

for L in range(L_min, L_max+1, L_step):

    beta = float(L)*dtau
    mu = 0.0

    filename4 = 'squaren%iU%.1f.geom' % (S, U)
    f4 = open(os.path.join(here, filename4), 'w')

    # geometry file - square lattice *******************************

    f4.write('#NDIM\n')
    f4.write('2\n')
    f4.write('#PRIM\n')
    f4.write('1.0  1.0  0.0\n')
    f4.write('-1.0 1.0  0.0\n')
    f4.write('0.0  0.0  1.0\n')
    f4.write('#SUPER\n')
    f4.write(str(S)+'  0\n')
    f4.write('0  '+str(S)+'\n')
    f4.write('#ORB\n')
    f4.write('s0  0.0  0.0  0.0\n')
    f4.write('#HAMILT             tup  tdn  lambda\n')
    f4.write('0 0  1.0  0.0  0.0  1.0  1.0  0.0\n')
    f4.write('0 0  0.0  1.0  0.0  1.0  1.0  0.0\n')
    f4.write('0 0  0.0  0.0  0.0  0.0  0.0  '+str(U)+'\n')
    f4.write('#SYMM\n')
    f4.write('d  0.0d0 0.0d0 0.0d0 1.0d0 0.0d0 0.d0\n')
    f4.write('d  0.0d0 0.0d0 0.0d0 0.0d0 1.0d0 0.d0\n')
    f4.write('c4 0.0d0 0.0d0 0.0d0 0.0d0 0.0d0 1.d0\n')
    f4.write('#PHASE\n')
    f4.write(' 1 1\n')
    f4.write('-1 1\n')
    f4.write('s0  0.0  0.0  0.0  1.0\n')
    f4.write('s1  0.0  1.0  0.0 -1.0\n')
    f4.write('#BONDS\n')
    f4.write('0 0  0.0  0.0  0.0 # 1\n')
    f4.write('0 0  1.0  0.0  0.0 # 2 -2\n')
    f4.write('0 0  1.0  1.0  0.0 # 3 -3\n')
    f4.write('0 0  0.0  1.0  0.0 # 4 -4\n')
    f4.write('0 0 -1.0  1.0  0.0 # 5 -5\n')
    f4.write('#PAIR\n')
    f4.write('           1     2    -2    3    -3     4     -4     5    -5\n')
    f4.write('s-wave    1.0   0.0   0.0  0.0   0.0   0.0    0.0   0.0   0.0\n')
    f4.write('s*-wave   0.0   1.0   1.0  0.0   0.0   1.0    1.0   0.0   0.0\n')
    f4.write('s**-wave  0.0   0.0   0.0  1.0   1.0   0.0    0.0   1.0   1.0\n')
    f4.write('d-wave    0.0   1.0   1.0  0.0   0.0  -1.0   -1.0   0.0   0.0\n')
    f4.write('d*-wave   0.0   0.0   0.0  1.0   1.0   0.0    0.0  -1.0  -1.0\n')
    f4.write('#END\n')
    f4.close()

    for n in range(1, n_max+1):

        filename1 = 'intestb%.1f-%i' % (beta, n)
        filename2 = 'testb%.1f-%i.sh' % (beta, n)

        f1 = open(os.path.join(here, filename1), 'w')
        f2 = open(os.path.join(here, filename2), 'w')

        # input file*******************************

        f1.write('# ==========================\n')
        f1.write('# lattice dimension\n')
        f1.write('# ==========================\n')
        f1.write('\n')
        f1.write('ofile  = testb%.1f-%i' % (beta, n)+'\n')
        f1.write('gfile  = squaren%iU%.1f.geom' % (S, U)+'\n')
        f1.write('\n')
        f1.write('# ==========================\n')
        f1.write('# Holstein model\n')
        f1.write('# ==========================\n')
        f1.write('\n')
        f1.write('SimType = 0\n')
        f1.write('omega   = 0.0\n')
        f1.write('\n')
        f1.write('# ==========================\n')
        f1.write('# Hubbard model\n')
        f1.write('# ==========================\n')
        f1.write('\n')
        f1.write('mu_up   = 0.0\n')
        f1.write('mu_dn   = 0.0\n')
        f1.write('L       = '+str(L)+'\n')
        f1.write('dtau    = '+str(dtau)+'\n')
        f1.write('HSF     = -1\n')
        f1.write('HSFtype = 0\n')
        f1.write('bcond   = 0.0, 0.0, 0.0\n')
        f1.write('delta1  = 4.0\n')
        f1.write('delta2  = 4.0\n')
        f1.write('\n')
        f1.write('# ==========================\n')
        f1.write('# Mets algorithm\n')
        f1.write('# ==========================\n')
        f1.write('\n')
        f1.write('nwarm   = '+str(warms)+'\n')
        f1.write('npass   = '+str(sweeps)+'\n')
        f1.write('ntry    = 1\n')
        f1.write('tausk   = 100\n')
        f1.write('tdm     = 0\n')
        f1.write('\n')
        f1.write('# ==========================\n')
        f1.write('# Measurements\n')
        f1.write('# ==========================\n')
        f1.write('\n')
        f1.write('nbin    = 10\n')
        f1.write('nhist   = 0\n')
        f1.write('seed    = '+str(n*12345)+'\n')
        f1.write('\n')
        f1.write('# ==========================\n')
        f1.write('# Numerical\n')
        f1.write('# ==========================\n')
        f1.write('\n')
        f1.write('north   = 8\n')
        f1.write('nwrap   = 8\n')
        f1.write('fixwrap = 1\n')
        f1.write('errrate = 0.001\n')
        f1.write('difflim = 0.01\n')

        f1.close()

        # job script file*******************************

        f2.write('#!/bin/bash\n')
        f2.write('#SBATCH --job-name=%.1f-%i\n' % (beta, n))
        f2.write('#SBATCH --output=testb%.1f-%i.log\n' % (beta, n))
        f2.write('#SBATCH --partition=puma-i9\n')
        f2.write('time ./ggeom intestb%.1f-%i' %
                 (beta, n)+'>outtestb%.1f-%i' % (beta, n)+'\n')

        f2.close()

        # job.sh file*******************************

        f3.write('sbatch testb%.1f-%i.sh' % (beta, n)+'\n')


f3.close()
