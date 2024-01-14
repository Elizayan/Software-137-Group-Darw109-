import requests
import time

def reprocess(text):
    for item in text:
        type_name=item["obj"]
        name=item["mention"]
        value=item["prob"]
        with open(type_name+".txt", 'a') as f:
            f.write(f'{name},\t{value}\n')

def query_plain(text, url="http://bern2.korea.ac.kr/plain"):
    return requests.post(url, json={'text': text}).json()

if __name__ == '__main__':
    cnt=0;
    with open('data.txt', 'r') as file: 
        #1926-15296 no
        #15296-15500 ok
        line = file.readline() 
        while line:
            if cnt<1926:
                cnt+=1
                line = file.readline()
                continue;
            line = file.readline()
            if cnt%100==0:
                print(cnt)
            text = line
            begin=0
            end=len(text)
            while end-begin>=5000:
                try:
                    ans=query_plain(text[begin:begin+4999])["annotations"]
                except:
                    print(f'{cnt},\t{begin}\t{end}:wrong web!')
                begin+=5000
                reprocess(ans)
            try:
                ans=query_plain(text[begin:end])["annotations"]
            except:
                print(f'{cnt},\t{begin}\t{end}:wrong web!')
            reprocess(ans)
            cnt+=1;
            line = file.readline() 