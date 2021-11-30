#!/bin/bash
#SBATCH --job-name=in_test_interface_mu=2.0 
#SBATCH --output=testsquare.log
#SBATCH --partition=puma-i9
time /nfs/home/zyt329/QUEST/ggeom e:\UC Davis\Research\Metal_Attractive_Hubbard_Layer\jobscripts/input_files/in_test_interface_mu=2.0>outfile 
