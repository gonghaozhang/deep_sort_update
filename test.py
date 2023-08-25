import tensorflow as tf
import sklearn
import cv2
print(cv2.__version__)
print(sklearn.__version__)
print(tf.__version__)


#cd "C:\Users\12062\Desktop\Research - Deng\deep_sort"
#python deep_sort_app.py --sequence_dir=./MOT16/test/MOT16-06 --detection_file=./resources/detections/MOT16_POI_test/MOT16-06.npy --min_confidence=0.3 --nn_budget=100 --display=True


#python tools/generate_detections.py --model=resources/networks/mars-small128.pb --mot_dir=./MOT16/train --output_dir=./resources/detections/MOT16_train

#python tools/generate_detections.py --model=resources/networks/mars-small128.pb --mot_dir=./MOT15/train --output_dir=./resources/detections/MOT15_train