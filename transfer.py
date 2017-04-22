import requests, shutil

def uploadFile(filename):
    with open(filename, 'rb') as f:
        try:
            res = requests.put("https://transfer.sh/" + filename, )
            f.close()
            return res.text
        except Exception as e:
            print e
            return ''

def downloadFile(url, filename):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(filename, 'wb') as a:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
