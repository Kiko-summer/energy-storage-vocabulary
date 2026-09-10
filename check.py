"""Run with python3 check.py; validates snapshot structure, not technical truth."""
import json
import re
from pathlib import Path
from urllib.parse import urlparse

root = Path(__file__).resolve().parent
vocab = (root / 'vocabulary.md').read_text()
entries = [json.loads(s) for s in re.findall(r'```json\n(.*?)\n```', vocab, re.S)]
index = (root / 'terms-index.md').read_text()
ids = [e['id'] for e in entries]
assert entries and len(ids) == len(set(ids)), 'Missing or duplicate entries'
links = re.findall(r'vocabulary\.md#([a-z0-9-]+)', index)
assert sorted(links) == sorted(ids), 'Index does not match snapshot'
assert len({e['sitePath'] for e in entries}) == len(entries), 'Duplicate routes'
for e in entries:
    c, r = e['content'], e['reviewRecord']
    assert e['id'] == c['id'] == r['termId']
    assert c['contentVersion'] == r['contentVersion']
    assert c['publicationStatus'] == 'published' and r['status'] == 'reviewed'
    assert all(r[k] for k in ('contentReviewed', 'boundaryReviewed', 'sourcesReviewed'))
    assert c['definition'] and c['sources'] and e['sceneLabel']
    assert f'<a id="{e["id"]}"></a>' in vocab
    assert e['sitePath'].startswith('/terms/') and e['sitePath'].endswith('/')
    for source in c['sources']:
        url = urlparse(source['href'])
        assert url.scheme == 'https' and url.netloc and source['title']
    for related in c.get('relatedTerms', []):
        if 'href' in related:
            assert related['href'] in {x['sitePath'] for x in entries}, related['href']
for name in ('SKILL.md', 'terms-index.md', 'acceptance.md'):
    for target in re.findall(r'\]\(([^)]+)\)', (root / name).read_text()):
        if '://' not in target:
            assert (root / target.split('#')[0]).is_file(), target
print(f'PASS: {len(entries)} entries; index, IDs, review versions, routes, sources and local links consistent.')
