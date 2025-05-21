import matplotlib.pyplot as plt
import numpy as np

category_names = ["strongly disagree", "disagree", "Niether agree nor disagree", "agree", "strongly agree"]

results = {
    "Question 1" : [13,10,14,20,13],
    "Question 2" : [15,12,19,23,10],
    "Question 3" : [12,11,18,22,30],
    "Question 4" : [30,4,18,12,17],
    "Question 5" : [23,11,12,21,18]
}

def survey(results, category_names):
    """
    Parameters
    """"""""
    results : dict
        This is a survey got from field survey.
        Kiingsley
        It matches the length of "category_names"
    category_names : list of str
        The category labels.
    """
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis = 1)
    category_colors = plt.colormaps["nipy_spectral"](np.linspace(0.15, 0.85, data.shape[1])) # Contetual Help can be used to source for names of other color types

    fix, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis = 1).max())
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left = starts, height = 0.5, label = colname, color = color)
        r, g, b, _   = color
        text_color = "white" if r * g * b < 0.5 else "blue"
        ax.bar_label(rects, label_type = "center", color = text_color)
        ax.legend(ncols = len(category_names), bbox_to_anchor = (0,1), loc = "lower left", fontsize = "small")
    return fix,ax
survey(results, category_names)
plt.show()
#  git add .
#  git commit -m "Matplotlib"
#  git push