import sys
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    # main arguments
    parser.add_argument("--model", default='gpt', type=str,
                       help="Model type: either 'gpt' or 't5'"
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
    parser.add_argument("--message", default=None, type=str,
                        help="Message for paraphrase"
                        )
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    
    args = parse_args()
    
    model = args.model
    print(model)
    
    top_p = args.top_p
    print(top_p)
    
    i = args.message
    print(i)