import shutil
import os
from baoming.settings import MEDIA_URL, MEDIA_ROOT

term_picture_root = MEDIA_ROOT + "\\term_picture"
if os.path.exists(term_picture_root):
    pass
else:
    os.makedirs(term_picture_root)
n_path = term_picture_root + '\\5b88a805-b82d-4f.jpg'
o_path = r'D:\PycharmProjects\lelingzdy\baoming\media\images\2019\08\5b88a805-b82d-4f.jpg'
# o_path = o_path.replace("\\",'/')
shutil.copy(o_path, term_picture_root)
reset_path = term_picture_root + '\\ssss@回宿舍.jpg'
if not os.path.exists(reset_path):
    os.rename(n_path, reset_path)
else:
    pass

print(shutil.disk_usage('D:'))
shutil.make_archive(term_picture_root, 'zip', term_picture_root)


def term_worker_picture(term_name, worker, username, picture_path):
    pass
