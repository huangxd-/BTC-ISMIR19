import os
import os

def mp3_2_wav(audio_path):
    dirname = os.path.dirname(audio_path)
    name, ext = os.path.splitext(os.path.basename(audio_path))
    output_path = audio_path
    if ext == ".mp3":
        output_path = os.path.join(dirname, name + ".wav")
        cmd = "lame --decode %s %s; rm -rf %s" % (audio_path, output_path, audio_path)
        os.system(cmd)
    return output_path
