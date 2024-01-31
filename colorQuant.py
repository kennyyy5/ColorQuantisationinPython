import numpy as np
from PIL import Image
import copy
import math

# Inputs:
#     img: m by n by 3 array of integers representing the color values of a photo
#     rGroups: integer representing the number of groups of red color values
#     gGroups: integer representing the number of groups of green color values
#     bGroups: integer representing the number of groups of blue color values
# constraints: 
#     1 <= rGroups, gGroups, bGroups <= 256
#     0 <= all integers in img <= 255
# Output: returns an m by n by 3 (same dimensions as input img array), 
#         with its color values quantized according to the specified group parameters
def colorQuantize( img, rGroups, gGroups, bGroups ):
    # your code goes here!
    rSepa = math.floor(256/rGroups)
    gSepa = math.floor(256/gGroups)
    bSepa = math.floor(256/bGroups)
    
    start = 0
    end = rSepa
    rArray = []
    for i in range(rGroups):
      rArray.append([])
      for j in range(start, end):
        rArray[i].append(j)
      start += rSepa
      end += rSepa
      if rArray[i][rSepa-1] == 254 and gGroups % 2 != 0:
         rArray[i].append(255)

    start = 0
    end = gSepa
    gArray = []
    for i in range(gGroups):
      gArray.append([])
      for j in range(start, end):
        gArray[i].append(j)
      start += gSepa
      end += gSepa
      if gArray[i][gSepa-1]==254 and gGroups % 2 != 0:
         gArray[i].append(255)

    start = 0
    end = bSepa
    bArray = []
    for i in range(bGroups):
      bArray.append([])
      for j in range(start, end):
        bArray[i].append(j)
      start += bSepa
      end += bSepa
      if bArray[i][bSepa-1]==254 and bGroups % 2 != 0:
         bArray[i].append(255)
    
    rArrayMid = []
    for i in range(rGroups):
      if(len(rArray[i])==rSepa):
        rArrayMid.append(math.ceil((rArray[i][0]+rArray[i][len(rArray[i])-1])/2))
      else:
        rArrayMid.append(math.floor((rArray[i][0]+rArray[i][len(rArray[i])-1])/2))

    gArrayMid = []
    for i in range(gGroups):
      if(len(gArray[i])==gSepa):
        gArrayMid.append(math.ceil((gArray[i][0]+gArray[i][len(gArray[i])-1])/2))
      else:
        gArrayMid.append(math.floor((gArray[i][0]+gArray[i][len(gArray[i])-1])/2))

    bArrayMid = []
    for i in range(bGroups):
      if(len(bArray[i])==bSepa):
        bArrayMid.append(math.ceil((bArray[i][0]+bArray[i][len(bArray[i])-1])/2))
      else:
        bArrayMid.append(math.floor((bArray[i][0]+bArray[i][len(bArray[i])-1])/2))
    # create image copy
    for i in range(len(img)):  
        for j in range(len(img[0])):    
            for k in range(3):
                if k==0:
                    for l in range(len(rArray)):  # investigate
                        for m in range(len(rArray[l])):
                            if img[i][j][k]==rArray[l][m]:
                                img[i][j][k] = rArrayMid[l]
                if k==1:
                    for l in range(len(gArray)):
                        for m in range(len(gArray[l])):
                            if(img[i][j][k]==gArray[l][m]):
                                img[i][j][k] =  gArrayMid[l]
                if k==2:
                    for l in range(len(bArray)):
                        for m in range(len(bArray[l])):
                            if img[i][j][k]==bArray[l][m]:
                                img[i][j][k] =  bArrayMid[l]

    return img
# Testing and starter code provided in main(): 
