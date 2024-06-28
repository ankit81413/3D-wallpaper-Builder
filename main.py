import eel
import os
import base64
import json
import cv2


# Set web files folder
eel.init('web')

frame = 0

def imagename():
    global frame
    imagge = "image" + str(frame) + ".png"
    frame += 1
    return imagge


@eel.expose()
def reload():
    global frame
    frame = 0

@eel.expose
def save_image(image_data):
    global frame  # Use the global frame variable
    # Create the 'images' folder if it doesn't exist
    if not os.path.exists('images'):
        os.makedirs('images')
    
    # Extract the base64 encoded image data
    image_data = image_data.split(",")[1]

    getname = imagename()
    imaggee = os.path.join('images', getname)  # Join folder path with filename

    
    # Decode and save the image to the 'images' folder
    with open(imaggee, 'wb') as f:
        f.write(base64.b64decode(image_data))

    print("successfully added "+imaggee)






def check_and_update_json():
    file_path = r"C:\Users\Ankit\Desktop\bulk eel\web\data.json"
    try:
        # Check if the file exists
        if os.path.exists(file_path):
            # Check if the file is empty
            if os.path.getsize(file_path) == 0:
                # Write "{}" to the file
                with open(file_path, 'w') as file:
                    file.write("{}")
                print(f"File '{file_path}' was empty. Updated with '{{}}'.")
            else:
                print(f"File '{file_path}' is not empty. No update required.")
        else:
            print(f"File '{file_path}' does not exist.")
    except Exception as e:
        print(f"Error occurred: {e}")


check_and_update_json()





@eel.expose
def save_data(data):
    update_json_file(data)
    print(data)
    print("saved")


@eel.expose
def update_json_file(json_data):
    file_path = r"C:\Users\Ankit\Desktop\bulk eel\web\data.json"
    try:
        # Write the JSON data to the file
        with open(file_path, 'w') as file:
            json.dump(json_data, file, indent=4)
        
        print("JSON file updated successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")



gmode = "save"


@eel.expose  # Expose this function to JavaScript
def getmode():
    global gmode
    print("Python function called")
    return gmode


@eel.expose
def choosemode(mode):
    global gmode
    if mode == "save":
        gmode = "save"
        print(gmode)

    else:
        gmode = "mass_production"
        print(gmode)




@eel.expose
def create_video(wallpaper_name):
    image_folder = 'images'
    # video_name = 'output_video2.avi'
    video_name = wallpaper_name[:-4]+".avi"
    
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

 





@eel.expose
def movietime(thef):
    image_folder = 'images'
    
    # Get the list of image files
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    
    # Get the total number of images
    total_images = len(images)

    

    print("you have to crate the movie total are "+str(total_images)+" and the thef is "+ str(thef))








@eel.expose
def delete_files_in_folder():
    folder_path=r"C:\Users\Ankit\Desktop\bulk eel\images"
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Iterate over each file and delete it
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):  # Check if it's a file
            os.remove(file_path)  # Delete the file
    print("ALL FILES IN THIS FOLDER HAVE BEEN DELETED")



eel.start('choose_mode.html', size=(800, 600))

