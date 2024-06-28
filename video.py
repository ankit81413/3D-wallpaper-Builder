import cv2
import os

def create_video():
    image_folder = 'images'
    video_name = 'output_video2.avi'
    
    # Get the list of image files
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort(key=lambda x: int(x.split("image")[1].split(".png")[0]))  # Sort the image files by frame number
    
    # Get image dimensions
    img = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, _ = img.shape
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter(video_name, fourcc, 20, (width, height))
    
    for image in images:
        image_path = os.path.join(image_folder, image)
        frame = cv2.imread(image_path)
        print("Processing frame:", image.split("image")[1].split(".png")[0])  # Print the frame number
        video.write(frame)
    
    cv2.destroyAllWindows()
    video.release()

if __name__ == "__main__":
    create_video()
