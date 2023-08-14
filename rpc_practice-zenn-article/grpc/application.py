from google.protobuf import json_format
from typing import List
from collections.abc import Iterable
import json


# 「grpc」パッケージと、grpc_tools.protocによって生成したパッケージをimportする
import user_pb2
import user_pb2_grpc


# ユーザー情報の読み込み
USER_DB = "./json_data/users.json"
with open(USER_DB, mode="r") as fp:
    users = json.load(fp)


class UserManager(user_pb2_grpc.UserManagerServicer):
    """
    サービス定義から生成されたクラスを継承して、
    定義したリモートプロシージャに対応するメソッドを実装する。
    クライアントが引数として与えたメッセージに対応するオブジェクト
    context引数にはRPCに関する情報を含むオブジェクトが渡される
    """

    # この下にメソッドを実装していく
