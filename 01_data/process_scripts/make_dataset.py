import os 
import pandas as pd 

wav_dir = "/Users/calzada/birdsongs/wood/01_data/"
dirs = ['laugh_wavs', 'drum_wavs', 'pik_wavs']
data = []

# assign each directory a value for 'class_ID'
dir_mapping = {
    'laugh_wavs' : 1,
    'drum_wavs': 2, 
    'pik_wavs': 3
}

# loop through the files, obtain x (filepath) and y (class_ID) and add to dataset 
for dir in dirs:
    wav_source_dir = os.path.join(wav_dir, dir)
    print(f"Processing directory: {wav_source_dir}")
    #print(wav_source_dir)
    for wav_file in os.listdir(wav_source_dir):
        wav_file_path = os.path.join(wav_source_dir, wav_file)
        data.append({'wav_filepath': wav_file_path, 'class_ID': dir_mapping[dir]})

df = pd.DataFrame(data)
print(df.head(200))   






