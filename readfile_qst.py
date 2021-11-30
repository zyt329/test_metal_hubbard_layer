
# read QUEST output
# v2 == energy = E_kin + E_pot

import numpy as np
import math

U = 6
beta_list = [0.1,0.11,0.12,0.14,0.16,0.18,0.2,0.225,0.25,0.275,0.3,0.325,0.35,0.375,0.4,0.425,0.45,0.475,0.5]

# non blank lines
# ================= #

def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

# ================= #

fe = open('E_U%i.out'%U,'w+')
fe_v2 = open('E_U%i_v2.out'%U,'w+')
fd = open('D_U%i.out'%U,'w+')
fd_v2 = open('D_U%i_v2.out'%U,'w+')

for beta in beta_list:

    # initialize variables
    corr_den = [[],[],[]]
    corr_den_err = [[],[],[]]
    density_section = 999999

    filename = 'testb'+str(beta)+'.out' # QUEST output file name
    print('beta=',beta,'\n')
    
    with open(filename,'r') as fp:
        for i,line in enumerate(nonblank_lines(fp)):
        
            data  = line.split()
            if data[0] == 'beta':
                beta = float(data[2])
                T = 1.0/beta
    
            if data[0] == 'double':
                DO = float(data[3])
                DO_err = float(data[5]) 

            if data[0] == 'kinetic':
                E_kin = float(data[4])
                E_kin_err = float(data[6]) 

            if data[0] == 'potential':
                E_pot = float(data[4])
                E_pot_err = float(data[6]) 

            if data[0] == 'PH-symm':
                energy = float(data[7])
                energy_err = float(data[9]) 
            
            # double occupancy per coordination number
            if data[0]=='Density-density' and data[3]=='(up-dn)':
                density_section=i
            if i>density_section and i<density_section+(166*165/2)+167 and int(data[0])==int(data[1]):
                z=site_list[int(data[0])][1]
                # if beta==0.1:
                #     print(int(data[0]),z)
                corr_den[z-3].append(float(data[6]))
                # corr_den_err[z-3].append(float(data[8]))

        # print(len(correlation_den[0]),len(correlation_den[1]),len(correlation_den[2]))
        DO3 = sum(corr_den[0])/float(len(corr_den[0]))
        Corr_den = np.array(corr_den[0])
        DO3_err = math.sqrt(np.sum(Corr_den**2)/float(len(corr_den[0]))-DO3**2)/math.sqrt(float(len(corr_den[0]))-1)
        DO4 = sum(corr_den[1])/float(len(corr_den[1]))
        Corr_den = np.array(corr_den[1])
        DO4_err = math.sqrt(np.sum(Corr_den**2)/float(len(corr_den[1]))-DO4**2)/math.sqrt(float(len(corr_den[1]))-1)
        DO5 = sum(corr_den[2])/float(len(corr_den[2]))
        Corr_den = np.array(corr_den[2])
        DO5_err = math.sqrt(np.sum(Corr_den**2)/float(len(corr_den[2]))-DO5**2)/math.sqrt(float(len(corr_den[2]))-1)

        # print(beta)
        # print(E_kin+E_pot)
        fe.write(str(T)+' '+str(beta)+' '+str(energy)+' '+str(energy_err)+'\n')
        fe_v2.write(str(T)+' '+str(beta)+' '+str(E_kin+E_pot)+' '+str(E_kin_err+E_pot_err)+'\n')
        fd.write(str(T)+' '+str(beta)+' '+str(DO)+' '+str(DO_err)+'\n')
        fd_v2.write(str(T)+' '+str(beta)+' '+str(DO3)+' '+str(DO3_err)+' '+str(DO4)+' '+str(DO4_err)+' '+str(DO5)+' '+str(DO5_err)+'\n')

fe.close()
fe_v2.close()
fd.close()
fd_v2.close()