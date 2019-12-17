for i in *.wav; do ffmpeg -i "$i" -y -ar 22050 -ac 1 "../output_refact_audio/$i" -acodec pcm_s16le -f s16le;  done
