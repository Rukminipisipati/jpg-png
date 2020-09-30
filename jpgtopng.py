import sys
import os
from PIL import Image,ImageFilter
image_folder=sys.argv[1]
output_folder=sys.argv[2]
#os.makedirs(image_folder)
#print(os.path.exists(image_folder))
if not os.path.exists(output_folder):
	os.makedirs(output_folder)
#print(os.path.exists(output_folder))
for filename in os.listdir(image_folder):
		img=Image.open(f'{image_folder}{filename}')
		clean_name=os.path.splitext(filename)[0] #splits the filename to get the first name and add extension.
		img.save(f'{output_folder}{clean_name}.png','png')
		#print('all done')

# c=1
# for filename in os.listdir(image_folder):
#     if filename.endswith(".jpg"):
#         im = Image.open(filename)
#         name='img'+str(c)+'.png'
#         rgb_im = im.convert('RGB')
#         rgb_im.save(output_folder,'png')
#         c+=1
#         print(os.path.join(output_folder, filename))
#         continue
#     else:
#         continue
