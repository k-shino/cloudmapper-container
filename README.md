# cloudmapper-docker

## TL;DR

* [duo-labs/cloudmapper](https://github.com/duo-labs/cloudmapper)のdocker版

## Setup

* 下記環境変数を設定する. (設定しない場合は[]に記載の名前となる)
  * `AWS_NAME` : 可視化するAWSアカウントを識別するための任意の名前を設定する．[demo]
  * `AWS_ID` : AWSアカウントのIDを設定する．アカウントIDがわからない場合は[こちら](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html)を参照．[123456789012]
  * `AWS_ACCESS_KEY` : AWSアカウントのリソース情報取得のためのAWSアクセスキーを設定．必要な権限は[こちら](https://github.com/duo-labs/cloudmapper#aws-privileges-required)を参照．[AAAAA]
  * `AWS_SECRET_KEY` : 上述のAWSアクセスキーに紐づくAWSシークレットキーを設定．[AAAAA]

  設定例：
  ```bash
  export AWS_NAME=prod
  export AWS_ID=123
  export AWS_ACCESS_KEY=BBBBB
  export AWS_SECRET_KEY=CCCCC
  ```
* ビルドを実施
  ```bash
  cd ./docker-compose/
  docker-compose -f docker-compose.yml -p cloudmapper build --pull
  ```
* デプロイを実施
  ```bash
  docker-compose -f docker-compose.yml -p cloudmapper up -d
  ```

  ```bash
  k-shino@alpha:~/cloudmapper-container/docker-compose$ docker-compose -f docker-compose.yml -p cloudmapper up -d
  WARNING: Some services (cloudmapper) use the 'deploy' key, which will be ignored. Compose does not support 'deploy' configuration - use `docker stack deploy` to deploy to a swarm.
  WARNING: The Docker Engine you're using is running in swarm mode.
  
  Compose does not use swarm mode to deploy services to multiple nodes in a swarm. All containers will be scheduled on the current node.
  
  To deploy your application across the swarm, use `docker stack deploy`.
  
  Creating network "cloudmapper_default" with the default driver
  Creating cloudmapper_cloudmapper_1 ... done
  ```

  `WARNING`が出ている場合，環境変数が未設定であったり，AWSアクセスキー，AWSシークレットキーに誤りがある場合がある．

## 使用方法

* デプロイが環境すると，`http://デプロイしたサーバのIPアドレス:8000/` にアクセスすると，cloudmapperのGUIが出力される．
* 24時間に一度，AWSアカウントの状態を取得し，出力結果が更新される．
  * 更新頻度を変更したい場合，`./docker-compose/docker-compose.yml` の `services.cloudmapper.healthcheck.interval`の値を秒数で入力する．
* 画面表示に関する設定変更したい場合，デプロイ後に以下のように入力する．
  ```bash
  docker-compose -f docker-compose.yml -p cloudmapper exec cloudmapper redraw --vpc-names test --regions ap-northeast-1 --internal-edges
  ```
  * 引数のオプションは `docker-compose exec cloudmapper redraw -h` にて確認可能．
  * デフォルトでは，`--no-internal-edges` のみ指定している．
* AWSアカウントのリソース情報を手動で更新したい場合，以下のコマンドを実行する．
  ```bash
  docker-compose -f docker-compose.yml -p cloudmapper exec cloudmapper recollect
  ```
* cloudmapperの画面上で，CIDRを文字列変換し表示させたい場合，以下のコマンドで変換可能．(詳細は[こちら](https://github.com/duo-labs/cloudmapper#option-2-generate-config-file)を参照)
  ```bash
  docker-compose -f docker-compose.yml -p cloudmapper exec cloudmapper cidr [add|remove] CIDR 表示させたい名称
  ```

  例：
  ```bash
  docker-compose -f docker-compose.yml -p cloudmapper exec cloudmapper cidr add 1.1.1.1/32 hoge
  docker-compose -f docker-compose.yml -p cloudmapper exec cloudmapper cidr remove 1.1.1.1/32
  ```

## 停止方法
```bash
docker-compose -f ./docker-compose.yml -p cloudmapper stop
```
