from moviepy.video.io.VideoFileClip import VideoFileClip


def equal_parts(filename, parts):
    video = VideoFileClip("video.mp4")
    duration = video.duration

    part1_start = 0 
    part1_end = duration / 4
    part2_start = duration  / 4
    part2_end = 2 * duration / 4
    part3_start = 2 * duration / 4
    part3_end = 3 * duration / 4
    part4_start = 3 * duration / 4
    part4_end = duration

    part1 = video.subclip(part1_start, part1_end)
    part2 = video.subclip(part2_start, part2_end)
    part3 = video.subclip(part3_start, part3_end)
    part4 = video.subclip(part4_start, part4_end)


    part1.write_videofile("part1.mp4")
    part2.write_videofile("part2.mp4")
    part3.write_videofile("part3.mp4")
    part4.write_videofile("part4.mp4")



# splitting into 3 equal parts
def three_equal_parts():
    video = VideoFileClip("video.mp4")
    duration = video.duration
    part1_start = 0
    part1_end = duration / 3
    part2_start = duration / 3
    part2_end = 2 * duration / 3
    part3_start = 2 * duration / 3
    part3_end = duration
    
    
    part1 = video.subclip(part1_start, part1_end)
    part2 = video.subclip(part2_start, part2_end)
    part3 = video.subclip(part3_start, part3_end)


    part1.write_videofile("part1.mp4")
    part2.write_videofile("part2.mp4")
    part3.write_videofile("part3.mp4")


# splitting into 2 equal parts
def two_equal_parts():
    video = VideoFileClip("video.mp4")
    duration = video.duration
    part1_start = 0
    part1_end = duration / 2
    part2_start = duration / 2
    part2_end = 2 * duration / 2


    part1 = video.subclip(part1_start, part1_end)
    part2 = video.subclip(part2_start, part2_end)
    
    
    part1.write_videofile("part1.mp4")
    part2.write_videofile("part2.mp4")



# custome splitting
def custome(time):
    video = VideoFileClip("video.mp4")
    duration = video.duration
    part1_start = 0
    part1_end = time
    part2_start = time
    part2_end = duration


    part1 = video.subclip(part1_start, part1_end)
    part2 = video.subclip(part2_start, part2_end)


    part1.write_videofile("part1.mp4")
    part2.write_videofile("part2.mp4")
