import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import image as mpimg


class ScrapBooker:

    @staticmethod
    def crop(array, dim, pos=(0, 0)):
        if pos[0]+dim[0] >= array.shape[0] or pos[1]+dim[1] >= array.shape[1]:
            print("ERROR : Dimensions or position value too high for the image")
        else:
            return array[pos[0]:pos[0] + dim[0], pos[1]:pos[1] + dim[1]]

    @staticmethod
    def thin(array, n, axis):
        if n >= array.shape[axis]:
            print("ERROR : n is too high, nothing changed")
        else:
            return np.delete(array, np.s_[::n], axis)

    @staticmethod
    def juxtapose(array, n, axis):
        res = array
        for i in range(n - 1):
            res = np.concatenate((array, res), axis)
        return res

    @staticmethod
    def mosaic(array, dim):
        res = array
        for i in range(dim[0] - 1):
            res = np.concatenate((array, res), 0)
        array = res
        for i in range(dim[1] - 1):
            res = np.concatenate((array, res), 1)
        return res


# img = mpimg.imread("5.png")
# img = ScrapBooker.crop(img, (500, 500))
# img = img * (1, 0, 0)
# img = ScrapBooker.juxtapose(img, 10, 0)
# imgplot = plt.imshow(img)
# plt.show()
