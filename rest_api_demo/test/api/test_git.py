import unittest
import os
import shutil
from api.Git import Git


class TestGit(unittest.TestCase):

    def test_clone(self):
        g = Git("test")
        path = g.get_repo_dir()
        try:
            shutil.rmtree(path)
        except PermissionError:
            for root, dirs, files in os.walk(path):
                for f in dirs+files:
                    os.chmod(os.path.join(root, f), 0o777)
            shutil.rmtree(path)
        except FileNotFoundError:
            pass

        self.assertEqual(os.path.exists(path), False)
        g.clone()
        self.assertEqual(os.path.exists(path), True)

if __name__ == '__main__':
    unittest.main()