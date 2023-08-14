## 環境

- python

```bash
% python --version
Python 3.11.4
% pip list
Package       Version
------------- -------
grpcio        1.57.0
grpcio-tools  1.57.0
line-profiler 4.0.3
pip           23.2.1
protobuf      4.24.0
setuptools    65.5.0
```

- gRPC

```bash
pip install grpcio grpcio-tools
```

- line_profiler

```bash
pip install line_profiler
```

## 実行

- response_bytes

```bash
% python server.py
```

```bash
% kernprof -l -v ./client.py
```

- tohoho

```bash
python server.py
```

```bash
python clinet.py
```

## 参考

### tohoho

- [とほほの gRPC 入門](https://www.tohoho-web.com/ex/grpc.html)

### gRPC の 4 つの通信方式を Python でやってみる

- [rpc_practice-zenn-article](https://zenn.dev/kumamoto/articles/0596ed47f33965)

### gRPC

- [Language Guide (proto 3)](https://protobuf.dev/programming-guides/proto3/)

### パフォーマンス計測

- [Python スクリプトのパフォーマンス計測ガイド](https://yakst.com/ja/posts/42)

- [line_profiler で、Python のプログラムを行単位でプロファイリングする](https://kazuhira-r.hatenablog.com/entry/2019/04/13/182005)
