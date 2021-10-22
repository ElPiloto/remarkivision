import collections
import pdb

import cv2
import numpy as np
import pytesseract as tess
import matplotlib.pyplot as plt
# This is where we define information about the items and positioning in the checklist template
NUM_CHECKBOXES = 16
# This means it has a thickneess of 2
HEADERLINE_Y_START = 191
HEADERLINE_Y_END = 192

# This means it has a width of 1
CHECKBOX_LEFT_X_START = 84
CHECKBOX_LEFT_X_END = 84
CHECKBOX_RIGHT_X_START = 139
CHECKBOX_RIGHT_X_END = 139
CHECKBOX_WIDTH = 56

CHECKBOX_TOP_Y_START = 270
CHECKBOX_TOP_Y_END = 271
CHECKBOX_BOTTOM_Y_START = 325
CHECKBOX_BOTTOM_Y_END = 326
CHECKBOX_HEIGHT = 57

# Top of box2 = top of box1 + this value.
CHECKBOX_INTERTOP_DISTANCE = 97


def get_checkbox_coordinates():
  """Generates coordinates of where we should parse checkboxes."""
  boxes = []
  current_y = CHECKBOX_TOP_Y_START
  for _ in range(NUM_CHECKBOXES):
    top = current_y
    bottom = top + CHECKBOX_HEIGHT - 1
    left = CHECKBOX_LEFT_X_START
    right = CHECKBOX_RIGHT_X_END
    boxes.append((left, right, bottom, top))
    current_y += CHECKBOX_INTERTOP_DISTANCE
  return boxes


def extract_patches(img, patch_coords):
  patches = []
  for c in patch_coords:
    left, right, bottom, top = c
    patches.append(np.copy(img[top:bottom + 1, left:right + 1]))
  return patches


def fill_patches(img, patch_coords, fill_value=0, in_place=False):
  if not in_place:
    img = np.copy(img)
  for coords in patch_coords:
    left, right, bottom, top = coords
    img[top:bottom + 1, left:right + 1] = fill_value
  return img


IMG_FILE = './data/checklist/checklist1.png'

checkbox_coords = get_checkbox_coordinates()
img = cv2.imread(IMG_FILE)

patches = extract_patches(img, checkbox_coords)
filled = fill_patches(img, checkbox_coords, fill_value=0, in_place=False)

plt.subplot(2, 1, 1)
plt.imshow(img)
plt.subplot(2, 1, 2)
plt.imshow(filled)
plt.show()
pdb.set_trace()

# TODO(ElPiloto): Move this to visualization utils.
