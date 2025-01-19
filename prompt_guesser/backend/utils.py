import nltk

useless_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves','you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their','theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too','very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']

ps = nltk.stem.PorterStemmer()

def is_substantial_word(word: str) -> bool:
    if len(word) <= 2 or word.lower() in useless_words:
        return False
    return True


def get_stems(s: str):
    return [ps.stem(word.lower()) for word in s.strip().split() if is_substantial_word(word)]

def gen_styled_string(sentence, guessed_set):
    word_list = sentence.strip().split()
    res = []
    for word in word_list:
        if ps.stem(word.lower()) in guessed_set:
            res.append("<span style=\"color:#90EE90\">" + word + "</span>")
        else:
            res.append(word)
    return " ".join(res)
    
    
def get_points(prompt, prompt_guess):
    words = get_stems(prompt)
    guessed_words = get_stems(prompt_guess)
    
    intersection = set(words).intersection(set(guessed_words))
    
    styled_prompt = gen_styled_string(prompt, intersection)
    styled_prompt_guess = gen_styled_string(prompt_guess, intersection)
    
    return len(intersection) * 100, styled_prompt, styled_prompt_guess 
