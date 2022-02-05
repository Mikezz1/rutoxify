# ruToxify - generating offensive comments with transformers
This repo contains scripts to run and train style-transfer models tuned on russian parallel corpora of toxic comments from [Detoxification challenge](https://github.com/skoltech-nlp/russe_detox_2022) and two collecions of toxic messages from Kaggle ([first](https://www.kaggle.com/alexandersemiletov/toxic-russian-comments/code), [second](https://www.kaggle.com/blackmoon/russian-language-toxic-comments)). The main  purpose of these models was to generate more diverse training examples of obscene & offensive comments for Detoxification challenge. Currently there are two models under the hood: T5base and GPT3small from Sberdevices. Both trained with small leaning rate for 4-5 epochs.
## Examples
> Приветик >>>  Приветик, чувак! Ты меня задолбал((
 
> Это плохая идея >>> это уёбищная идея 
## Usage
- First, download  models by running `load_models.sh` in bash. Then you can try out models by running run.py script and entering message to paraphrase. Feel free to change `model` (default one  is gpt2) and tune generation method by specifying parameters `top-p`, `top-k` ans `temp`as follows:
 ```
python3 run.py --model t5 --top-p 91 --top-k 5 --temp 50  --text "Тест"
>>> Тесты, блять:(
 ```
- You can pass message directly by `--text` argument or in the console if `--text` is not specified
 ```
python3 run.py
>>> Всем привет!
>>> Всем привет! :(
 ```
- For more info on arguments call `--help`
- If you wish to use these models, you can download weights [here](https://www.dropbox.com/sh/5ulccmqwoillf2j/AAALO_OSiutTNmii7T0qBTXRa?dl=0) and [here](https://www.dropbox.com/sh/chpfa4arm7c727w/AACICvSnKvc7xaE9mWjydtcVa?dl=0) or from this repo. Code for fine-tuning is available in ./train folder. 
