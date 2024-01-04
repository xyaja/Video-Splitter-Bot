from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import asyncio

# splitting given video into equal parts
async def split_parts(file_path, parts):
    video = VideoFileClip(file_path)
    video_length = video.duration
    duration_per_part = video_length / parts
    output_folder = f'{file_path}/Parts'
    
    for i in range(parts):
        logger.info("splitting started")
        start_time = i * duration_per_part
        logger.info(f"start_time :- {start_time}")
        output_file = os.path.join(output_folder, f"part{i+1}.mp4")
        end_time = start_time + duration_per_part
        vpart = await video.subclip(start_time, end_time)
        vpart.write_videofile(output_file)

        return output_folder
