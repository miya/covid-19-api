# covid19-jp-api

![Scheduler](https://github.com/miya/covid19-jp-api/workflows/Scheduler/badge.svg)

## なんこれ
コロナウイルスによる都道府県別の感染者数と死亡者数を公開している[API](https://github.com/ryo-ma/covid19-japan-web-api)をGithubActionsで定期的に叩き、このリポジトリのgh-pagesブランチにjsonファイルをプッシュすることで自分のGithubPagesに擬似的にAPIを作っています。

## なぜつくった
[covid19-jp-linebot](https://github.com/miya/covid19-jp-linebot)という日本国内のコロナウイルスによる感染者数と死亡者数を返すlinebotを開発しています。linebotは不特定多数のユーザーに使われることが想定されるので、メッセージが送られるたびにAPIを叩いてしまうとサーバーの運営者に多大な負担がかかってしまいます。そのため、決められた時間にだけAPIを叩き自分のGithubPagesにプッシュし、linebotにはその擬似APIを叩かせることで負担を軽減することができると考えたので作りました。

## 参考
* [covid19hokkaido_scraping](https://github.com/Kanahiro/covid19hokkaido_scraping)  
* [GitHub Actionsを活用して擬似APIサーバーを用意する](https://qiita.com/Kanahiro/items/e7021b05199ae52e818b)

## 擬似API
* [raw](https://raw.githubusercontent.com/miya/covid19-jp-api/gh-pages/prefectures.json)  
* [GithubPages](https://miya.github.io/covid19-jp-api/prefectures.json)
