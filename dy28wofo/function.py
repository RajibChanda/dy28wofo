import numpy as np
from ipywidgets import interact, fixed
from PIL import Image
def imshow(X, resize=None):
    """
    resizes an image by the given parameter.
    Returns:
        Shows a resized image
    Args:
        X = Either an image url or a 2D numpy array 
        resize = a tuple of targetted size, if this is empty then default size would be 512X512
    """
    if(resize == None):
        resize = (512,512)
    try: 
        if (str(type(X) == "numpy.ndarray")):
            X = Image.fromarray(X)
        #img = Image.open(X)
        resized_img = X.resize(resize)
        resized_img.show()
    except:
            print("Only accepts numpy array or an image url")