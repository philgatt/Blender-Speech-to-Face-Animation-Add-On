import json
import wave
from vosk import Model, KaldiRecognizer
import eng_to_ipa as p


class Word:
    ''' A class representing a word from the JSON format for vosk speech recognition API '''

    def __init__(self, dict):
        '''
        Parameters:
          dict (dict) dictionary from JSON, containing:
            conf (float): degree of confidence, from 0 to 1
            end (float): end time of the pronouncing the word, in seconds
            start (float): start time of the pronouncing the word, in seconds
            word (str): recognized word
        '''

        self.conf = dict["conf"]
        self.end = dict["end"]
        self.start = dict["start"]
        self.word = dict["word"]

    def to_string(self):
        ''' Returns a string describing this instance '''
        return "{:20} from {:.2f} sec to {:.2f} sec, confidence is {:.2f}%".format(
            self.word, self.start, self.end, self.conf * 100)

def transcribeFile(audioFile, model):
    wf = wave.open(audioFile, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print("Audio file must be WAV format mono PCM.")
        exit(1)

    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    # get the list of JSON dictionaries
    results = []
    # recognize speech using vosk model
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            part_result = json.loads(rec.Result())
            results.append(part_result)
            print(part_result)
    part_result = json.loads(rec.FinalResult())
    results.append(part_result)

    # convert list of JSON dictionaries to list of 'Word' objects
    list_of_Words = []
    for sentence in results:
        if len(sentence) == 1:
            # sometimes there are bugs in recognition
            # and it returns an empty dictionary
            # {'text': ''}
            continue
        for obj in sentence['result']:
            w = Word(obj)  # create custom Word object
            list_of_Words.append(w)  # and add it to list
        # Extracting the words from the dictionary
        words = [i['word'] for i in sentence['result']]
        print("Words in the dictionary:", words)

        # Prompt the user to enter a list of new words
        new_words = input("Enter new words separated by spaces: ").split()

        # Check if the number of new words is equal to the number of words in the dictionary
        if len(new_words) != len(words):
            print("Error: The number of new words does not match the number of words in the dictionary")
        else:
            # Updating the words in the dictionary
            for i in range(len(words)):
                sentence['result'][i]['word'] = new_words[i]

#        print("Original dictionary:")
#        print(sentence)

#        modified_dict_str = input("Enter modified dictionary as a string: ")

#        # convert modified dictionary string to dictionary object
#        modified_dict = eval(modified_dict_str)

#        # update original dictionary with modified dictionary
#        sentence.update(modified_dict)

#        # print updated dictionary
#        print("Updated dictionary:")
#        print(sentence)
        
    wf.close()  # close audiofile
    return list_of_Words


def ConvertEnglishToIpa(list_of_Words):
    for i in range(len(list_of_Words)):
        ipaWord = p.convert(list_of_Words[i].word)
        list_of_Words[i].word = ipaWord
