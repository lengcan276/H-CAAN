import os
import pickle
import numpy as np
import pandas as pd
import re
import sys
# from scripts.parsers import vocab_parser

def tokenizer(smile):
    "Tokenizes SMILES string"
    pattern =  "(\[[^\]]+]|Br?|Cl?|N|O|S|P|F|I|b|c|n|o|s|p|\(|\)|\.|=|#|-|\+|\\\\|\/|_|:|~|@|\?|>|\*|\$|\%[0-9]{2}|[0-9])"
    regezz = re.compile(pattern)
    tokens = [token for token in regezz.findall(smile)]
    assert smile == ''.join(tokens), ("{} could not be joined".format(smile))
    return tokens

def build_vocab(smiles, vocab_name='char_dict', save_dir=None):
    ### Build vocab dictionary
    print('building dictionary...')
    char_dict = {}
    char_idx = 1
    mol_toks = []
    with open(smiles, 'r') as f:
        for line in f:
            line = line.split('\n')[0]
            if line.lower() in ['smile', 'smiles', 'selfie', 'selfies']:
                pass
            else:
                mol = tokenizer(line)
                for tok in mol:
                    if tok not in char_dict.keys():
                        char_dict[tok] = char_idx
                        char_idx += 1
                    else:
                        pass
                mol.append('<end>')
                mol_toks.append(mol)

    ### Write dictionary to file
    with open(os.path.join(save_dir, vocab_name+'.pkl'), 'wb') as f:
        pickle.dump(char_dict, f)
    return char_dict
    
if __name__ == '__main__':
    filePath = '/home/nudt_cleng/ccleng/MMFDL-main/notebook/0423/origin/results/LipophilicitySmileAll.txt'
    file_name = 'Lipophilicity_smiles_char_dict'
    savePath = '/home/nudt_cleng/ccleng/MMFDL-main/notebook/0423/origin/results/'
    char_dict = build_vocab(filePath, file_name, savePath)

    vocab_path = '/home/nudt_cleng/ccleng/MMFDL-main/notebook/0423/origin/results/Lipophilicity_smiles_char_dict.pkl'
    with open(vocab_path, 'rb') as f:
        smilesVoc = pickle.load(f)
    print(smilesVoc)

