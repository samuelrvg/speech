import wave
import json
from vosk import Model, KaldiRecognizer

# Carrega o modelo (substitua "model" pelo caminho para a sua pasta de modelo, se necessário)
model = Model("model")

# Abre o arquivo de áudio
wf = wave.open("audio-ptBR.wav", "rb")

# Verifica se o áudio está no formato correto
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != 'NONE':
    print("O arquivo de áudio deve ser WAV mono PCM de 16 bits.")
    exit(1)

# Cria o reconhecedor
rec = KaldiRecognizer(model, wf.getframerate())

# Realiza a transcrição
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        res = rec.Result()
        result = json.loads(res)
        print(result['text'])
    else:
        rec.PartialResult()

# Resultado final
res = rec.FinalResult()
result = json.loads(res)
print("Transcrição:", result['text'])