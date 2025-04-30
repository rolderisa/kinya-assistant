from gtts import gTTS
from pydub import AudioSegment
import os

qa_pairs = {
    "Rwanda Coding Academy iherereye he?": "Iherereye mu Karere ka Nyabihu, mu Ntara y’Iburengerazuba.",
    "Umurwa mukuru w’u Rwanda ni uwuhe?": "Ni Kigali.",
    "U Rwanda rwavukiye ryari?": "Rwavukiye tariki ya 1 Gicurasi 1962.",
    "Ikipe y'igihugu y’u Rwanda yitwa nde?": "Ni Amavubi.",
    "Ururimi rw'icyongereza mu Rwanda ni iryande?": "Ni ururimi rwa gatatu nyuma rw’Ikinyarwanda n’Igifaransa."
}

output_dir = "audio_qa"
os.makedirs(output_dir, exist_ok=True)

for i, (question, answer) in enumerate(qa_pairs.items(), 1):
    # Generate TTS
    tts_q = gTTS(text=question, lang='rw')
    tts_a = gTTS(text=answer, lang='rw')

    mp3_q = os.path.join(output_dir, f"question_{i}.mp3")
    mp3_a = os.path.join(output_dir, f"answer_{i}.mp3")

    wav_q = os.path.join(output_dir, f"question_{i}.wav")
    wav_a = os.path.join(output_dir, f"answer_{i}.wav")

    # Save MP3
    tts_q.save(mp3_q)
    tts_a.save(mp3_a)

    # Convert MP3 to WAV
    sound_q = AudioSegment.from_mp3(mp3_q)
    sound_a = AudioSegment.from_mp3(mp3_a)

    sound_q.export(wav_q, format="wav")
    sound_a.export(wav_a, format="wav")

    # Clean up MP3 files
    os.remove(mp3_q)
    os.remove(mp3_a)

print("✅ WAV files successfully generated!")
