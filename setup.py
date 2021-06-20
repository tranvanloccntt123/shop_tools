import os
dir_path = os.path.dirname(os.path.realpath(__file__))
crop_path = dir_path+'//crop/'
download_path = dir_path+'//download/'
mock_path = dir_path+'//mock/'
mockup_path = dir_path+'//mockup/'
excel_path = dir_path+'//excel/'

if os.path.exists(r""+crop_path) == False:
    os.mkdir(r""+crop_path)

if os.path.exists(r""+download_path) == False:
    os.mkdir(r""+download_path)

if os.path.exists(r""+mock_path) == False:
    os.mkdir(r""+mock_path)

if os.path.exists(r""+mockup_path) == False:
    os.mkdir(r""+mockup_path)

if os.path.exists(r""+excel_path) == False:
    os.mkdir(r""+excel_path)