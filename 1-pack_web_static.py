from fabric import task
from datetime import datetime
from pathlib import Path

def do_pack(c):
    try:
        Path("versions").mkdir(exist_ok=True)
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        ac_name = f"versions/web_static_{now}.tgz"
        c.local(f"tar -czvf {ac_name} web_static")
        return ac_name
    except Exception:
        return None
