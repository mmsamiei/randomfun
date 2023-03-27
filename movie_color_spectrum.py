import cv2
import numpy as np 
import einops
from tqdm.auto import tqdm
import sys

if __name__ == "__main__":
    path = sys.argv[1]
    vidcap = cv2.VideoCapture(path)
    num_total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    mean_pixles = []
    for i in tqdm(range(num_total_frames)):
        success,image = vidcap.read()    # save frame as JPEG file
        mean_pixle = einops.reduce(image.astype(float), 'h w c -> c', 'mean')
        mean_pixles.append(mean_pixle)
    color_spectrum = np.array(mean_pixles)
    color_spectrum = einops.repeat(color_spectrum, 'w c -> h w c', h=400)
    cv2.imwrite('output.png', color_spectrum)


