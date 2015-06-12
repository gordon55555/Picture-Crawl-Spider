##################################################################
#author   : Wuxupeng                                             #
#date     : 2015.6.11                                            #
#function : Convert the jpg picture to the fixed size of picture #              
#         :                                                      #
##################################################################
import os
import sys
import numpy
#import pylab
from PIL import Image
import os.path
import glob
import cPickle

def ReadFileList(sourcefile):
    filename = sourcefile
    listfile = os.listdir(filename)
    return listfile

def convertjpg(jpgfile ,sourcefile, outdir, width=500, height=720):
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    i = 0    
    for jpg in jpgfile:
        try:
            img=Image.open(sourcefile+r'/'+jpg) 
            print "convert " + str(i) + "th" 
            new_img=img.resize((width,height),Image.BILINEAR)  
            outadd =  os.path.join(outdir,str(i)+'.jpg') 
            new_img.save(outadd)
            i = i + 1
        except Exception as err:
            print "This jpg has some problem, so skip it!"
     
def convall(file):
    allfile = ReadFileList(file)
    convfile = []
    for tem in allfile:
        if os.path.isdir(file+r'/'+tem):
            convfile.append(tem)
    print convfile
    for tem in convfile:
        sourcefile = r'./link/'+tem
        print sourcefile
        sourcelist = ReadFileList(sourcefile)
        destlist   = r'./DealDate/'+ tem
        convertjpg(sourcelist ,sourcefile, destlist, 32, 24)

def convpickle():
    fileList = ReadFileList(r'./DealDate')
    i = 0
    #len = 0
    #for files in fileList:
    #    file = ReadFileList(r'./DealDate/'+files)
    #    len = len + len(file)
    
    img = []
    for files in fileList:
        file = ReadFileList(r'./DealDate/'+files)
        for f in file:
            address = r'./DealDate/'+files+r'/'+f
            fp = open(address,'r')
            img.append(numpy.asarray(Image.open(fp),dtype='float64') / 256)
            fp.close()
            i = i+1
            print i
    train = numpy.asarray(img)
    print type(train)
    add = r'./PickleDate/'+'train'+'.pkl'
    
    f0 = open(add, 'wb')
    cPickle.dump(train,f0)
    f0.close()

    '''
        
    img = Image.open(open('./3wolfmoon.jpg'))
    #print type(img)
    img =[ [[1,2,3],[4,5,6],[7,8,9]],
           [[10,11,13],[14,15,16],[17,18,19]],
           [[21,22,23],[24,25,26],[27,28,29]]]
    img = numpy.asarray(img, dtype='float64') 
    img_ = img.transpose(2, 0, 1).reshape(1, 3, 3, 3)
    print img_
    '''
#####################################################################

convall(r'./link')
convpickle()
#print "convent finished"


