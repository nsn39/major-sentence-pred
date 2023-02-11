from googletrans import Translator
translator = Translator()

SRC_LANG = "en"
DEST_LANG = "ne"

SRC_FILE = "corpus_english/0.txt"
DEST_FILE = "corpus_nepali/translated.txt"

out_file = open(DEST_FILE, "w")

with open(SRC_FILE, "r") as read_file:
    for line in read_file:
        #print(line)
        # count no of " characters
        origin_line = str()
        if line[-2] != '"': #skip if the text has no quotation marks.
            continue

        if line[-2] == '"':
            separated = line.split('"')
            origin_line = separated[1] 
        elif line[-2] == "." or line[-1] == ".":
            separated = line.split('.')
            origin_line = separated[1][1:] + "."

        print(origin_line)
        translated = translator.translate(origin_line, dest=DEST_LANG, src=SRC_LANG)
        final_line = translated.text + "\n"
        print(final_line)
        out_file.write(final_line)

# close the file object at last.
out_file.close()
