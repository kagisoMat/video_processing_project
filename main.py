from supabase import create_client
import ffmpeg

# Supabase URL and API Key (ensure these are secured and not hardcoded in production)
url = "https://kjimrvtpxeuqgtbvfrgb.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtqaW1ydnRweGV1cWd0YnZmcmdiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjY4MjM5MzAsImV4cCI6MjA0MjM5OTkzMH0.TQ_0dGeK3kIOX_Q756ybRYBpoLY-_l4K1ZOzTzQqsQs"
supabase = create_client(url, key)


def upload_video(file_path):
    # Upload video to Supabase
    with open(file_path, "rb") as f:
        supabase.storage.from_("videos").upload("video.mp4", f)



def clip_video(input_file, output_file, start_time, duration):
    """Clips a segment of the video using ffmpeg"""
    try:
        # Clip the video with the specified start time and duration
        (
            ffmpeg
            .input(input_file, ss=start_time, t=duration)
            .output(output_file)
            .run()
        )
        print(f"Video clipped successfully: {output_file}")
    except ffmpeg.Error as e:
        print(f"Failed to clip video: {e.stderr.decode()}")


if __name__ == "__main__":
    # Example usage
    upload_video("long_videos/test.mp4")

    # Clip 5 seconds starting from 10 seconds in the video
    clip_video("long_videos/test.mp4", "output.mp4", start_time=10, duration=5)
