import json,re,sys
sys.path.insert(0,'pipeline'); import yandex_entrances as y
html=y.fetch("OctoSkills Береговой проезд 5А",55.755869,37.509988)
out={}
def walk(x):
    if isinstance(x,dict):
        if x.get("title")=="OctoSkills" and "coordinates" in x and "keys" not in out:
            out["keys"]=sorted(x.keys())
            out["timeish"]={k:x[k] for k in x if re.search("hour|work|time|open|status|phone|url|site",k,re.I)}
        for v in x.values(): walk(v)
    elif isinstance(x,list):
        for v in x: walk(v)
for b in re.findall(r'<script[^>]*type="application/json"[^>]*>(.*?)</script>',html,re.S):
    try: walk(json.loads(b))
    except Exception: pass
json.dump(out,open("auto/entrance-probe-out.json","w"),ensure_ascii=False,indent=1)
