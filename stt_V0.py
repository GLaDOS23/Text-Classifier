import speech_recognition as sr
from pydub import AudioSegment

def mp3_to_text(mp3_file):
    # Конвертируем MP3 в WAV
    #audio = AudioSegment.from_mp3(mp3_file)
    #wav_file = "converted.wav"
    #audio.export(wav_file, format="wav")
    wav_file = mp3_file
    # Инициализируем распознаватель
    recognizer = sr.Recognizer()

    # Открываем файл для распознавания
    with sr.AudioFile(wav_file) as source:
        audio_data = recognizer.record(source)

    # Распознаем речь
    try:
        text = recognizer.recognize_google(audio_data, language="ru")#"en-US")
        print("Распознанный текст: ", text)
        return text
    except sr.UnknownValueError:
        print("Google Web Speech API не смог распознать аудио")
    except sr.RequestError as e:
        print(f"Не удалось получить результаты от Google Web Speech API; {e}")

# Укажите путь к вашему MP3 файлу
mp3_file_path = "Озвучка Фила.wav"
mp3_to_text(mp3_file_path)
