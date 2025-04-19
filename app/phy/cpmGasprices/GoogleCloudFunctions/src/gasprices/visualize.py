import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import math
import os
from matplotlib.ticker import (MultipleLocator,
                               FormatStrFormatter,
                               AutoMinorLocator)


def generate_save_plot_e5_diesel(df, location, title, subtitle, filename):
    plt.rcdefaults()
    font_path = os.getcwd()+'/resources/LinLibertine_Rah.ttf'
    font_manager.fontManager.addfont(font_path)
    prop = font_manager.FontProperties(fname=font_path)

    plt.style.use('Solarize_Light2')
    px = 1/plt.rcParams['figure.dpi']

    plt.rcParams['font.family'] = "sans-serif"
    plt.rcParams['font.sans-serif'] = prop.get_name()

    colors = plt.rcParams["axes.prop_cycle"]()

    px = 1/plt.rcParams['figure.dpi']
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1,
                                   sharex=True, figsize=(640*px, 360*px))

    #fig.suptitle(title, fontsize=24, fontproperties=prop)
    fig.suptitle(title, fontsize=24)

    e5min = df['e5'][df['e5'] > 0.1].min()
    e5max = df['e5'][df['e5'] > 0.1].max()
    e5min = (math.floor(e5min*100)/100)-0.01
    e5max = (math.ceil(e5max*100)/100)+0.01
    #print(e5min, e5max)
    dieselmin = df['diesel'][df['diesel'] > 0.1].min()
    dieselmax = df['diesel'][df['diesel'] > 0.1].max()
    dieselmin = (math.floor(dieselmin*100)/100)-0.01
    dieselmax = (math.ceil(dieselmax*100)/100)+0.01

    c = next(colors)["color"]
    ax1.plot(df.e5, label='e5', color=c)
    #ax1.set_title(subtitle, fontproperties=prop)
    ax1.set_title(subtitle)
    # ax1.legend(prop=prop)
    ax1.legend()
    ax1.set_ylim([e5min, e5max])
    #ax1.set_ylabel("Preis", fontproperties=prop)
    ax1.yaxis.set_major_formatter(FormatStrFormatter('% 1.2f'))

    c = next(colors)["color"]
    ax2.plot(df.diesel, label='diesel', color=c)
    # ax2.legend(prop=prop)
    ax2.legend()
    ax2.set_ylim([dieselmin, dieselmax])
    #ax2.set_ylabel("Preis", fontproperties=prop)

    plt.tight_layout()
    plt.savefig(filename)
    # plt.show()
    plt.clf()
