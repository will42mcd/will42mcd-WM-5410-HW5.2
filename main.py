import re
import string


def process_file(fname,enc):
    with open(fname, 'r', encoding=enc) as file:
        dat = file.read()
        dat = perform_re(dat)
    return dat.split()
#end function

def perform_re(text):
    text = re.sub(r'(CHAPTER) ([IVXLC]+.)', '\\1\\2', text)
    return text

def main():
    lcs_data = process_file("LCS.txt", "UTF-8")
    edit_dist_data = process_file("edit_dist.txt", "UTF-8")
    pool = [lcs_data, edit_dist_data]
    word2 = process_file("edit_dist_changes.txt", "UTF-8")
    word1 = process_file("LCS_changes.txt", "UTF-8")
    words = [word1, word2]
    count = 0
    for i in pool:
        for j in words:
            if i == j:
                count = count + 1
            else:
                pass
    print(count/len(words))

    if count > .75:
        print("Code has been taken from the internet.")
    else:
        print("Code is original ")



if __name__ == "__main__":
    main()