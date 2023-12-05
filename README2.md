# Dejavu Audio Fingerprinting and Recognition System Output Explanation

The Dejavu system generates an output dictionary after processing an audio file. This document explains what each key-value in the output represents.

## Keys Explanation

- `total_time`: The total time taken by the system to process the audio file and return a result. Includes fingerprinting, querying, and aligning time.

- `fingerprint_time`: The time taken to create a fingerprint of the audio file.

- `query_time`: The time taken to query the database for the audio fingerprint.

- `align_time`: The time taken to align the matches found in the database.

- `results`: A list of potential matches found in the database. Each item in the list is a dictionary with the following keys:

  - `song_id`: The ID of the song in the database.

  - `song_name`: The name of the song in the database.

  - `input_total_hashes`: The total number of hashes (fingerprints) generated from the input audio.

  - `fingerprinted_hashes_in_db`: The number of hashes of the song stored in the database.

  - `hashes_matched_in_input`: The number of hashes that matched between the input audio and the song in the database.

  - `input_confidence`: A measure of confidence in the match, based on the proportion of input audio hashes that matched with the song in the database.

  - `fingerprinted_confidence`: A measure of confidence in the match, based on the proportion of song hashes in the database that matched with the input audio.

  - `offset`: The time offset between the input audio and the song in the database, measured in units of the audio's sample rate.

  - `offset_seconds`: The time offset between the input audio and the song in the database, measured in seconds.

  - `file_sha1`: The SHA-1 hash of the song file in the database.

The `results` list is sorted by `input_confidence`, with the most confident match first. If the system is confident in its match, the first item in the `results` list will be the correct match.

Please note that the actual accuracy of the system can depend on factors such as the quality and diversity of the audio data in the database, the quality of the audio sample being recognized, and the specific parameters used for fingerprinting and recognition.


# Usage Guide for Audio Recognition Python Script

This Python script takes a single audio file to be fingerprinted and another file to be recognized. It uses the Dejavu library to perform audio recognition.

## Requirements
- Python 3.6 or above
- Dejavu library installed (`pip install pydejavu`)

## Command Line Arguments
This script requires two input arguments:

1. `fingerprint_file`: The path to the audio file to be found.
2. `recognize_file`: The path to the audio file (sets) to be searched.

## Usage
To use this script, navigate to the directory containing your Python file in your terminal, and then run the following command:

```bash
python vast_cather_docker.py /path/to/fingerprint/file /path/to/recognize/file


# Usage Guide for YouTube to MP3 Downloader

This script allows you to download the audio from a YouTube video as an MP3 file.

## Requirements
- Python 3.6 or above
- `yt-dlp` and `ffmpeg` installed (`pip install yt-dlp` and `sudo apt-get install ffmpeg`)

## Usage
To use this script, navigate to the directory containing the Python file in your terminal, and then run the following command:

```bash
python ytdownload.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
