#  Function for coloring the diagonal of an image based on a given color dictionary.
def color_diag(img, diag, dict):
  """
  Parameters:
  - img: The image to be colored (3D list).
  - diag: The diagonal values to determine colors.
  - dict: The color dictionary mapping values to RGB colors.

  Returns:
  - The colored image.
  """
  for i in range(len(diag)):
    for x in range(0 + (100 * i), 100 + (100 * i)):
      for y in range(100):
        pixel = img[x][y]

        # Set RGB values based on the color dictionary
        pixel[0] = dict[diag[i]][0]
        pixel[1] = dict[diag[i]][1]
        pixel[2] = dict[diag[i]][2]

  return img


# Function used to color the entire board of an image based on a given color dictionary.
def color_board(img, grid, dict):
  """
  Parameters:
  - img: The image to be colored (3D list).
  - grid: The grid of values to determine colors.
  - dict: The color dictionary mapping values to RGB colors.

  Returns:
  - The colored image.
  """
  for i in range(len(grid)):
    for x in range(0 + (100 * i), 100 + (100 * i)):
      for j in range(len(grid)):
        for y in range(0 + (100 * j), 100 + (100 * j)):
          pixel = img[x][y]

          # Get the value from the grid
          key = int(grid[i][j])

          # Set RGB values based on the color dictionary
          pixel[0] = dict[key][0]
          pixel[1] = dict[key][1]
          pixel[2] = dict[key][2]

  return img
