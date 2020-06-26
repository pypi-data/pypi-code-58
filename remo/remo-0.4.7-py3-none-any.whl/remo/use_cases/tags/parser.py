import csv
import os
from typing import List, Dict

from remo_app.remo.stores.tag_store import TagStore


class TagParser:
    header = ['file_name', 'tag']

    def __init__(self, annotation_set_id: int):
        self.annotation_set_id = annotation_set_id

    def can_parse_file(self, path: str) -> bool:
        if not os.path.exists(path):
            return False

        _, extension = os.path.splitext(path)
        if extension != '.csv':
            return False

        with open(path) as fp:
            csv_reader = csv.reader(fp, delimiter=',')
            header = None
            while not header:
                header = next(csv_reader)
            return self.is_valid_header(header)

    def is_valid_header(self, header: List[str]) -> bool:
        return header == self.header

    def parse_tags(self, path: str) -> Dict[str, List[str]]:
        with open(path) as fp:
            csv_reader = csv.reader(fp, delimiter=',')
            header = None
            while not header:
                header = next(csv_reader)

            tags = {}
            for row in csv_reader:
                if len(row) == 0:
                    continue
                file_name, tag = row
                arr = tags.get(file_name, [])
                arr.append(tag)
                tags[file_name] = arr
            return tags

    def parse(self, path: str):
        tags = self.parse_tags(path)
        TagStore.add_tags_to_annotation_set(tags, self.annotation_set_id)
