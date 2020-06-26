# -*- coding: utf-8 -*-
# Copyright (C) 2020 Reactive Markets Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Summary
-------
feed ack data structures.
"""

import reactive.papi.FeedRequestReject as FbsFrr


class FeedRequestReject:

    def __init__(self, req_id: str, error_code: int, error_message: str):
        self.req_id = req_id
        self.error_code = error_code
        self.error_message = error_message

    @classmethod
    def load_from_fbs(cls, reject: FbsFrr.FeedRequestReject):
        return cls(req_id=reject.ReqId(), error_code=reject.ErrorCode(),
                   error_message=reject.ErrorMessage())
