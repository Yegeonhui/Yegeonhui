from PIL import Image
from PIL.ExifTags import TAGS
def get_exif(filename):
    image=Image.open(filename)
    info=image._getexif()
    return info


info=get_exif("C:/Users/admin/desktop/직박구리/Geonhui/extra/사진/1.jpg")
taglabel={}
for tag,value in info.items():
    decoded=TAGS.get(tag,tag) 
    print(decoded)
    taglabel[decoded]=value
print(taglabel)