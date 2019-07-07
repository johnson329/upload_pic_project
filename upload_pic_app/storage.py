from django.core.files.storage import FileSystemStorage
import os,time,random

class ImageStorage(FileSystemStorage):
    def __init__(self,location=None, base_url=None, file_permissions_mode=None,
                 directory_permissions_mode=None):
        super(ImageStorage,self).__init__(location,base_url)
    def _save(self, name, content):
        #图片扩展名
        ext=os.path.splitext(name)[1]
        #路径
        file_dir=os.path.dirname(name)
        #文件名
        fn=time.strftime('%Y%m%d%H%M%S')
        fn=fn+"_%s"%random.randint(0,1000)
        name=os.path.join(file_dir,fn+ext)
        return super(ImageStorage,self)._save(name,content)




