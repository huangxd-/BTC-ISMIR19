# A Bi-Directional Transformer for Musical Chord Recognition

This repository has the source codes for the paper "A Bi-Directional Transformer for Musical Chord Recognition"(ISMIR19).

<img src="png/model.png">

## Requirements
- pytorch >= 1.0.0
- numpy >= 1.16.2
- pandas >= 0.24.1
- pyrubberband >= 0.3.0
- librosa >= 0.6.3
- pyyaml >= 3.13
- mir_eval >= 0.5
- pretty_midi >= 0.2.8

## File descriptions
  * `audio_dataset.py` : loads data and preprocesses label files to chord labels and mp3 files to constant-q transformation. 
  * `btc_model.py` : contains pytorch implementation of BTC.
  * `train.py` : for training. 
  * `crf_model.py` : contatins pytorch implementation of Conditional Random Fields (CRFs) .
  * `baseline_models.py` : contains the codes of baseline models.
  * `train_crf.py` : for training CRFs.  
  * `run_config.yaml` : includes hyper parameters and paths that are needed.
  * `test.py` : for recognizing chord from audio file. 

## Using BTC : Recognizing chords from files in audio directory

### Using BTC from command line
```bash 
$ python test.py --audio_dir audio_folder --save_dir save_folder --voca False
```
  * audio_dir : a folder of audio files for chord recognition (default: './test')
  * save_dir : a forder for saving recognition results (default: './test')
  * voca : False means major and minor label type, and True means large vocabulary label type (default: False)
  
The resulting files are lab files of the form shown below and midi files.

  <img src="png/example.png">

## Attention Map
The figures represent the probability values of the attention of self-attention layers 1, 3, 5 and 8 respectively. The
layers that best represent the different characteristics of each layers were chosen. The input audio is the song "Just A Girl"
(0m30s ~ 0m40s) by No Doubt from UsPop2002, which was in evaluation data.
  <img src="png/attention.png">

## Data
We used Isophonics[1], Robbie Williams[2], UsPop2002[3] dataset which consists of chord label files. Due to copyright issue, these datasets do not include audio files. The audio files used in this work were collected from online music service providers.

[1] http://isophonics.net/datasets 

[2] B. Di Giorgi, M. Zanoni, A. Sarti, and S. Tubaro. Automatic
chord recognition based on the probabilistic
modeling of diatonic modal harmony. In Proc. of the
8th International Workshop on Multidimensional Systems,
Erlangen, Germany, 2013.

[3] https://github.com/tmc323/Chord-Annotations

## Reference
  * pytorch implementation of Transformer and Crf: https://github.com/kolloldas/torchnlp 

## Comments
  * Any comments for the codes are always welcome.


附加：
1. 需要python3
2. 安装pytorch：pip3 install torch==1.5.0+cpu torchvision==0.5.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
3. 没有gpu，则使用torch.load(model_path, map_location='cpu')
4. 安装yum install libsndfile
5. 安装指定版本pip3 install numba==0.48.0
6. SoundFile not support mp3
7. yum install lame; lame --decode <输入_mp3文件> <输出_wav文件>
8. python3 test.py --audio_dir audio_folder --save_dir save_folder --voca True
9. 有汉字需转成拼音 pip3 install pinyin; pinyin.get("你好", format="strip")

参考：
1. https://www.npmjs.com/package/piano-chart
2. https://www.npmjs.com/package/chord-fingering#Data
3. https://www.npmjs.com/package/chord-charter
4. https://www.npmjs.com/package/chord-dictionary
5. https://www.npmjs.com/package/@tombatossals/chords-db
6. https://www.npmjs.com/package/markdown-it-chords
7. https://www.npmjs.com/package/vexflow
8. https://www.npmjs.com/package/chord-illustrator
9. https://www.npmjs.com/package/tonal-chord
10. https://www.npmjs.com/package/chorus
11. https://www.npmjs.com/package/lib-scale-chord-convert
12. https://www.npmjs.com/package/svguitar
13. https://www.npmjs.com/package/jazzband
14. https://www.npmjs.com/package/chordy-svg
15. https://www.npmjs.com/package/react-svg-chord-progressions
16. https://www.npmjs.com/package/vexchords
17. https://www.npmjs.com/package/chordsheetjs
18. https://www.npmjs.com/package/chordictionary
19. https://www.npmjs.com/package/@midiate/midiate
20. https://www.npmjs.com/package/octavian
21. https://www.npmjs.com/package/musictheoryjs
22. https://www.npmjs.com/package/chord-sketch-ui
23. https://www.npmjs.com/package/ember-cli-guitar-chords
24. https://www.npmjs.com/package/soundbank-multi
25. https://www.npmjs.com/package/teoria
26. https://www.npmjs.com/package/react-ukelele
27. https://www.npmjs.com/package/@lyre/fretboard
28. https://www.npmjs.com/package/autocomposer-js
29. https://www.npmjs.com/package/react-chord-generator
30. https://www.npmjs.com/package/vc-chord-diagram
31. https://www.npmjs.com/package/tjn-react-guitar-chord
32. https://www.npmjs.com/package/ukulele-chord
33. https://www.npmjs.com/package/chord.js
34. https://www.npmjs.com/package/scorejs
35. https://www.npmjs.com/package/chordplayer
36. https://www.npmjs.com/package/chordjs
37. https://www.npmjs.com/package/ireal-renderer
38. https://www.npmjs.com/package/sharp11-web-audio
39. https://www.npmjs.com/package/yama-stream
40. https://www.npmjs.com/package/create-music-stream

41. http://doc.gecimi.com/en/latest/#
42. https://cloud.tencent.com/developer/article/1543945
43. https://api.hzhihe.com/QqMusic
44. https://github.com/JooZh/music-api-for-qq √ 【自搭api】
