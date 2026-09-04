from urllib.parse import urlsplit, urlunsplit

def normalize(url:str)->str:
    raw=url.strip()
    if "://" not in raw: raw="https://"+raw
    p=urlsplit(raw)
    if p.scheme not in {"http","https"} or not p.netloc: raise ValueError("invalid HTTP URL")
    return urlunsplit((p.scheme.lower(),p.netloc,p.path or "/",p.query,p.fragment))
