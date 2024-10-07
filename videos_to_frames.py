

'''
I have 5 HEVC video files each 1 minute long. 
Each video is filmed at 20 frames per second 
corresponding to 1200 frames per video. 
The following code block will read in a HEVC file
and produce 1200 frames. 
'''


# Importing relevant packages  
import os 
import cv2 

# Extracting the frames from the HEVC videos
def extract_frames_from_videos(video_path, output_dir, frames_per_video=1200):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if video opened successfully
    if not cap.isOpened():
        print(f"Error: Could not open video {video_path}")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # We will manually count frames
    frame_count = 0
    saved_frame_count = 0
    success, frame = cap.read()

    # Extract frames manually and stop at 1200
    while success and saved_frame_count < frames_per_video:
        # Save the frame if we haven't reached 1200 yet
        frame_filename = os.path.join(output_dir, f"frame_{saved_frame_count + 1:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        saved_frame_count += 1

        # Read the next frame
        success, frame = cap.read()
        frame_count += 1

    cap.release()
    print(f"Extracted {saved_frame_count} frames to {output_dir}\n")

# Main script to process multiple videos
def process_videos(video_files, output_base_dir, frames_per_video=1200):
    for idx, video_file in enumerate(video_files):
        video_filename = os.path.basename(video_file).split('.')[0]
        output_dir = os.path.join(output_base_dir, f"video_{idx}")

        extract_frames_from_videos(video_file, output_dir, frames_per_video)

# Video names
video_files = [
    'labeled/0.hevc', 
    'labeled/1.hevc',
    'labeled/2.hevc',
    'labeled/3.hevc',
    'labeled/4.hevc',
    'unlabeled/5.hevc',
    'unlabeled/6.hevc',
    'unlabeled/7.hevc',
    'unlabeled/8.hevc',
    'unlabeled/9.hevc',
]

output_base_dir = 'extracted_frames'  # Directory to store extracted frames
process_videos(video_files, output_base_dir)