import speech_recognition as sr
from pydub import AudioSegment
import os

def split_audio(mp3_file, segment_length=10000):
    audio = AudioSegment.from_mp3(mp3_file)
    duration = len(audio)
    segments = []
    for start in range(0, duration, segment_length):
        end = min(start + segment_length, duration)
        segment = audio[start:end]
        segments.append(segment)
    return segments

def recognize_audio(segment_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(segment_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language="ru-RU")
            return text
        except sr.UnknownValueError:
            return "Google Web Speech API не смог распознать аудио"
        except sr.RequestError as e:
            return f"Не удалось получить результаты от Google Web Speech API; {e}"

def process_mp3_to_text(mp3_file):
    segments = split_audio(mp3_file)
    result = []
    
    for i, segment in enumerate(segments):
        # Экспортируем каждый сегмент в WAV файл
        segment_path = f"segment_{i}.wav"
        segment.export(segment_path, format="wav")
        
        # Преобразуем сегмент в текст
        text = recognize_audio(segment_path)
        print(f"Segment {i} text: {text}")
        result.append(text)
        
        # Удаляем временный файл сегмента
        os.remove(segment_path)
    
    return " ".join(result)

# Укажите путь к вашему MP3 файлу
mp3_file_path = "Озвучка Фила.mp3"
full_text = process_mp3_to_text(mp3_file_path)
print("Полный текст: ", full_text)
