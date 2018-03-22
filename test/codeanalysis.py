#/usr/bin/env python3
import pprint
from prospector.run import Prospector
from prospector.config import ProspectorConfig

from unittest import TestCase

import sys
import os

REPO_BASE_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))

class AnalyseTest(TestCase):
    """Testcase class that does code checking"""

    def test_prospector(self):
        """Run prospector tests"""

        PROSPECTOR_OPTIONS = [
            '--strictness', 'medium',
            '--max-line-length', '120',
            '--absolute-paths',
        ]
        sys.argv = ['fakename']
        sys.argv.extend(PROSPECTOR_OPTIONS)
        sys.argv.append(REPO_BASE_DIR)
        config = ProspectorConfig()
        config.libraries = []
        prospector = Prospector(config)
        prospector.execute()
        failures = [msg.as_dict() for msg in prospector.get_messages()]
        self.assertFalse(failures, "prospector failures: %s" % pprint.pformat(failures))
