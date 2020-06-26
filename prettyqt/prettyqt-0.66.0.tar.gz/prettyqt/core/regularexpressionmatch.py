# -*- coding: utf-8 -*-
"""
@author: Philipp Temminghoff
"""

from qtpy import QtCore


class RegularExpressionMatch(QtCore.QRegularExpressionMatch):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.string = None
        self.pos = None
        self.endpos = None

    def __repr__(self):
        return "RegularExpressionMatch()"

    def __getitem__(self, item):
        return self.group(item)

    def group(self, *groups):
        if len(groups) > 1:
            return tuple(self.captured(i) for i in groups)
        if len(groups) == 0:
            return self.captured(0)
        return self.captured(groups[0])

    def groups(self, default=None) -> tuple:
        if self.lastindex is None:
            return tuple()
        return (self.group(i) if i <= self.lastindex else default
                for i in range(self.re.captureCount()))

    def groupdict(self, default=None) -> dict:
        groups = [self.group(i) if i <= self.lastindex else default
                  for i in range(self.re.captureCount())]
        names = self.re.namedCaptureGroups()
        return {names[i]: groups[i] for i in range(self.re.captureCount())}

    def start(self, group: int = 0):
        return self.capturedStart(group)

    def end(self, group: int = 0):
        return self.capturedEnd(group)

    def span(self, group: int = 0) -> tuple:
        return (self.start(group), self.end(group))

    @property
    def lastindex(self):
        idx = self.lastCapturedIndex()
        return None if idx == -1 else idx

    @property
    def lastgroup(self):
        if self.lastCapturedIndex() == -1:
            return None
        return self.re.namedCaptureGroups()[self.lastCapturedIndex()]

    @property
    def re(self):
        return self.regularExpression()


if __name__ == "__main__":
    reg = RegularExpressionMatch()
