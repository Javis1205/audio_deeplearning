import pysrt
from pydub import AudioSegment

audio_name = 'vachtuongcu.mp3'
sub_name = 'vachtuongcu.srt'
audio_outdir = 'output'
csv_output = 'output.csv'

song = AudioSegment.from_file(audio_name)
subs = pysrt.open(sub_name, encoding='utf-8')

# Define lambda function convert time to miliseconds
time_to_ms = lambda x: (x.hours*3600 + x.minutes * 60 + x.seconds) * 1000 + x.milliseconds

# Extract data
with open(csv_output, 'w') as fd:
    for sub in subs:
        # Get start time, end time in miliseconds
        start_ms = time_to_ms(sub.start)
        end_ms = time_to_ms(sub.end)
        # Audio extracted file name
        audio_extract_name = '{}/{}_{}_{}.wav'.format(audio_outdir, audio_name, start_ms, end_ms)
        text = str(sub.text.encode('utf-8'))
        # Extract file
        extract = song[start_ms:end_ms]
        # Saving
        extract.export(audio_extract_name, format="wav")
        # Write to csv file
        fd.write('{}|{}\n'.format(audio_extract_name, text))
