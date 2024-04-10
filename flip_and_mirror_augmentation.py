from __future__ import annotations
import albumentations as A

import os
import cv2
    
def load_yolo_bboxes(file_path):
    boxes = []
    labels = []

    with open(file_path, "r") as f:
      for line in f:
        data = line.split()
        labels.append(data[0])
        boxes.append([float(data[1]), float(data[2]), float(data[3]), float(data[4])])

    return (boxes, labels)

def write_yolo_bboxes(box_bounds, class_labels, file_path):
    if len(box_bounds) != len(class_labels):
        print("number of bounding boxes mismatched with number of labels")
        raise ValueError
    
    with open(file_path, "w") as f:
       i = 0
       while i < len(class_labels):
          f.write(f"{class_labels[i]} {box_bounds[i][0]} {box_bounds[i][1]} {box_bounds[i][2]} {box_bounds[i][3]}\n")
          i += 1

# TO DO: Load labels and images as a list and loop through them
label_file = f"{os.getcwd()}\\obj_Train_data\\frame_000081.txt"
image_file = f"{os.getcwd()}\\obj_Train_data\\frame_000081.PNG"

bb_data = load_yolo_bboxes(label_file)
boxes, labels = bb_data
print(boxes)
print(labels)

image = cv2.imread(image_file)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Can modify this to do resizing and such, just set to flipping right now
transform_pipeline = A.Compose([
    A.HorizontalFlip(p=0.5),
  ],bbox_params = A.BboxParams(
        format="yolo",
        label_fields=["class_labels"],
    ))

transformed = transform_pipeline(image=image, bboxes=boxes, class_labels=labels)

print(transformed["bboxes"])

cv2.imwrite(f"{os.getcwd()}\\obj_Train_data\\augmented\\frame_000081.PNG", transformed["image"])
write_yolo_bboxes(transformed["bboxes"], transformed["class_labels"], f"{os.getcwd()}\\obj_Train_data\\augmented\\frame_000081.txt")