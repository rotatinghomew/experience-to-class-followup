import unittest

from inspect_inputs import read_tables


class SourceRecords(unittest.TestCase):
    def test_shared_course_quotas_and_notices(self):
        tables = read_tables()
        groups = {row['class_group']:row for row in tables['quota']}
        courses = {row['class']:row for row in tables['courses']}
        leads = {row['lead'] for row in tables['cohorts']}
        for row in courses.values():
            self.assertIn(row['class_group'],groups)
        for row in tables['commitments']+tables['events']:
            self.assertIn(row['class'],courses)
            self.assertIn(row['lead'],leads)

    def test_outcome_and_opening_corrections_remain_distinct(self):
        tables = read_tables()
        for row in tables['events']:
            self.assertLessEqual(row['happened'],row['received'])
        self.assertTrue({'switched','refused','accepted'} <= {row['kind'] for row in tables['events'] if row['event'].startswith('E-final')})
        self.assertTrue(any(row['state']=='suspended' for row in tables['opening_changes']))
        self.assertTrue(any(row['decision']=='excluded' for row in tables['identity_candidates']))
