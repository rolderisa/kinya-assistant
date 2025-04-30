🗣️ Kinyarwanda Voice Assistant
A lightweight voice assistant that listens to Kinyarwanda speech, transcribes it using Whisper ASR, and responds with synthesized speech via VITS TTS.​


🎯 Features
🎙️ Speech-to-text transcription in Kinyarwanda using mbazaNLP/Whisper-Small-Kinyarwanda.

🔊 Text-to-speech synthesis with facebook/mms-tts-kin.

🤖 Predefined question-answer matching.

📁 Batch processing of .wav files.

🪄 Automatic audio playback on Windows.​

📂 Project Structure


Kin_voice_assistant/
├── audio/               # Input .wav files
├── outputs/             # Generated answer audio files
├── gen.py               # Main script
├── .env                 # Hugging Face token
└── README.md
⚙️ Setup Instructions
Clone the Repository


git clone https://github.com/rolderisa/Kinya-assistant.git
cd Kin_voice_assistant
Create and Activate a Virtual Environment

python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Unix or MacOS
Install Dependencies


pip install -r requirements.txt
Set Up Environment Variables

Create a .env file in the root directory and add your Hugging Face token:


HUG_TOKEN=your_huggingface_token_here
Ensure FFmpeg is Installed

Download and install FFmpeg from ffmpeg.org. Add the bin directory to your system's PATH.

🧪 Usage
Prepare Your Audio Files

Place your .wav files in the audio/ directory. Ensure they are clear recordings in Kinyarwanda.

Run the Assistant


python main.py
View Outputs

The transcribed text and corresponding responses will be displayed in the console. Synthesized answer audio files will be saved in the outputs/ directory and played automatically.