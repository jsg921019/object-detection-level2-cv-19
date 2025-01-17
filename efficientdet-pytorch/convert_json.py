import json
import argparse
import os


parser = argparse.ArgumentParser(description='Convert json to eff style (class label starts at 1)')
parser.add_argument('--json_path', type=str, default='', help='json path')
args = parser.parse_args()

with open(args.json_path, 'r') as f:
    annos = json.load(f)

for anno in annos['annotations']:
    anno['category_id'] += 1

for anno in annos['categories']:
    anno['id'] += 1

with open(os.path.join(os.path.dirname(args.json_path), 'eff_' + os.path.basename(args.json_path)), 'w') as f:
    json.dump(annos, f)