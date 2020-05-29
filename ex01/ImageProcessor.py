import matplotlib.image as mpimg
import matplotlib.pyplot as plt


class ImageProcessor:

    def load(self, path):
        return mpimg.imread(path)

    def display(self, obj):
        plt.imshow(obj)
        plt.show()
