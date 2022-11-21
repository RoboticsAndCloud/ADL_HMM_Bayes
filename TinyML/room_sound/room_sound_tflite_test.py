# -*- coding: utf-8 -*-
"""
@author: Jason Zhang
@github: https://github.com/JasonZhang156/Sound-Recognition-Tutorial
"""

from tflite_runtime.interpreter import Interpreter
# from keras.models import load_model
# import tensorflow as tf
import esc10_input
import numpy as np
import os
import time

labels = ['door_open_closed', 'eating', 'keyboard', 'pouring_water_into_glass', 'toothbrushing', 'vacuum',
 'drinking', 'flush_toilet', 'microwave', 'quiet', 'tv_news', 'washing_hand']

ob_folder = '/home/ascc/LF_Workspace/Bayes_model/Product_ADL/ADL_HMM_BAYES/room_sound/sound_dataset/ascc_activity_1second/feature/ascc_logmel_total.npz'
num_class = len(labels)
mean, std = esc10_input.get_mean_std(ob_folder, 'logmel',num_class)

MOTION_TFLITE_MODEL = './sound_default_model.tflite'


def use_gpu():
    """Configuration for GPU"""
    # from tensorflow.compat.v1.keras.backend import set_session
    os.environ['CUDA_VISIBLE_DEVICES'] = str(0)
    # config = tf.ConfigProto()
    config = tf.compat.v1.ConfigProto()
    config.gpu_options.per_process_gpu_memory_fraction = 0.5
    config.gpu_options.allow_growth = True
    set_session(tf.compat.v1.InteractiveSession(config=config))


def predict_tflite(test_data):


    model_path = MOTION_TFLITE_MODEL

    # bathroom: 0, bedroom:1, kitchen:2, livingroom:3, hallway:4, door:5
    # labels=['bathroom','bedroom', 'kitchen','livingroom', 'hallway', 'door']
    # # label_path = data_folder + "labels_home_v1.txt"
    # print("labels:", labels)


    interpreter = Interpreter(model_path)
    print("Model Loaded Successfully.")

    interpreter.allocate_tensors()

    shape = interpreter.get_input_details()[0]['shape']
    print("interpreter input Shape:", shape)



    # set_input_tensor(interpreter, image)
    input_index = interpreter.get_input_details()[0]['index']

    
    # todo for loop to get the result
    # test_sound = np.expand_dims(test_data, axis=0).astype(np.float32)
    test_sound = np.float32(test_data)
    print("test_sound shape:", test_sound.shape)


    interpreter.set_tensor(input_index, test_sound)



    time1 = time.time()
    interpreter.invoke()
    time2 = time.time()
    print("time2:", time2)
    classification_time = np.round(time2-time1, 3)
    print("invoken Time =", classification_time, "seconds.")

    output_details = interpreter.get_output_details()
    # print("output details:", output_details)
    output_details = interpreter.get_output_details()[0]
    # print("output2 details:", output_details)
    output = np.squeeze(interpreter.get_tensor(output_details['index']))
    print('output1:', output)
    prediction_classes = np.argmax(output)
    print('prediction_classes:', prediction_classes, " ", labels[prediction_classes])

    return prediction_classes, output[prediction_classes]


def CNN_test(test_fold, feat):
    """
    Test model using test set
    :param test_fold: test fold of 5-fold cross validation
    :param feat: which feature to use
    """
    # model = load_model('./cnn_logmel_foldone_second.h5')

    # 读取测试数据
    # _, _, test_features, test_labels = esc10_input.get_data(test_fold, feat)
    t1 = time.time()
    t2= time.time()
    while(1):
        try:
            t1= time.time()

            path = './mic_data/output.wav'

            # path = './mic_data/output.wav'
            test_feature = esc10_input.get_single_data(path)
            test_feature = np.expand_dims(test_feature, axis=-1)

            test_feature = (test_feature - mean) / std
            test_feature = test_feature.reshape(1,64,138,1)
            #print("test_feature: ",test_feature.shape)
            # 导入训练好的模型

            pre, val = predict_tflite(test_data=test_feature)
            # result = model.predict(test_feature)[0]
            # print(result)
            # pre = labels[np.argmax(result)]
            # val = result[np.argmax(result)]
            # print('pre:', pre, ' val:', val)
            t2 = time.time()
            print("Get_prediction time cost:", np.round(t2-t1, 3))  
            print("Result:", pre, '(' + str(val) + ')') 
            print("=========================================================")

        except Exception as e:
            print(e)

        # print("time (s) used: ",t2 - t1)
        # t1 = t2
        # print('\n')

    # 输出训练好的模型在测试集上的表现
    # score = model.evaluate(test_features, test_labels)
    # print('Test score:', score[0])
    # print('Test accuracy:', score[1])

    # return result


if __name__ == '__main__':
    # use_gpu()  # 使用GPU

    CNN_test(1, 'logmel')

    # dict_acc = {}
    # print('### [Start] Test model for ESC10 dataset #####')
    # for fold in [1, 2, 3, 4, 5]:
    #     print("## Start test fold{} model #####".format(fold))
    #     acc = CNN_test(fold, 'mfcc')
    #     dict_acc['fold{}'.format(fold)] = acc
    #     print("## Finish test fold{} model #####".format(fold))
    # dict_acc['mean'] = np.mean(list(dict_acc.values()))
    # print(dict_acc)
    # print('### [Finish] Test model finished for ESC10 dataset #####')
