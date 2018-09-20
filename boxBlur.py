
def bowBlur(image):
  blurred = []
  for i in range(1, len(image) - 1):
    for j in range(1, len(image[i]) - 1):
      blurred.append([image[i - 1][j - 1], image[i - 1][j], image[i - 1][j + 1],
  image[i][j - 1], image[i][j], image[i][j + 1],
  image[i + 1][j - 1], image[i + 1][j], image[i + 1][j + 1]])
  return blurred



image = [[36, 0,18,9], 
        [27,54, 9, 0], 
        [81,63,72,45]]

threeByThree = (bowBlur(image))
print(threeByThree[1])
