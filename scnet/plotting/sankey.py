import matplotlib
from matplotlib import pyplot as plt
from scnet.plotting import _alluvial

font = {'family': 'Arial',
        'weight': 'bold',
        'size': 14}

matplotlib.rc('font', **font)
matplotlib.rc('ytick', labelsize=14)
matplotlib.rc('xtick', labelsize=14)


def sankey_diagram(data, save_path=None, show=False, **kwargs):
    plt.close('all')
    ax = _alluvial.plot(data.tolist(),
                        color_side=kwargs.get("color_side", 1),
                        alpha=kwargs.get("alpha", 0.5),
                        x_range=kwargs.get("x_range", (0, 1)),
                        res=kwargs.get("res", 20),
                        figsize=kwargs.get("figsize", (21, 15)),
                        disp_width=kwargs.get("disp_width", True),
                        width_in=kwargs.get("width_in", True),
                        wdisp_sep=kwargs.get("wdisp_sep", ' ' * 2),
                        cmap=kwargs.get("cmap", matplotlib.cm.get_cmap('jet')),
                        v_gap_frac=kwargs.get("v_gap_frac", 0.03),
                        h_gap_frac=kwargs.get("h_gap_frac", 0.03),
                        labels=kwargs.get("labels", None),
                        fontname=kwargs.get("fontname", "Arial"),
                        )
    if save_path is not None:
        plt.savefig(save_path, dpi=kwargs.get("dpi", 200), bbox_inches='tight')
    if show:
        plt.show()
    plt.close()
