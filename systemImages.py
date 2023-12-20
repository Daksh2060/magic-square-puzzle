import pygame
import numpy


# Function used to load an image from a file and convert it to a 3D list of pixels.
def getImage(filename):
  """
  Parameters:
  - filename: The path to the image file.

  Returns:
  - A 3D list representing the image pixels.
  """
  image = pygame.image.load(filename)
  return pygame.surfarray.array3d(image).transpose(1, 0, 2).tolist()


# Functions used to save a 3D list of pixels as an image file.
def saveImage(pixels, filename):
  """
  Parameters:
  - pixels: A 3D list representing the image pixels.
  - filename: The desired path and name of the output image file.
  """
  nparray = numpy.asarray(pixels).transpose(1, 0, 2)
  surf = pygame.surfarray.make_surface(nparray)
  
  # Create a new display surface with the specified width and height
  (width, height, colours) = nparray.shape
  surf = pygame.display.set_mode((width, height))
  
  # Copy the pixel values to the surface
  pygame.surfarray.blit_array(surf, nparray)
  
  # Save the surface as an image file
  pygame.image.save(surf, filename)


#Function creates a black image with the specified width and height.
def getBlackImage(width, height):
  """
  Parameters:
  - width: The width of the black image.
  - height: The height of the black image.

  Returns:
  - A 3D list representing a black image.
  """
  return [[[0, 0, 0] for i in range(width)] for j in range(height)]
