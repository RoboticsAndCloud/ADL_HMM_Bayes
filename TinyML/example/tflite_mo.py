from tflite_runtime.interpreter import Interpreter
from PIL import Image
import numpy as np
import time

def load_labels(path): # Read the labels from the text file as a Python list.
  with open(path, 'r') as f:
    return [line.strip() for i, line in enumerate(f.readlines())]

def set_input_tensor(interpreter, image):
  tensor_index = interpreter.get_input_details()[0]['index']
  input_tensor = interpreter.tensor(tensor_index)()[0]
  input_tensor[:, :] = image

def classify_image(interpreter, image, top_k=2):
  set_input_tensor(interpreter, image)

  interpreter.invoke()
  output_details = interpreter.get_output_details()
  print("output details:", output_details)
  output_details = interpreter.get_output_details()[0]
  print("output2 details:", output_details)
  output = np.squeeze(interpreter.get_tensor(output_details['index']))
  print('output1:', output)
  prediction_classes = np.argmax(output)
  print('prediction_classes:', prediction_classes)

  scale, zero_point = output_details['quantization']
  output = scale * (output - zero_point)
  print('output:', output)

  ordered = np.argpartition(-output, 1)
  return [(i, output[i]) for i in ordered[:top_k]][0]

data_folder = "./"
data_folder_image = "./hometest/"

#model_path = "./home_model.tflite"
model_path = "./home_model20.tflite"
label_path = data_folder + "labels_home_v1.txt"

interpreter = Interpreter(model_path)
print("Model Loaded Successfully.")

interpreter.allocate_tensors()
_, height, width, _ = interpreter.get_input_details()[0]['shape']
print("Image Shape (", width, ",", height, ")")

# Load an image to be classified.
#image = Image.open(data_folder + "test.jpg").convert('RGB').resize((width, height))
#image = Image.open(data_folder_image + "bathroom2.jpg").convert('RGB').resize((width, height))
#image = Image.open(data_folder_image + "kitchen_test.jpg").convert('RGB').resize((width, height))
image = Image.open(data_folder_image + "livingroom_test.jpg").convert('RGB').resize((width, height))

# Classify the image.
time1 = time.time()
label_id, prob = classify_image(interpreter, image)
print("label id:", label_id)
time2 = time.time()
classification_time = np.round(time2-time1, 3)
print("Classificaiton Time =", classification_time, "seconds.")

# Read class labels.
labels = load_labels(label_path)

# Return the classification label of the image.
classification_label = labels[label_id]
print("Image Label is :", classification_label, ", with Accuracy :", np.round(prob*100, 2), "%.")
