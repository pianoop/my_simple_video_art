import cv2 as cv

video_file = 'example2.webm'

video = cv.VideoCapture(video_file)

if video.isOpened():
    fps = video.get(cv.CAP_PROP_FPS)
    wait_msec = int(1 / fps * 1000)
    
    while True:
        valid, img = video.read()
        if not valid:
            break

        h, w = img.shape[:2]
        img2 = cv.resize(img, (w//2, h//2))
        edge = 255 - cv.Laplacian(img2, -1)
        #img = cv.bitwise_and(img, edge)
        cv.imshow('Video Player', edge)

        key = cv.waitKey(wait_msec)
        if key == 27: # ESC
            break

    cv.destroyAllWindows()
