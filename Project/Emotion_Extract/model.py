import numpy as np
import csv
import torch
import torch.nn as nn
import torch.nn.functional as F
import os


path = os.getcwd()


class NN(nn.Module):
    def __init__(self, embedding, embedding_dim, hidden_dim, vocab_size, output_dim, batch_size):
        super(NN, self).__init__()

        self.batch_size = batch_size

        self.hidden_dim = hidden_dim

        self.word_embeddings = embedding

        # The LSTM takes word embeddings as inputs, and outputs hidden states
        # with dimensionality hidden_dim.
        self.lstm = nn.LSTM(embedding_dim,
                            hidden_dim,
                            num_layers=2,
                            dropout=0.5,
                            batch_first=True)

        # The linear layer that maps from hidden state space to output space
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, sentence):
        # sentence = sentence.type(torch.LongTensor)
        # print ('Shape of sentence is:', sentence.shape)

        sentence = sentence.to(device)

        embeds = self.word_embeddings(sentence)
        # print ('Embedding layer output shape', embeds.shape)

        # initializing the hidden state to 0
        # hidden=None

        h0 = torch.zeros(2, sentence.size(0), hidden_dim).requires_grad_().to(device)
        c0 = torch.zeros(2, sentence.size(0), hidden_dim).requires_grad_().to(device)

        lstm_out, h = self.lstm(embeds, (h0, c0))
        # get info from last timestep only
        lstm_out = lstm_out[:, -1, :]
        # print ('LSTM layer output shape', lstm_out.shape)
        # print ('LSTM layer output ', lstm_out)

        # Dropout
        lstm_out = F.dropout(lstm_out, 0.5)

        fc_out = self.fc(lstm_out)
        # print ('FC layer output shape', fc_out.shape)
        # print ('FC layer output ', fc_out)

        out = fc_out
        out = F.softmax(out, dim=1)
        # print ('Output layer output shape', out.shape)
        # print ('Output layer output ', out)
        return out


# model load
model = torch.load(path + '/model.pt')


# HELPER FUNCTIONS

def read_glove_vecs(glove_file):
    with open(glove_file, 'r') as f:
        words = set()
        word_to_vec_map = {}
        for line in f:
            line = line.strip().split()
            curr_word = line[0]
            words.add(curr_word)
            word_to_vec_map[curr_word] = np.array(line[1:], dtype=np.float64)

        i = 1
        words_to_index = {}
        index_to_words = {}
        for w in sorted(words):
            words_to_index[w] = i
            index_to_words[i] = w
            i = i + 1
    return words_to_index, index_to_words, word_to_vec_map


def convert_to_one_hot(Y, C):
    Y = np.eye(C)[Y.reshape(-1)]
    return Y


def read_csv(filename):
    phrase = []
    emoji = []

    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)

        for row in csvReader:
            phrase.append(row[0])
            emoji.append(row[1])

    X = np.asarray(phrase)
    Y = np.asarray(emoji, dtype=int)

    return X, Y


word_to_index, index_to_word, word_to_vec_map = read_glove_vecs(path +'/glove.6B.50d.txt')


def sentences_to_indices(X, word_to_index, max_len):
    """
    Converts an array of sentences (strings) into an array of indices corresponding to words in the sentences.
    """

    m = X.shape[0]  # number of training examples

    # Initialize X_indices as a numpy matrix of zeros and the correct shape
    X_indices = np.zeros((m, max_len))

    for i in range(m):  # loop over training examples

        # Convert the ith sentence in lower case and split into a list of words
        sentence_words = X[i].lower().split()

        # Initialize j to 0
        j = 0

        # Loop over the words of sentence_words
        for w in sentence_words:
            # Set the (i,j)th entry of X_indices to the index of the correct word.
            X_indices[i, j] = word_to_index[w]
            # Increment j to j + 1
            j = j + 1

    return X_indices


X_train, Y_train = read_csv(path +'/train.csv')
X_test, Y_test = read_csv(path +'/test.csv')
maxLen = len(max(X_train, key=len).split())
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
hidden_dim = 128


def predict(input_text, print_sentence=True):
    labels_dict = {
        0: "❤️ Loving",
        1: "⚽️ Playful",
        2: "😄 Happy",
        3: "😞 Annoyed",
        4: "🍽 Foodie",
    }

    # Convert the input to the model
    x_test = np.array([input_text])
    X_test_indices = sentences_to_indices(x_test, word_to_index, maxLen)
    sentences = torch.tensor(X_test_indices).type(torch.LongTensor)

    # Get the class label
    ps = model(sentences)
    top_p, top_class = ps.topk(1, dim=1)
    label = int(top_class[0][0])

    if print_sentence:
        print("\nInput Text: \t" + input_text + '\nEmotion: \t' + labels_dict[label])

    return label


# pip install googletrans

##########################################################################################
# 최종함수
##########################################################################################


import re
from google_trans_new import google_translator


def translator_function(text):
    translator = google_translator()
    translate_text = translator.translate(text, lang_tgt='en')
    return translate_text


def cleanText(readData):
    # 텍스트에 포함되어 있는 특수 문자 제거
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', readData)

    return text


def split_sentences(text):
    text = cleanText(text)
    temp = text.split(' ')
    sentence = []
    sentences = []

    while len(temp) != 0:
        while len(sentence) != 10:
            if len(temp) == 0:
                break
            sentence.append(temp.pop(0))

        sentences.append(' '.join(sentence))
        sentence = []

    return sentences


def multi_predict(sentences):
    results = []
    for i in sentences:
#         try:
        results.append(predict(i))
#         except Exception as e:
#             pass
    return results


# 최종 예측형태
text = input('입력하세요')


print(multi_predict(split_sentences(cleanText(translator_function(text)))))

