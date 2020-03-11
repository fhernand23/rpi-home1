from skimage import metrics
import numpy as np
import cv2


class ImageUtil():
    def __init__(self, image1, image2):
        # load the images
        self.image1 = cv2.imread(image1)
        self.image2 = cv2.imread(image2)
        # convert the images to grayscale
        self.image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        self.image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    def mse(self):
        # the 'Mean Squared Error' between the two images is the
        # sum of the squared difference between the two images;
        # NOTE: the two images must have the same dimension
        err = np.sum((self.image1.astype("float") - self.image2.astype("float")) ** 2)
        err /= float(self.image1.shape[0] * self.image2.shape[1])

        # return the MSE, the lower the error, the more "similar"
        # the two images are
        return err

    def compare_images(self):
        # compute the mean squared error and structural similarity
        # index for the images
        # m = self.mse()
        ssim = metrics.structural_similarity(self.image1, self.image2)

        # return strutctural similarity
        return ssim

    def are_similar(self):
        ssim = self.compare_images()

        if ssim > 0.95:
            # similar
            return True
        else:
            print("similarity: ", ssim)
            return False
