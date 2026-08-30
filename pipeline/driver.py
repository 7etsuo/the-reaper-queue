import json, time, urllib.request, urllib.error, uuid, sys

HOST = "http://127.0.0.1:8188"
CID = str(uuid.uuid4())

def post(graph):
    body = json.dumps({"prompt": graph, "client_id": CID}).encode()
    req = urllib.request.Request(HOST + "/prompt", body, {"Content-Type": "application/json"})
    try:
        return json.load(urllib.request.urlopen(req, timeout=60))["prompt_id"]
    except urllib.error.HTTPError as e:
        print("SUBMIT ERROR:", e.read().decode()[:3000]); raise

def wait(pid, timeout=5400, label=""):
    t0 = time.time()
    last = -1
    while time.time() - t0 < timeout:
        try:
            h = json.load(urllib.request.urlopen(f"{HOST}/history/{pid}", timeout=30))
        except Exception:
            time.sleep(3); continue
        if pid in h:
            st = h[pid].get("status", {})
            if st.get("status_str") == "error" or not st.get("completed", False):
                for m in st.get("messages", []):
                    if m[0] in ("execution_error", "execution_interrupted"):
                        print("EXEC ERROR:", json.dumps(m[1])[:2500]); return None
            outs = []
            for nid, o in h[pid].get("outputs", {}).items():
                for key in ("images", "gifs", "videos"):
                    for im in o.get(key, []):
                        outs.append(im)
            el = int(time.time() - t0)
            print(f"  done {label} in {el}s -> {[o.get('filename') for o in outs]}", flush=True)
            return outs
        el = int(time.time() - t0)
        if el // 30 != last // 30:
            print(f"  ...{label} {el}s", flush=True); last = el
        time.sleep(3)
    print("TIMEOUT", label); return None

def run(graph, label=""):
    pid = post(graph)
    print(f"queued {label} ({pid})", flush=True)
    return wait(pid, label=label)
