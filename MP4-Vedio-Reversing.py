import cv2

# Getting the vedio
ved = cv2.VideoCapture('E:\\Python Programs\\Extras\\Automated-Web-func\\Youtube Downloader\\YTDownloader_vedio-2021-4-30-20-13.mp4')

## Properties of the vedio
# Total no. of frames in the vedio
frames = ved.get(cv2.CAP_PROP_FRAME_COUNT)

# FPS of the vedio
fps = ved.get(cv2.CAP_PROP_FPS)

# Height and Width of the vedio
height = ved.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = ved.get(cv2.CAP_PROP_FRAME_WIDTH)

## Initiating the output vedio writter
fourcc = cv2.VideoWriter_fourcc(*'MJPG')

# Creating the output vedio writter 
out = cv2.VideoWriter('e://Python Programs//Extras//Cv2//Vedio-Reversing//reversed.avi',fourcc, fps, (int(width), int(height)))

# Getting the last frame of the vedio
frame_index = frames - 1
print(f'no. of frames in the vedio is {frames}')
# checking the vedio instance is ready
  
if ved.isOpened():
    
    while frame_index != 0:
        # Setting the frame index of the vedio 
        ved.set(cv2.CAP_PROP_POS_FRAMES,frame_index)
        # getting the vedio frame of the frame index
        RET, frame = ved.read()

        # Writting the frame onto the output vedio writter
        out.write(frame)

        # Getting the previous frame index
        frame_index -= 1

        # Showing the Remaining frames to be written onto the output vedio writter
        if frame_index%100 == 0:
            print(frame_index)