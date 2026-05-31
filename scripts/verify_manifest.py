from pathlib import Path
import csv, hashlib, sys
root = Path(__file__).resolve().parents[1]
manifest = root / 'FILE_MANIFEST.csv'
failures = []
with manifest.open('r', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rel = row['path']
        expected = row['sha256']
        p = root / rel
        if not p.exists():
            failures.append((rel, 'missing'))
            continue
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        if h != expected:
            failures.append((rel, 'sha256 mismatch'))
if failures:
    print('MANIFEST_VERIFY_FAIL')
    for rel, reason in failures:
        print(f'{rel}: {reason}')
    sys.exit(1)
print('MANIFEST_VERIFY_PASS')
