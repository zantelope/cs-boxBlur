def boxBlur(image):

  #empty array to place values within the 3x3 matrix
  threeByThreeVals = []
  
  #empty array to place the average of values within 3x3 matrix
  threeByThreeAvgs = []
  
  #empty array to place average values into a matrix
  blurredMatrix = []


  #find the values of elements within all 3x3 matrixes and place in threeByThreeVals list
  #start loops at 1 and stop at one before the length's end since no elements at the ends 
  #can be the center of a 3x3 matrix
  for i in range(1, len(image) - 1):
    for j in range(1, len(image[i]) - 1):
      threeByThreeVals.append(
        #determine values of 3x3 matrixes with image[i][j] at center
        [image[i - 1][j - 1], image[i - 1][j], image[i - 1][j + 1],
         image[i][j - 1], image[i][j], image[i][j + 1],
         image[i + 1][j - 1], image[i + 1][j], image[i + 1][j + 1]])

  #calculate averages of 3x3 matrixes, round down to the nearest integer, and add them 
  #into threeByThreeAvgs list
  for i in range(len(threeByThreeVals)):
    threeByThreeAvgs.append(int(sum(threeByThreeVals[i]) / len(threeByThreeVals[i])))



  # A for loop goes from 0 to the length of the threeByThreeAvgs list, each iteration increases i 
  # by the length of image[0] - 2, which is the length of blurredMartix[x] that I want. This way when 
  # the list is sliced using i for the beginning of the slice it starts on the correct location and and 
  # i + image[0] - 2 ends the slice at the correct length.

  for i in range(0, len(threeByThreeAvgs), (len(image[0]) - 2)):
    blurredMatrix.append(threeByThreeAvgs[i:i + (len(image[0]) - 2)])


  #return blurred matrix
  return blurredMatrix
