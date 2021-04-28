# Crop using ffmpeg

import os


class Crop:

    def __init__(self):
        # Get data from user
        self.file_loc = input("File (Location): ")
        self.start_time = input("Start (00:00:00): ")
        self.duration = input("Duration (00:00:00): ")
        self.output_file = input("Output (Location): ")

    def crop_video(self):
        command = f"ffmpeg -i {self.file_loc} -ss {self.start_time} -t {self.duration} -vcodec copy -acodec copy {self.output_file}"
        os.system(command)


if __name__ == "__main__":
    crop = Crop()
    crop.crop_video()
