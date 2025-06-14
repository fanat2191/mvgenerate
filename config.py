import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCENES_DIR = os.path.join(BASE_DIR, 'scenes')
FRAMES_DIR = os.path.join(BASE_DIR, 'frames')
AUDIO_DIR = os.path.join(BASE_DIR, 'audio')
VIDEO_DIR = os.path.join(BASE_DIR, 'video')
FINAL_DIR = os.path.join(BASE_DIR, 'final')

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
