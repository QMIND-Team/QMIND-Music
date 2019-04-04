# Next Steps

## Tristan

Goal: Create a 2D array that translates the qualities of an image to the music-generating neural net.

### What went well

- Functional program
- Normalized data to improve performance
- Classifies image as one of 12 categories based on the dominant colour

### Overview

The goal of image processing is to classify each image in a unique manner. However, it should be systematic - similar images should have similar arrays. This will result in the music output by images sounding similar as well.

The challenge is that images do not map to music naturally. They are both artistic work, but they do not share any characteristics. 

Similarly, there is no "right/wrong" answer to train a neural network with. Any program will be heavily subject to user bias depending on how images and songs were paired (that is how we trained our network).

_So how do we process images?_

Each image needs to be transformed into an array of numbers - 200x64 in this case. The array should represent the important characteristics of the image. What do you think about when you are trying to sort images into different piles? One or multiple of those traits will be used to enumerate each image.

We employed the KAZE algorithm to sort images into keypoints. The more features an image has, the more keypoints. In general, descriptor vectors for highly defined features (sharp colour/shading changes) contain larger numbers.

The KAZE algorithm is typically used for image matching - detecting whether two images are the same despite perspective or brightness changes. However, we are not looking for identical images. We are systematically classifying images. As such, we may want to take into account other methods.

__Here are some issues and next steps for the image analysis section:__

### Removing 0's

The output data is a list of 64-element vectors. The list length is 200, but each image has an average of 30 keypoints. As a result, these arrays are filled with mostly 0's.

This can be fixed by repeating the vectors or filling the space with other data.

Repeating vectors is the easiest method, since they are the right size for the array. The vectors would be placed in the first n spaces, as before, but then each vector would be placed a second time in the same order. This would repeat until all 200 spaces are filled.

Alternatively, each cycle of vectors could be followed by a vector of 0's. Then images with fewer keypoints would still be represented with more 0s. For example, an image with 9 keypoints would have an array with 10% zeros, while an image with 49 keypoints would be filled except for 2% of the vectors.

### Take colour data

Currently the images are being processed exclusively using keypoints. While this is used for matching images, it does not take into account all of the data a human would observe.

Colour is perhaps the primary way humans classify images on first glance. As such,it should be taken into account.

The image_analysis_techniques notebook in the research section describes several methods for colour analysis. They are as follows:

*Dominant colours:* calculates the percentage of the image that each colour occupies.

*Colour vibrance* determines whether an image is colourful or grey. A bright red image will score the maximum value, while a black-and-white checkerboard would score 0.

*Colour turbulence* evaluates how frequently the colour changes in an image, and how significant the change is. It is often proportional to the number of key points, but is calculated in a different way.

Unfortunately each of these calculations outputs one or a few numbers. This would not work for filling a 200x64 array. As such, they would have to be used as multipliers, or constants in a function.

### Transfer learning

Transfer learning applies the front end of a neural network intended for a different purpose to the desired output. 

In this case, an image classifier would output various weights, effectively sorting the image. The output from this classifier would then be used to produce a song.

Pros:

- Classifies images very effectively
- Images that would be matched using the compare network will result in similar songs

Cons:

- Using a function-focused classifier is more concerned on performance than utilizing all the relevant data. Some aspects of the image may be completely ignored, even if a human would take them into account.