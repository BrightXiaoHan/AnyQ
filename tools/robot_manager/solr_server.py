import os
import sys
import json
import tornado
import uuid

from tornado.web import RequestHandler

cwd = os.path.abspath(os.path.dirname(__file__))

if cwd not in sys.path:
    sys.path.append(cwd) 

import solr_yuyi_tools as tools
import anyq_tools as anyq


class SolrToolsHandler(RequestHandler):

    def post(self):
        data = json.loads(self.request.body.decode("utf-8"))
        code = self._handle_data(data)
        result_data = {
            "status_code": code
        }
        self.write(json.dumps(result_data, ensure_ascii=False))

    def _handle_data(self, dic):
        """处理字典数据
        
        Args:
            dic (dict): 字典数据，具体类型子类指定
        
        Raises:
            NotImplementedError: 子类必须复写该方法

        Returns:
            int: 状态码
        """
        raise NotImplementedError

class CreateRobotHandler(SolrToolsHandler):
    """数据示例{
        "robot_code": "robot_id"
    }
    """
    def _handle_data(self, dic):
        return 0

class DeleteRobotHandler(SolrToolsHandler):
    """数据示例{
        "robot_code": "robot_id"
    }
    """
    def _handle_data(self, dic):
        
        return tools.delete_robot(dic["robot_code"])
        

class DeleteItemsHandler(SolrToolsHandler):
    """数据示例{
        "q_ids": ["id1", "id2"],
        "robot_code": "robot_id"
    }
    """
    def _handle_data(self, dic):
        return tools.delete_documents(dic["q_ids"])
        

class AddItemsHandler(SolrToolsHandler):
    """数据示例{
        "documents":[{"answer": "支持推广账户使用。", "question": "AI服务支持推广账号使用么？", "id": "3"}],
        "robot_id": "robot_id"
    }
    """
    def _handle_data(self, dic):
        return tools.upload_documents(documents=dic["documents"], robot_id=dic["robot_id"])

class AskHandler(RequestHandler):
    """数据示例{
        "robot_code": "test_robot_id",
        "question": "用户提问的问题"
    }
    """
    def post(self):
        data = json.loads(self.request.body.decode("utf-8"))
        result = anyq.ask(data["question"], data["robot_code"])
        response_json = {
            "answer": "对不起，您问的问题我暂时无法回答，但是我会努力学习的哦。"
        }
        if len(result) > 0:
            response_json["answer"] =  result[0]["answer"]
        self.write(json.dumps(response_json, ensure_ascii=False))


def main():
    # 对服务的配置问题
    settings = {
        'debug': False
    }
    application = tornado.web.Application([
        (r'/robot_manager/single/add_items', AddItemsHandler),
        (r'/robot_manager/single/delete_items', DeleteItemsHandler),
        (r'/robot_manager/single/delete_robot', DeleteRobotHandler),
        (r'/robot_manager/single/create_robot', CreateRobotHandler),
        (r'/robot_manager/single/ask', AskHandler)
    ],**settings)
    http_server = tornado.httpserver.HTTPServer(application)
    # 2. 服务端口
    http_server.listen(8080)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()