import numpy
#import theano
#import theano.tensor as T
#import lasagne
import Image
import re
import os
import shutil
#from theano.tensor.signal.pool import downsample
from collections import OrderedDict
import pylab

import time

def get_data(img_path,label_path):
       
        #open and store image as numpy array
        img = Image.open(img_path)
        d = numpy.array(img)
        img.close()

        #open and store txt file as numpy array
	label = open(label_path)
        content = label.readlines()
        str1=content[0]
        
        #Extract all the integers from the string
        listOfInt =  map(int,re.findall('\d+',str1))
        y = numpy.array(listOfInt)
        label.close()

        return OrderedDict(input=d,truth=y)

#input: the origin path to the label
# format generated
# pathOfFile NumberOfTarget Position1OfTarget Position2OfTarget

def positive_txtFile_Generator
    
#take in 2 






#Takes in the label files and if the file is empty, move them to a negative sample file
#input the original path of label and image file
#input destination of destination negative sample label and image file
def move_negative_file(path_label, path_image,destination_label,destination_img):
   
    for filename in os.listdir(path_label):
       
        full_path_label = os.path.join(path_label, filename)
        name = os.path.splitext(filename)[0] 
        full_path_image = os.path.join(path_image, name + '.jpg')
        
        try:
                if os.stat(full_path_label).st_size == 0:
                    print filename
                    shutil.move(full_path_label, destination_label)
         #          print os.statd(full_path_label).st_size 
                    shutil.move(full_path_image, destination_img ) 
        except OSError:
                print 'No Such File'

    return None

def main():
    '''
    #----------------------------------------------------------------------------------
    # takes in a file with a list of label names
    #path to the file with labels

    path_label = '/home/amy/Desktop/all_data/label'
    path_image = '/home/amy/Desktop/all_data/img'
    destination_label = "/home/amy/Desktop/all_data/negative_label"
    destination_img = '/home/amy/Desktop/all_data/negative_img'

    move_negative_file(path_label, path_image,destination_label,destination_img)
    #------------------------------------------------------------------------------------ 
    '''
    # data = get_data("/home/amy/Desktop/all_data/img/i_245.jpg","/home/amy/Desktop/all_data/label/i_245.txt")

if __name__ == "__main__":
    main()
