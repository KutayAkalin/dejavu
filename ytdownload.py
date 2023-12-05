import os
import sys

def download_mp3(youtube_url, file_name):
    # Create the directory if it doesn't exist
    if not os.path.exists('yt_mp3'):
        os.makedirs('yt_mp3')
    
    # Format the command with the provided URL and file name
    command = f'yt-dlp -f "bestaudio[ext=m4a]" --extract-audio --audio-format mp3 --audio-quality 0 --output "yt_mp3/{file_name}.%(ext)s" {youtube_url}'
    
    # Execute the command
    os.system(command)

def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python ytdownload.py <youtube_url> <file_name>")
        sys.exit(1)

    # Extract the arguments
    youtube_url = sys.argv[1]
    file_name = sys.argv[2]

    # Call the download function
    download_mp3(youtube_url, file_name)

if __name__ == "__main__":
    main()
