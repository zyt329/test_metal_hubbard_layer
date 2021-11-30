import os
from matplotlib import pyplot as plt
from matplotlib import cycler
from matplotlib import cm
import pandas as pd
from astropy.io import ascii
import numpy as np

cwd = os.path.dirname(os.path.abspath(__file__)) + "\\"
file_name = "11pts.result"
df = ascii.read(cwd + file_name)


def size_compare_ploting(df_sub, colnames, quantity, quantity_symbol, J1):
    colors = [icolor['color'] for icolor in plt.rcParams['axes.prop_cycle']]
    custom_cycler = cycler(linestyle=['-', '--'])*cycler(color=colors)
    plt.rcParams['axes.prop_cycle'] = custom_cycler
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
              '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
    #colors = ['lime','blue','red']
    params = {'legend.fontsize': 13,
              'axes.labelsize': 15,
              'axes.titlesize': 20,
              'xtick.labelsize': 12,
              'ytick.labelsize': 12,
              'ytick.major.size': 5.5,
              'axes.linewidth': 2}

    plt.rcParams.update(params)

    Qs = ['16', '20', '24', '28', '32', '36']
    Ls = ['8', '12', '16']
    for J1_index, colname in enumerate(colnames):
        fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(10, 6.18))
        ax = axs

        #ax.axvline(x=0.6213, color='gray', linestyle='--')
        for L_index, df in enumerate(df_sub):
            label = "J1="+colname[0].replace('Temp_', '')+', Q='+Qs[L_index]
            # label='L='+Ls[L_index]
            ax.plot(df[colnames[J1_index][0]], df[colnames[J1_index][1]], '-*', markersize=2,
                    linewidth=1,
                    color=colors[L_index],
                    label=label, alpha=1)

            #ax.legend(ncol=1, handleheight=1.5, labelspacing=0.05, loc='upper left', frameon=True)
        ax.legend(fontsize=18)
        #ax.set_xlim(0, 1)
        #ax.set_ylim(60, 80)
        ax.set_xlabel(r'Temperature', size=20)
        ax.set_ylabel(quantity, size=20)
        ax.minorticks_on()
        ax.tick_params(axis='both', which='major',
                       labelsize=15, length=8, width=2)
        ax.tick_params(axis='both', which='minor',
                       labelsize=12, length=4, width=1)
        ax.grid(True)

        fig.savefig('./paper_plots/Avg_Dist/'+'fine_peak__Avg_Dist_synsize_'
                    + quantity_symbol+"J1=" +
                    colname[0].replace('Temp_', '')+'.png',
                    format='png',
                    dpi=600)
        # break


J1_list = ['0.8']  # ,'0.0', '0.2', '0.6' '0.85', '1.15']
# plotting different
for J1 in J1_list:
    quantity = r"Average Distance/Synthetic Size"
    quantity_symbol = 'Avg_Dist'

    # read in the data
    path = "E:/UC Davis/Research/Synthetic Dimensions/Synthetic_dim_code/data_in_text1/Avg_Dist/"
    filenames = ["fine_peak_avgdist_synsize_nonperiodic_L=16_J1=["+J1+"]_Q=16_"+quantity_symbol,
                 "fine_peak_avgdist_synsize_nonperiodic_L=16_J1=[" +
                 J1+"]_Q=20_"+quantity_symbol,
                 "fine_peak_avgdist_synsize_nonperiodic_L=16_J1=[" +
                 J1+"]_Q=24_"+quantity_symbol,
                 "fine_peak_avgdist_synsize_nonperiodic_L=16_J1=[" +
                 J1+"]_Q=28_"+quantity_symbol,
                 "fine_peak_avgdist_synsize_nonperiodic_L=16_J1=[" +
                 J1+"]_Q=32_"+quantity_symbol,
                 "fine_peak_avgdist_synsize_nonperiodic_L=16_J1=["+J1+"]_Q=36_"+quantity_symbol]
    df_sub = []
    for index, filename in enumerate(filenames):
        df_sub.append(ascii.read(path + filename + ".txt"))
    # get the column names
    colnames = []
    num_col = len(df_sub[0].keys())
    for index in range(int(num_col/2)):
        colnames.append([df_sub[0].keys()[index*2],
                         df_sub[0].keys()[index*2+1]])

    size_compare_ploting(df_sub=df_sub, colnames=colnames,
                         quantity=quantity, quantity_symbol=quantity_symbol, J1=J1)
