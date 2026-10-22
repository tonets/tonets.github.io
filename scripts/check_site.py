#!/usr/bin/env python3
"""Check generated pages, local links, images, fragments, and leaked Wiki URLs."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.ids, self.links, self.images, self.duplicates = path, set(), [], [], []
        self.feed(path.read_text(encoding='utf-8'))
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids: self.duplicates.append(a['id'])
            self.ids.add(a['id'])
        if tag == 'a' and a.get('href'): self.links.append(a['href'])
        if tag in ('img', 'script') and a.get('src'): self.images.append(a['src'])
        if tag == 'link' and a.get('rel') == 'stylesheet': self.images.append(a['href'])

root = Path(sys.argv[1] if len(sys.argv)>1 else 'public').resolve()
pages = {p.resolve(): Page(p) for p in root.rglob('*.html')}
home = pages[root/'index.html']
style = next(x for x in home.images if x.endswith('/assets/site.css'))
prefix = urlsplit(style).path.removesuffix('/assets/site.css')
errors=[]; checked=0
for path, page in pages.items():
    for duplicate in page.duplicates: errors.append(f'{path.relative_to(root)}: duplicate ID {duplicate}')
    for link in page.links + page.images:
        u=urlsplit(link)
        if u.scheme or u.netloc: continue
        dest=unquote(u.path)
        if dest.startswith('/'):
            if prefix and not dest.startswith(prefix+'/'): errors.append(f'{path}: wrong base path {link}');continue
            dest=dest[len(prefix):].lstrip('/')
            target=root/dest
        else: target=path.parent/dest if dest else path
        if target.is_dir():target=target/'index.html'
        target=target.resolve();checked+=1
        if not target.exists():errors.append(f'{path.relative_to(root)}: missing {link}');continue
        if u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:
            errors.append(f'{path.relative_to(root)}: missing fragment {link}')
    for link in page.links + page.images:
        u=urlsplit(link)
        if u.hostname=='www.bi.cs.titech.ac.jp' and u.path.startswith('/~ohue/'):
            errors.append(f'{path.relative_to(root)}: legacy dependency {link}')
if errors:
    print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(pages)} HTML pages; {checked} local links, assets and fragments; base path {prefix or "/"}')
