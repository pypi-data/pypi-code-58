
# This file was generated by 'versioneer.py' (0.18) from
# revision-control system data, or from the parent directory name of an
# unpacked source archive. Distribution tarballs contain a pre-generated copy
# of this file.

import json

version_json = '''
{
 "branch": "1.2.0)",
 "date": "2020-06-26T12:32:54+0100",
 "dirty": false,
 "error": null,
 "full-revisionid": "87487b4c14ac489014e6f9c814842286fd9e9fff",
 "repository": "https://github.com/metawards/MetaWards",
 "version": "1.2.0"
}
'''  # END VERSION_JSON


def get_versions():
    return json.loads(version_json)
