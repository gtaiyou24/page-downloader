# Page Downloader
Webページをダウンロードするシステム

## How to
<details><summary>起動方法</summary>

```bash
docker-compose up --build
```

 - [Page Downloader - Swagger UI](http://0.0.0.0:8000/docs)

</details>

<details><summary>UT実行方法</summary>

```bash
pytest -v ./tests
```

</details>

<details><summary>デプロイ手順</summary>

```bash
sh build_and_push.sh lambda-page-downloader ./app/Dockerfile.aws.lambda
```
</details>