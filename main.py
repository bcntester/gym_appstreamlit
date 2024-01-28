import os
import streamlit as st
import math
from streamlit_image_select import image_select


exercises_list = []
def load_images_from_folder(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):
            img_path = os.path.join(folder_path, filename)
            images.append(img_path)
    return images

#images_folder = "./assets/icons/"

def display_images_in_grid(image_paths, grid_columns=3):
    num_images = len(image_paths)
    num_rows = int(math.ceil(num_images / grid_columns))
    images_exercises = []
    captions_img = []
    for row in range(num_rows):
        cols = st.columns(grid_columns)
        for col_index, col in enumerate(cols):
            image_index = row * grid_columns + col_index
            if image_index < num_images:
                # col.image(image_paths[image_index], caption=os.path.basename(image_paths[image_index]))
                images_exercises.append(image_paths[image_index])
                captions_img.append(os.path.basename(image_paths[image_index]))
                
    img_selected = image_select(label="",
                 images=images_exercises,
                 captions=captions_img,
                 )
    return img_selected

def display_videos_in_grid(videos_paths, grid_columns=3):
    selected_videos = []
    num_videos = len(videos_paths)
    num_rows = int(math.ceil(num_videos / grid_columns))
    for row in range(num_rows):
        cols = st.columns(grid_columns)
        for col_index, col in enumerate(cols):
            video_index = row * grid_columns + col_index
            if video_index < num_videos:
                col.video(videos_paths[video_index])
                add_button_key = f"add_button_{video_index}"
                if col.button("Add", key=add_button_key):
                    selected_videos.append(videos_paths[video_index])
    return selected_videos

def load_exercise_images(value):
    exercise_folder = os.path.join(".\\assets\\img", f"{value}_exercises")
    exercise_images = [os.path.join(exercise_folder, f) for f in os.listdir(exercise_folder) if f.endswith(".webp")]    
    return exercise_images

def load_exercise_videos(value):
    exercise_folder = os.path.join(".\\assets\\img", f"{value}_exercises")
    exercise_videos = [os.path.join(exercise_folder, f) for f in os.listdir(exercise_folder) if f.endswith(".mp4")]
    return exercise_videos

def main():

    st.title("Gymapp")
    images_folder = ".\\assets\\icons\\"
    # Check if the folder exists
    if not os.path.exists(images_folder):
        st.error("Folder not found. Please enter a valid path.")
        return

    # Load images from the folder
    image_paths = load_images_from_folder(images_folder)

    # Expander 1: Muscle Groups
    with st.expander("Muscle Groups"):
        if not image_paths:
            st.warning("No .png images found in the specified folder.")
        else:
            # Display images in a grid
            musclegroup_selected = display_images_in_grid(image_paths, grid_columns=3)
            musclegroup_selected = musclegroup_selected.split("icon_")[1]
            musclegroup_selected = musclegroup_selected.split(".")[0]
    # Expander 2: Exercises
    with st.expander("Exercises"):
        exercise_videos = load_exercise_videos(musclegroup_selected)
        selected_videos = display_videos_in_grid(exercise_videos, grid_columns=3)
        exercises_list.extend(selected_videos)
        

    # Expander 3: Exercises Selection
    with st.expander("Exercises Selection"):
        # You can add content related to exercise selection here
        st.write(exercises_list)



if __name__ == "__main__":
    main()
