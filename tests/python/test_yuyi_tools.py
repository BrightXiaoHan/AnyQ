import unittest
import time
import sys

# 添加测试文件目录到path
source_folder = "tools/robot_manager"
if source_folder not in sys.path:
    sys.path.append(source_folder)

from solr_yuyi_tools import *

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.robot_id = "test_robot_id"
        self.documents = [
            {"answer": "支持推广账户使用。", "question": "你好",
                "id": "test_unique_id"}
        ]

    def test_upload_delete(self):
        code = upload_documents(self.documents, self.robot_id)
        self.assertEqual(code, 0)
        # time.sleep(5)
        # docs = query_documents("robot_id:%s" % self.robot_id)
        # self.assertGreater(len([d for d in docs if d["robot_id"] == self.robot_id]), 0)
        code = delete_robot(self.robot_id)
        self.assertEqual(code, 0)
        # time.sleep(5)  # 等待10秒
        # docs = query_documents("robot_id*%s" % self.robot_id)
        # self.assertEqual(len([d for d in docs if d["robot_id"] == self.robot_id]), 0)

if __name__ == '__main__':
    unittest.main()
