
class something():

    def __init__(self):
        wordlist = []
        def echo(word):
            wordlist.append(word)
            return word
        
        def secret():
            return wordlist

        self.fcn = echo
        self.secret = secret

if __name__ == "__main__":

    ab = something()
    print ab.fcn("Hello")
    print ab.fcn("Hi")

    #ab.wordlist
    print ab.secret()
