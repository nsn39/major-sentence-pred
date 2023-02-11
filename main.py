# Write some prompt formats
format_1 = "come up with 50 sentences that any normal person will use in real life related to {}"

# call the chat-GPT client to get the text
from pyChatGPT import ChatGPT
from session_token import TOKEN

file_list = [
    "keywords.txt",
#    "keywords2.txt",
#    "keywords3.txt",
#    "keywords4.txt",
#    "keywords5.txt"
]

api = ChatGPT(TOKEN)

for i, file in enumerate(file_list):
    new_file = "corpus_english/" + str(i) + ".txt"
    out_file = open(new_file, 'a')
    output_str = str()
    with open(file, "r") as file:
        for line in file:
            keyword = line
            prompt = format_1.format(keyword)
            response = api.send_message(prompt)
            output_str = response['message'] + "\n"
            print("output: " + output_str)
            out_file.write(output_str)
    out_file.close()
    

resp = api.send_message('Hello, world!')
# save the text to the corpus_folder.

if __name__=="__main__":
    print("creating dataset...")