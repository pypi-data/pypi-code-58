#!/usr/bin/env python

# Copyright 2016-2020 Biomedical Imaging Group Rotterdam, Departments of
# Medical Informatics and Radiology, Erasmus MC, Rotterdam, The Netherlands
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

from WORC.detectors.detectors import WORCDirectoryDetector
from WORC.addexceptions import WORCValueError
import os


def find_exampledatadir():
    """Find WORC example data folder."""
    # Check if example data directory exists
    base_dir = WORCDirectoryDetector().do_detection()
    if not base_dir:
        raise WORCValueError('WORC installation directory not detected!')
    else:
        return os.path.join(base_dir, 'exampledata')


def find_testdatadir():
    """Find WORC test data folder."""
    # Check if example data directory exists
    base_dir = WORCDirectoryDetector().do_detection()
    if not base_dir:
        raise WORCValueError('WORC installation directory not detected!')
    else:
        testdatadir = os.path.join(base_dir, 'test', 'tmp')
        if not os.path.exists(testdatadir):
            os.mkdir(testdatadir)
        return testdatadir