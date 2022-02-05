#! pip install -qq transformers
import sys
import argparse
from transformers import (AutoModelWithLMHead,
                          T5ForConditionalGeneration,
                          AutoTokenizer,
                          pipeline)

def parse_args():
    parser = argparse.ArgumentParser()
    # main arguments
    parser.add_argument("--model", default='gpt', type=str,
                       help="Model type: either 'gpt' or 't5'"
                       )
    parser.add_argument("--device", default=0, type=int,
                       help="0 for cuda, -1 for cpu"
                       )
    parser.add_argument("--top_p",  default=95, type=int,
                        help="Top-p parameter for generation"
                       )
    parser.add_argument("--top_k", default=3, type=int,
                       help="Top-k parameter for generation"
                       )
    parser.add_argument("--temp", default=50, type=int,
                        help="Temperature parameter for generation"
                       )
    parser.add_argument("--max_len", default=100, type=int,
                        help="Max len of generated text (in tokens)"
                       )
    parser.add_argument("--gpt_model_path", default='./models/gpt/', type=str,
                        help="Path to pre-trained model"
                       )
    parser.add_argument("--t5_model_path", default='./models/t5/', type=str,
                        help="Path to pre-trained model"
                       )
    parser.add_argument("--gpt_tokenizer_path", default='./tokenizers/gpt/', type=str,
                        help="Path to gpt tokenizer"
                       )
    parser.add_argument("--t5_tokenizer_path", default='./tokenizers/t5', type=str,
                        help="Path to t5 tokenizer"
                        )
    parser.add_argument("--text", default=None, type=str,
                        help="Message to paraphrase. Should be inside '' "
                        )
    args = parser.parse_args()
    return args

def process_input(input: str) -> str:
    return f'<s>{input}</s>>>>><p>'


def paraphrase(input: str, pipe) -> str:
    output =  pipe(input)
    return output[0]['generated_text'].split('</s>>>>><p>')[1].split('</p>')[0]

# run the script
if __name__ == "__main__":
    
    args = parse_args()
    
    # init model and tokenizer
    if args.model == 'gpt':
        model = AutoModelWithLMHead.from_pretrained(args.gpt_model_path, max_length = args.max_len)
        tokenizer = AutoTokenizer.from_pretrained(args.gpt_tokenizer_path)
    elif args.model == 't5':
        model = T5ForConditionalGeneration.from_pretrained(args.t5_model_path, max_length = args.max_len)
        tokenizer = AutoTokenizer.from_pretrained(args.t5_rokenizer_path)
        
    # init generation pipeline
    pipe = pipeline('text-generation',
                     model=model,
                     tokenizer=tokenizer,
                     framework='pt',
                     top_k = args.top_k,
                     top_p=args.top_p,
                     temperature=args.temperature,
                     batch_size=1)

    # get predictions
    print("Enter message:")
    
    input = args.text or str(input())
    if args.model == 'gpt':
        output = paraphrase(process_input(input), pipe) # gpt2 requires additional symbols for generation
    else:
        output = pipe(input)
    print(f"Paraphrase: {output}")
