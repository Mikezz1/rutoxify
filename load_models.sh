mkdir models/gpt
mkdir models/t5
wget -q https://www.dropbox.com/sh/5ulccmqwoillf2j/AAALO_OSiutTNmii7T0qBTXRa?dl=0 --content-disposition
unzip t5_model.zip -d models/t5
wget -q https://www.dropbox.com/sh/chpfa4arm7c727w/AACICvSnKvc7xaE9mWjydtcVa?dl=0 --content-disposition
unzip gpt_model.zip -d models/gpt
mv models/gpt/gpt_tokenizer /tokenizers/
mv models/t5/t5_tokenizer /tokenizers
