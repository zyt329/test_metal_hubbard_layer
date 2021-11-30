# 0.input the line number and the values to change to.
# 1.Modify an existing script. (for each value should have different output names)
# 2.Run on the cluster with the modified script.

import os
import numpy as np
import math

# read from the file with no blank lines
# ================= #


def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line


def modify(input_name, output_name, line_text, line2change, val):
    """
    modify a specific line of code of the input file. "vals" in the line_text is replaced by the input val.
    """
    # read input file
    # ===================== #
    with open(input_name, 'r') as fp:
        lines = fp.readlines()

    # change the input file to what you want and write it to the file
    # ===================== #
    if os.path.exists(output_name):
        with open(output_name, 'w') as fp_new:
            lines[line2change] = line_text.replace('vals', str(val), 1)
            fp_new.writelines(lines)
    elif not os.path.exists(output_name.replace(output_name.split('/', -1)[-1], '', 1)):
        os.system(
            'mkdir '+output_name.replace(output_name.split('/', -1)[-1], '', 1))
        print('made directory:' +
              output_name.replace(output_name.split('/', -1)[-1], '', 1))
        with open(output_name, 'x') as fp_new:
            lines[line2change] = line_text.replace('vals', str(val), 1)
            fp_new.writelines(lines)
    else:
        with open(output_name, 'x') as fp_new:
            lines[line2change] = line_text.replace('vals', str(val), 1)
            fp_new.writelines(lines)


vals = np.linspace(-2.0, 2.0, num=3)
for val in vals:
    # "cwd" gives the path of the folder the "modify_script.py" file is in.
    cwd = os.path.dirname(os.path.abspath(__file__)) + '/'
    output_name = cwd+'input_files/in_test_interface_mu='+str(val)
    modify(
        input_name=cwd+'in_test_interface',
        output_name=cwd+'in_test_interface_tempo',
        line_text='mu_up  =  vals \n',
        line2change=18,
        val=val
    )
    modify(
        input_name=cwd+'in_test_interface_tempo',
        output_name=cwd+'in_test_interface_tempo',
        line_text='mu_dn  =  vals \n',
        line2change=19,
        val=val
    )
    modify(
        input_name=cwd+'in_test_interface',
        output_name=output_name,
        line_text='ofile  = out_file_mu=vals \n',
        line2change=4,
        val=val
    )
    #========= modify batch script ============#
    modify(
        input_name=cwd+'test_interface.sh',
        output_name=cwd+'test_interface.sh',
        line_text='#SBATCH --job-name='+output_name.split('/', -1)[-1]+' \n',
        line2change=1,
        val=val
    )
    modify(
        input_name=cwd+'test_interface.sh',
        output_name=cwd+'test_interface.sh',
        line_text='time /nfs/home/zyt329/QUEST/ggeom '+output_name+'>outfile \n',
        line2change=4,
        val=val
    )
    #========= run the created scripts ===========#
    os.system('cd '+cwd.replace('modify_script.py', '', 1)+';'
              + 'rm in_test_interface_tempo'+';')
    # + 'sbatch test_interface.sh')
