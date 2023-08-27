

import json, os, sys


def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html)
        
def open_html(path):
    with open(path, 'rb') as f:
        return f.read()
    
