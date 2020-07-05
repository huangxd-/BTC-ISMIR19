import os
import pinyin

def chinese_2_pinyin(name):
    #name = name.replace("(", "-").replace(")", "-").replace(" ", "-")
    return pinyin.get(name, format="strip")

def mp3_2_wav(audio_path):
    dirname = os.path.dirname(audio_path)
    name, ext = os.path.splitext(os.path.basename(audio_path))
    output_path = audio_path

    # name to yinpin
    name_pinyin = chinese_2_pinyin(name)

    if ext == ".mp3":
        output_path = os.path.join(dirname, name_pinyin + ".wav")
        cmd = "lame --decode '%s' '%s'; rm -rf '%s'" % (audio_path, output_path, audio_path)
        os.system(cmd)
    return output_path
