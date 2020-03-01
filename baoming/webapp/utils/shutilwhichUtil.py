import shutil
import os
from baoming.settings import MEDIA_URL, MEDIA_ROOT
import time


# term_picture_root = MEDIA_ROOT + "\\term_picture"
# if os.path.exists(term_picture_root):
#     pass
# else:
#     os.makedirs(term_picture_root)
# n_path = term_picture_root + '\\5b88a805-b82d-4f.jpg'
# o_path = r'D:\PycharmProjects\lelingzdy\baoming\media\images\2019\08\5b88a805-b82d-4f.jpg'
# # o_path = o_path.replace("\\",'/')
# shutil.copy(o_path, term_picture_root)
# reset_path = term_picture_root + '\\ssss@回宿舍.jpg'
# if not os.path.exists(reset_path):
#     os.rename(n_path, reset_path)
# else:
#     pass

# print(shutil.disk_usage('D:'))
# shutil.make_archive(term_picture_root, 'zip', term_picture_root)


def term_worker_picture(term_name, worker, username, picture_type, picture_path):
    # images/2019/07/72739cf9-b27c-45.jpg
    term_picture_root = MEDIA_ROOT + "/" + term_name + '/' + worker
    if os.path.exists(term_picture_root):
        pass
    else:
        os.makedirs(term_picture_root)
    picture_path_str = str(picture_path)
    path_str = str(picture_path_str).split('/')
    picture_name = path_str[len(path_str) - 1]
    n_path = term_picture_root + '/' + picture_name
    if not os.path.exists(n_path):
        o_path = MEDIA_ROOT + "/" + picture_path_str
        # o_path = o_path.replace("\\",'/')
        # 将文件拷贝到指定目录
        shutil.copy(o_path, term_picture_root)
        # 先进行拷贝，再修改名字
        # 如果不存在这个文件则拷贝创建
        reset_path = term_picture_root + '/' + username + '_' + picture_type + '_' + picture_name
        if not os.path.exists(reset_path):
            # 如果已有同名图片，则跳过
            os.rename(n_path, reset_path)
        else:
            pass
    else:
        # 如果存在则不创建
        pass




def term_make_archive(term_name):
    term_picture_root = MEDIA_ROOT + "/" + term_name
    if os.path.exists(term_picture_root):
        term_picture_root_new = MEDIA_ROOT + "/" + str(time.time()).replace('.', '_')
        shutil.make_archive(term_picture_root_new, 'zip', term_picture_root)
        term_name_time = term_picture_root_new + '.zip'
        return term_name_time
    else:
        return None
