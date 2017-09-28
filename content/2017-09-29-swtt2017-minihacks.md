Title: Salesforce World Tour Tokyo 2017 ミニハック解答速報
Date: 2017-09-29 10:00
Slug: 2017-09-29-swtt2017-minihacks
Author: zaki-yama
Category: Event

昨年もやりましたが、今年も全問解いてみたので簡単な内容ふりかえりを。
問題はこちら。

<blockquote class="embedly-card" data-card-controls="0"><h4><a href="https://developer.salesforce.com/ja/worldtour2017/minihacks">worldtour2017/minihacks</a></h4><p>Trailblazer Zone MiniHacks - Salesforce World Tour Tokyo 2017</p></blockquote>
<script async src="//cdn.embedly.com/widgets/platform.js" charset="UTF-8"></script>

おそらく [10/25 の Meetup](https://www.meetup.com/ja-JP/Tokyo-Salesforce-Developer-Group/events/243315371/) でまた解説がてらお話することになりそうなので
ここではかなり端折って書いてます。

また、例によってデプロイして動かせるようにメタデータを GitHub に置いておきます。
https://github.com/zaki-yama/swtt2017-minihacks

### 課題1 – ポイント & クリックでアプリを作成する

毎年必ず出題されるポイント＆クリック系の正統派な問題です。
文章から要件を把握するのが難しく、1問目がこれだと2問目以降見る気力を失ってしまった方も多そう。
（2 問目以降はちょいちょい簡単なの混じってた）

> Price（料金）はShow（ショー）オブジェクトから取得します。また、Total Cost（総額）は自動で計算されるようにしてください。

や

> ショーやアトラクションには、それぞれ席数（合計席数）の制限があります。（...中略...）満席になったら、それ以上の予約はできません。

などから、Show と Ticket を主従関係で結んであげればいいことがわかれば後は入力規則・積み上げ集計・承認プロセスを駆使して要件を満たすように作り込むだけです。

なお入力規則については、「あらかじめショー側で指定された座席数をオーバーする場合はチケットを作成できない」というだけであれば

```zsh
ShowId__r.TotalSeats__c - ShowId__r.BookedSeats__c < NumberOfTotalSeats__c
```

* `NumberOfTotalSeats__c: チケットオブジェクトの総座席数（大人用席数＋小人用席数 の数式項目）`
* `ShowId__r.TotalSeats__c: ショーオブジェクトの座席数（手入力）`
* `ShowId__r.BookedSeats__c: ショーオブジェクトの予約済み席数（NumberOfTotalSeats__c の積み上げ集計）`

で済みそうですが、これだとチケット更新時に保存できなくなっちゃうんですよね。
なのでここまでやる必要があるかわからない＆合ってるか怪しいですが、私はこうしました。

```
IF(ISNEW(),
  ShowId__r.TotalSeats__c - ShowId__r.BookedSeats__c < NumberOfTotalSeats__c,
  ShowId__r.TotalSeats__c - ShowId__r.BookedSeats__c + PRIORVALUE(NumberOfTotalSeats__c) < NumberOfTotalSeats__c
)
```

`ISNEW()` で作成時かどうか、 `PRIORVALUE()` で更新前の値が取得できるんですねー知らなかった。
なおドキュメントに記載は見つかりませんでしたが、 `PRIORVALUE()` は作成時には 0 (null) ではなく保存しようとしている値がそのまま入ってるようだったので、IF 文での分岐が必要でした。

<br />
### 課題 2 – LightningアプリケーションビルダーとDreamhouse

Dreamhouse アプリをインストールして指示通りにコンポーネントを配置するだけだったので、おそらく一番簡単だったのではないでしょうか。
パス設定なんて項目ができてたんですね。

![path-settings]({filename}/images/2017-09-29-swtt2017-minihacks/path-settings.png)

（ドキュメント：https://help.salesforce.com/articleView?id=rss_sales_path.htm&type=0 ）

この Trailhead モジュールやるといいんじゃないかな。
[パスおよびワークスペース | Salesforce Trailhead](https://trailhead.salesforce.com/ja/modules/sales_admin_optimize_salesforce_for_selling)

<br />
### 課題3 – アンケート投票機能（コーディング使用不可）

フロー機能を使ったお題です。フロー、初めて触りました。
Contestant と Vote を主従関係でむすんだ後、 Vote のレコードを作成するフローコンポーネントを作る必要があるんですが
調べた限りフローは主従関係項目に対応していないっぽかったので、そのあたり皆さんどう解決したのか気になります。

私は Spring'17 から
[Lightning ページへのフローの埋め込み (ベータ)](https://releasenotes.docs.salesforce.com/ja-jp/spring17/release-notes/rn_forcecom_flow_lab.htm)
という機能で LEX 内にフローコンポーネントを埋め込むとレコード ID が取れるようになったというのを見つけ、これで解決しました。

（ただどうやったらレコード ID を渡せるようになるのかがいまいちわかりづらかったので、そのあたりは Meetup でお話できれば）

> Lightningエクスペリエンス内のタブからフローコンポーネントを利用して実行し

という要件を満たしてない気がして自信なかったんですが、このあたりは設問の表現も微妙なラインだったので判定基準としては特になく、OK とのことでした。

<br />
### 課題4 – Lightningを使ったBMI計算ツール

コード書く必要ありますが、これも比較的簡単。
`<ui:outputText>` に替わる基本コンポーネントってないんですね。`<lightning:input disabled="true">` でむりやり解決。

<br />
### 課題5 – Lightning データサービス（Apex使用不可）

こいつも厄介でした。 [Lightning コンポーネント開発者ガイドへのリンク](https://developer.salesforce.com/docs/atlas.ja-jp.208.0.lightning.meta/lightning/data_service.htm) を貼ってくれてますが、
日本語の記事は情報が古くサンプルが動かないんですね。。。

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">ミニハックに精を出されている皆様、Lightningデータサービスは日本語ドキュメントの情報が間違ってるので英語版読むか一度Trailheadやるのオススメです <a href="https://t.co/duSfqqSlk0">https://t.co/duSfqqSlk0</a> <a href="https://twitter.com/hashtag/sfdg?src=hash&amp;ref_src=twsrc%5Etfw">#sfdg</a></p>&mdash; Shingo Yamazaki (@zaki___yama) <a href="https://twitter.com/zaki___yama/status/912180132391010304?ref_src=twsrc%5Etfw">2017年9月25日</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

この Trailhead モジュールは日本語化されてるけど最新の情報になってるっぽいので、これやってから戻ってくるとすんなりいきました。

<br />
### 課題6 – Heroku Connectを使ってみる

去年と全く同じ課題（解いてから気づいた）。

Python の 2 系 3 系問題でハマる人がいたらしく。
「※ Heroku でApplicationが動作しない場合は...」は慌てて追記された文章なのかと推察されますが、そこにも誤りがあったり。（ `runtime.txt` に書くのは `python-2.7.13` が正しい）
Python, Heroku やったことないという人は意味不明なエラーが出て早々にさじを投げた可能性大。

それから Heroku Connect、毎回やる度 GUI で設定するの面倒だなーと思ってましたが、ちゃんと JSON 形式の設定ファイルとしてインポート／エクスポートできるよう CLI が提供されてるんですね。
https://github.com/heroku/heroku-connect-plugin

<br />
### 課題7 – Einstein Visionを利用した検索

Einstein！と身構えてしまいますが、これも手順通りに設定するだけでクリアできる系。
最後 Bot の入力方法だけ注意が必要で、「物件画像検索」と入力したらそのままエンター押さずに画像を添付する必要があったんですね。


<br />
### 課題8 – 検索可能な取引先責任者リスト

これも去年似たようなお題がありましたが、今回は取引先のレコードページに埋め込むタイプでしたね。
`implements="force:hasRecordId"` を設定すると `v.recordId` で現在開いているレコードの ID が取れる、と。


<br />
### おわりに（告知）

というわけで今年のミニハックの内容をざっくりふりかえりました。
冒頭にも書きましたが 10/25(水) の Developer Group の Meetup ではもうちょっと補足＆Tips を交えつつお話する予定です。
ぜひご参加を。

<blockquote class="embedly-card"><h4><a href="https://www.meetup.com/ja-JP/Tokyo-Salesforce-Developer-Group/events/243315371/">Tokyo Salesforce Developer Group</a></h4><p>秋の深まりを感じる季節となるでしょう。（この頃は） ということで、Winter '18 リリースに向けてMeetupを開催したいと思います。 リリースノートの中からDev向けにフォーカスして、内容を共有していきます。 また、LT（8min程度...の予定）を募集します！Salesforce, Herokuに関するネタならなんでもOKですので、ちょこっと話してみたいという方、ぜひどうぞ！（yonei</p></blockquote>

Dev な人じゃなくても大丈夫です！怖くない！
