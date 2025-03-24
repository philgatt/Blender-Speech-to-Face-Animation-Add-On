import wave
import contextlib
from vosk import Model, KaldiRecognizer
from .speech_processing import transcribeFile, ConvertEnglishToIpa
from .animation import animateMesh

keyframesPerSecond = 30

def CheckAudioFileLength(audio_path):
    with contextlib.closing(wave.open(audio_path, 'r')) as f:
        return f.getnframes() / float(f.getframerate())

def RunScript(props):
    model = Model(props.model_path)
    audio_length = CheckAudioFileLength(props.audio_path)
    words = transcribeFile(props.audio_path, model)
    ConvertEnglishToIpa(words)
    animateMesh(props, words)
    print("Lip Sync Complete")