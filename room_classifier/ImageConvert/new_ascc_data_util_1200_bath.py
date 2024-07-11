"""
@Brief: Process the data collected from ASCC environment.
@Author: Fei L
@Data: 03/14/2022
"""

from datetime import datetime
from datetime import timedelta

import os

DAY_FORMAT_STR = '%Y-%m-%d'
DATE_HOUR_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

DATE_HOUR_TIME_FORMAT_DIR = '%Y-%m-%d-%H-%M-%S'


ASCC_DATE_HOUR_TIME_FORMAT = '%Y%m%d%H%M%S'


TRAIN_RUNNING_TIME_FORMAT = "%H:%M:%S"


def get_timestamp_map_from_dir(dir, time_difference, copy_flag=False, type='image'):
    path = dir
    count = 0
    prefix = ''
    map_dict = {}
    for fn in os.listdir(path):
        if not os.path.isdir(dir + '/' + fn):
            print(fn)

            ascc_date_str = fn
            ascc_date = ascc_date_str.replace('.jpg', '')
            ascc_date = ascc_date.replace('shot_', '')  # robot
            ascc_date = ascc_date.replace('_000', '')   # robot
            # print('after:', ascc_date)

            if type == 'audio':
                ascc_date = ascc_date_str.replace('_rec.wav', '')
            elif type == 'motion':
                ascc_date = ascc_date_str.replace('_motion.txt', '')

            ascc_activity_time = datetime.strptime(ascc_date, ASCC_DATE_HOUR_TIME_FORMAT)

            ascc_activity_timestamp = ascc_activity_time.timestamp()
            milan_activity_timestamp = ascc_activity_timestamp - time_difference
            milan_activity_time = datetime.fromtimestamp(milan_activity_timestamp)

            mapping_time_str =  milan_activity_time.strftime(DATE_HOUR_TIME_FORMAT)
            print('milan activity mapping time:', mapping_time_str)

            mapping_time_str_dir =  milan_activity_time.strftime(DATE_HOUR_TIME_FORMAT_DIR)


            map_dict[ascc_date] = mapping_time_str

            source_dir = dir + '/' + fn

            new_dir = dir + '/' + mapping_time_str_dir

            print("new_dir:", new_dir)

            cp_cmd = 'cp -r ' + source_dir + ' ' + new_dir 

            print(cp_cmd)
            try:
                if os.path.exists(new_dir) == False:
                    os.mkdir(new_dir)
            except Exception as e:
                print(e)
                pass

            if type == 'motion':
                new_dir += '/motion.txt'
            
            cp_cmd = 'cp -r ' + source_dir + ' ' + new_dir 
            print(cp_cmd)           
            
            try:
                if copy_flag:
                    os.system(cp_cmd)
            except Exception as e:
                print(e)
                pass

            # rotate_dir = source_dir + '_rotate'
            # print("rotate_dir:", rotate_dir)
            # if source_dir.find('rotate') > -1:
            #     continue
            


            count = count +1

        else:
            print('fn:', fn)


    # count = sum([len(files) for root, dirs, files in os.walk(dir)])
    return map_dict


def get_timestamp_map(test_dir, milan_activity_date, ascc_date_str, copy_flag = False, type = 'image'):
    # milan_activity_date = '2009-12-11 09:10:27'
    milan_activity_time = datetime.strptime(milan_activity_date, DATE_HOUR_TIME_FORMAT)
    milan_activity_time_start = milan_activity_time

    # ascc_date_str = '20220309214619_rotate'
    ascc_date = ascc_date_str.replace('_rotate', '')
    ascc_activity_time = datetime.strptime(ascc_date, ASCC_DATE_HOUR_TIME_FORMAT)

    milan_activity_time_start_time_stamp = milan_activity_time_start.timestamp()
    ascc_activity_timestamp = ascc_activity_time.timestamp()
    diff = ascc_activity_timestamp - milan_activity_time_start_time_stamp
    print('milan timestamp:', milan_activity_time_start_time_stamp, 'ascc:', ascc_activity_timestamp,'diff:', diff)

    # test_dir = '/home/ascc/Desktop/white_case_0309_1211/activity_data/kitchen_activity'
    map_dict = get_timestamp_map_from_dir(test_dir, diff, copy_flag, type)

    sd = sorted(map_dict.items())
    print('Mapping')
    print('Milan \t ASCC')
    for k,v in sd:
        print(v, '\t', k)

    for k,v in sd:
        print("'"+str(k)+"'" + ",")

    print('cnt:', len(map_dict))


def generate_data_from_dir(dir, duration):
    path = dir
    count = 0
    source_dir_list = ['20220309220103',
'20220309220112',
'20220309220122',
'20220309220131',
'20220309220140',
'20220309220150',
'20220309220159',
'20220309220209',
'20220309220218',
'20220309220238',
'20220309220249',

'20220309220102',
'20220309220111',
'20220309220121',
'20220309220130',
'20220309220139',
'20220309220149',
'20220309220158',
'20220309220208',
'20220309220217',
'20220309220237',
'20220309220248',]

    map_dict = {}
    for fn in os.listdir(path):
        if os.path.isdir(dir + '/' + fn):
            print(fn)

            ascc_date_str = fn
            ascc_date = ascc_date_str.replace('_rotate', '')
            if ascc_date not in source_dir_list:
                continue

            ascc_activity_time = datetime.strptime(ascc_date, ASCC_DATE_HOUR_TIME_FORMAT)

            new_ascc_activity_time = ascc_activity_time + timedelta(seconds = duration)

            new_ascc_time_str =  new_ascc_activity_time.strftime(ASCC_DATE_HOUR_TIME_FORMAT)

            print('new_ascc_time_str:', new_ascc_time_str)
            map_dict[ascc_date] = new_ascc_time_str

            source_dir = dir + '/' + fn

            new_dir = dir + '/' + new_ascc_time_str

            print("new_dir:", new_dir)

            mv_cmd = 'mv ' + source_dir + ' ' + new_dir

            print(mv_cmd)
            
            try:
                os.system(mv_cmd)
            except Exception as e:
                print(e)
                pass

            count = count +1

        else:
            print('fn:', fn)

    return map_dict


def generate_data_from_dir_kitchen_copy(dir):
    path = dir
    count = 0
    source_dir_list = ['20220309215209',
'20220309215222',
'20220309215231',
'20220309215241',
'20220309215250',
]

    map_dict = {}
    for fn in os.listdir(path):
        if os.path.isdir(dir + '/' + fn):
            print(fn)

            ascc_date_str = fn
            ascc_date = ascc_date_str.replace('_rotate', '')
            if ascc_date not in source_dir_list:
                continue

            ascc_activity_time = datetime.strptime(ascc_date, ASCC_DATE_HOUR_TIME_FORMAT)

            new_ascc_activity_time = ascc_activity_time + timedelta(seconds = 60 *15)

            new_ascc_time_str =  new_ascc_activity_time.strftime(ASCC_DATE_HOUR_TIME_FORMAT)

            print('new_ascc_time_str:', new_ascc_time_str)
            map_dict[ascc_date] = new_ascc_time_str



            source_dir = dir + '/' + fn

            new_dir = dir + '/' + new_ascc_time_str

            print("new_dir:", new_dir)

            cp_cmd = 'cp -r ' + source_dir + ' ' + new_dir

            print(cp_cmd)
            
            try:
                os.system(cp_cmd)
            except Exception as e:
                print(e)
                pass

            count = count +1

        else:
            print('fn:', fn)

    return map_dict


milan_activity_date = '2009-12-11 12:00:54'

ascc_date_str = '20240618035643'
# base_path = '/home/ascc/Desktop/adl_0819/activity/0846_kitchen/'
base_path = '/home/ascc/LF_Workspace/Bayes_model/IROS23/ADL_HMM_BAYES/Data_Apartment/Offline/Watch/'

base_dir = "120054_bath"

images = base_path +  'Image/' + base_dir

# get_timestamp_map(test_dir=images, milan_activity_date=milan_activity_date, ascc_date_str=ascc_date_str)

# # Generate final data dir
# get_timestamp_map(test_dir = images,milan_activity_date=milan_activity_date, ascc_date_str=ascc_date_str, copy_flag=True)

audio = base_path + 'Audio/' + base_dir

# get_timestamp_map(test_dir=audio, milan_activity_date=milan_activity_date, ascc_date_str=ascc_date_str,copy_flag=False, type = 'audio')


# # Generate final data dir
# get_timestamp_map(test_dir=audio, milan_activity_date=milan_activity_date, ascc_date_str=ascc_date_str,copy_flag=True, type = 'audio')


motion = base_path + 'Motion/' + base_dir

# get_timestamp_map(test_dir=motion, milan_activity_date=milan_activity_date, ascc_date_str=ascc_date_str, copy_flag=False, type = 'motion')


# # # Generate final data dir
get_timestamp_map(test_dir=motion, milan_activity_date=milan_activity_date, ascc_date_str=ascc_date_str,copy_flag=True, type = 'motion')



# milan_activity_date = '2009-12-11 08:46:27'
# ascc_date_str = '20220819144013_rotate'
# ascc_date_str = '20240618032743'
# base_path = '/home/ascc/Desktop/adl_0819/activity/0846_kitchen/'
# base_path = '/home/ascc/LF_Workspace/Bayes_model/IROS23/ADL_HMM_BAYES/Data_Apartment/Offline/Robot/0619/image/084627_kitchen'
images = '/home/ascc/LF_Workspace/Bayes_model/IROS23/ADL_HMM_BAYES/Data_Apartment/Offline/Robot/0619/image/' + base_dir


# get_timestamp_map(test_dir=images, milan_activity_date=milan_activity_date, ascc_date_str=ascc_date_str)

# # Generate final data dir
# get_timestamp_map(test_dir = images,milan_activity_date=milan_activity_date, ascc_date_str=ascc_date_str, copy_flag=True)