

size_finding.py -   This code gives us the number of imgaes in a bin and the dimensions of the dataset. Run for the entire set of 3.9k images.Out put stored in an exel sheet






number of x_rays.ipynb- this file gives us the number of stacked xrays per image of the dataset (e.g 3 ,4 or 5 per radiographic image).Run for the entire datase. Output stored in exel sheet




final_splitting.ipynb- This file helps in splitting the radiographic images according to the no. of xrays stacked in each.It is run for the entire dataset.output images stored in the given directory


CUTPICS.ipynb   - This file cuts a sample taken from the split images to a dimension as desired. The dimension of cutting is based on the original size of the image. images stored in directory


resizingcode.ipynb  - This file reads the sample cut imgaes obtained from CUTPICS.ipynb and resizes them to the dimensions 299*2999 and 299*500 so these images can be
			given as input for the feature extraction done by the pre trained CNN models.Images stored in directory mentioned.



Feature_extraction.ipynb-   This file gives the feature vectors for the images run in it and stores the vectors in an exel sheet. after extracting the vectors, the code also runs to find the distances between 100 sample images and the 80 images of defective and non defective images.These distances are again stored in exel sheet.
				this code is run for both the CNN models, Resnet50 and inception_v3.



Removing letters.py   - This has the first part of removing letters in a picture it is finds the letters that are present in the welding images.

