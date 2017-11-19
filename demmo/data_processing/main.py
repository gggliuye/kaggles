
import json
import numpy as np

'''
id - the id of the image

band_1, band_2 - the flattened image data. Each band has 75x75 pixel values in
the list, so the list has 5625 elements. Note that these values are not the
normal non-negative integers in image files since they have physical meanings
- these are float numbers with unit being dB. Band 1 and Band 2 are signals
characterized by radar backscatter produced from different polarizations at
 a particular incidence angle. The polarizations correspond to HH (transmit
 /receive horizontally) and HV (transmit horizontally and receive vertically).
 More background on the satellite imagery can be found here.

inc_angle - the incidence angle of which the image was taken. Note that this
field has missing data marked as "na", and those images with "na" incidence
angles are all in the training data to prevent leakage.

is_iceberg - the target variable, set to 1 if it is an iceberg, and 0 if it is
 a ship. This field only exists in train.json.
'''

train_data = json.load(open('data/train.json'))
outdir = 'data/train_batch'
outdirt = 'data/test_batch'
outdir_test = 'data/eval_batch'

def write(image, outdirx):
  newfile = open(outdirx, 'ab')
  image = bytes(image)
  newfile.write(image)
  newfile.close()

def write_label(byte, outdirx):
  newfile = open(outdirx, 'ab')
  newfile.write(byte.to_bytes(1, byteorder='big'))

def make_train_bin():
  for i in range(1200):
    band_1 = train_data[i]["band_1"]
    band_2 = train_data[i]["band_2"]
    id_i = train_data[i]["id"]
    label = train_data[i]["is_iceberg"]
    band1 = dosth(band_1)
    band2 = dosth(band_2)
    #image size (75,75)
    write_label(label, outdir)
    write(band1, outdir)
    write(band2, outdir)

    if i%50 == 0:
      print("make %d bin file success"%i)

def make_eval_bin():
  for j in range(400):
    i = j + 1200
    band_1 = train_data[i]["band_1"]
    band_2 = train_data[i]["band_2"]
    id_i = train_data[i]["id"]
    label = train_data[i]["is_iceberg"]
    band1 = dosth(band_1)
    band2 = dosth(band_2)
    #image size (75,75)
    write_label(label, outdir_test)
    write(band1, outdir_test)
    write(band2, outdir_test)

    if i%50 == 0:
      print("make %d bin file success"%i)

def make_train_once():
  for i in range(1):
    band_1 = train_data[i]["band_1"]
    band_2 = train_data[i]["band_2"]
    id_i = train_data[i]["id"]
    label = train_data[i]["is_iceberg"]
    band1 = dosth(band_1)
    band2 = dosth(band_2)
    #image size (75,75)
    x = np.uint8(1)
    print(x)
    write(x, outdirt)
    label = 0
    print(label)
    write_label(label, outdirt)
    write(band1, outdirt)
    write(band2, outdirt)

    if i%50 == 0:
      print("make %d bin file success"%i)


def dosth(image):
    max1 = max(image)
    min1 = min(image)
    for i in range(5625):
        image[i] = (image[i] - min1) * 255 / (max1 - min1)
        image[i] = int(image[i])
    return image

#make_train_once()
make_train_bin()
make_eval_bin()
