import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def imshow(img, text=None, should_save=False):
    """

    :param img:
    :param text:
    :param should_save:
    :return:
    """
    npimg = img.numpy()
    plt.axis("off")
    if text:
        plt.text(75, 8, text, style='italic', fontweight='bold', bbox={'facecolor': 'white', 'alpha': 0.8, 'pad': 10})
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()

def show_plot(iteration, loss):
    """

    :param iteration:
    :param loss:
    :return:
    """
    plt.plot(iteration, loss)
    plt.show()
