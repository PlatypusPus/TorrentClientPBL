import bencodepy as ben

def decode_bytes(obj):
    if isinstance(obj, dict):
        return {decode_bytes(k): decode_bytes(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [decode_bytes(i) for i in obj]
    elif isinstance(obj, bytes):
        try:
            return obj.decode('utf-8')
        except UnicodeDecodeError:
            return obj
    else:
        return obj

def read(path):
    with open(path, "rb") as f:
        data = ben.decode(f.read())
    readable_data = decode_bytes(data)
    print(readable_data)

def main():
    torrent_path = r"C:\Users\shovi\Downloads\test.torrent"
    read(torrent_path)

if __name__ == "__main__":
    main()