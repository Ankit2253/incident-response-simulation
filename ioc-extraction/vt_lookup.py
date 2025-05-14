import argparse, requests

def lookup(hash, api_key):
    url = f"https://www.virustotal.com/api/v3/files/{hash}"
    headers = {"x-apikey": api_key}
    r = requests.get(url, headers=headers)
    print(r.json())

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--hash', required=True)
    p.add_argument('--apikey', required=True)
    args = p.parse_args()
    lookup(args.hash, args.apikey)
