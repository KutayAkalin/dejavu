import json
import argparse
from dejavu import Dejavu
from dejavu.logic.recognizer.file_recognizer import FileRecognizer
import os 

config = {
    "database": {
        "host": "db",
        "user": "postgres",
        "password": "password",
        "database": "dejavu"
    },
    "database_type": "postgres"
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fingerprint file and recognize file.')
    parser.add_argument('fingerprint_file', type=str, help='The file to be fingerprinted.')
    parser.add_argument('recognize_file', type=str, help='The file to be recognized.')

    args = parser.parse_args()

    # create a Dejavu instance
    djv = Dejavu(config)

    # Fingerprint a single file
    djv.fingerprint_file(args.fingerprint_file)

    # Recognize audio from a file using the shortcut
    results = djv.recognize(FileRecognizer, args.recognize_file)
    print(f"From file we recognized: {results}\n")
