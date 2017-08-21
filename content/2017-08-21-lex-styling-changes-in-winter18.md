Title: Winter'18からLEXのスタイルがちょっとだけ変わります
Date: 2017-08-21 17:00
Slug: 2017-08-21
Author: zaki-yama

最後に更新したのいつだろうと思ったら 4 月でした。
このまま更新頻度が Salesforce のリリース並になってしまうのは避けたいので、
毎週／隔週でのまとめ記事投稿は潔く諦め、記事単体の紹介でも随時投稿していきたいと思います。

今回はこちらの記事について。
Partner Community でも ISV 向け Alert がありました。

<blockquote class="embedly-card"><h4><a href="https://developer.salesforce.com/blogs/developer-relations/2017/08/winter-coming-lightning.html">Get your Lightning components ready for Winter '18 - Developer Relations</a></h4><p>You know what they say - time flies when you're having fun! And we've been having a lot of fun since Lightning Experience launched two short years ago. This blog post covers several enhancements in the Winter '18 release which might affect your components and Visualforce pages.</p></blockquote>
<script async src="//cdn.embedly.com/widgets/platform.js" charset="UTF-8"></script>

以前のような、LEX のメニューがサイドから Classic 同様のヘッダーに移動するほどの大きな変更ではないようですが
Lightning Component および Visualforce でアプリを開発している開発者は影響を受ける可能性があります。


## 何が変わるの？

以下で具体的に見ていきましょう。

### 1. Background changes: 背景色の変更

![background-changes]({filename}/images/2017-08-21-lex-styling-changes-in-winter18/background-changes.png)

真っ先に目につくのが背景色です。
これまで白一色だったページの印象ががらっと変わりました。

![background-astro]({filename}/images/2017-08-21-lex-styling-changes-in-winter18/background-astro.png)

よく見るとアストロ君です。氷漬けにされてしまったんでしょうか。

#### **開発者への影響**

特に Lightning Component を開発していて、背景色を明示的に指定していない場合
以下のキャプチャのように新しい背景によってコンポーネントが見づらくなる可能性があります。

![missing-background]({filename}/images/2017-08-21-lex-styling-changes-in-winter18/missing-background.png)

（画像は記事より引用）

背景色を指定するには、コンポーネントの CSS で

```css
.THIS {
  background-color: #fff;
}
```

とするか、または SLDS の `<div class="slds-card">` を使う、あるいは標準コンポーネントの `<lightning:card>` を使うという手段もあるそうです。


### 2. List Density: リストビューの行間が詰まった

左が現在の Summer'17、右がプレリリース環境での Winter'18 です。

![list-density]({filename}/images/2017-08-21-lex-styling-changes-in-winter18/list-density.png)

行間がぎゅっと詰まり、表示できるレコード数が増えたことがわかります。

#### **開発者への影響**

SLDS の [Data Tables](https://www.lightningdesignsystem.com/components/data-tables/) を使っている場合はこの影響を受けます。

### 3. Page Legibility: レコード詳細のフォントサイズが大きくなった

同じく左が Summer'17、右が Winter'18 です。
目視では違いに気づけなかったので開発者コンソールで見てみましたが、1 px 大きくなってます。

![page-legibility]({filename}/images/2017-08-21-lex-styling-changes-in-winter18/page-legibility.png)


#### **開発者への影響**

SLDS で [design token](https://www.lightningdesignsystem.com/design-tokens/#category-font) を使っている場合は影響を受ける可能性があります。
どの token かはわからず。

### 背景色の変更を延期したい

自作にしろ AppExchange からのダウンロードにしろ、たくさんのコンポーネントを利用している組織にとって、背景色がいきなり変わってしまうと問題となる場合があります。
そこで、現在は設定からこの変更を無効化することができます。

![themes-setting]({filename}/images/2017-08-21-lex-styling-changes-in-winter18/themes-setting.png)

（日本語でも themes... で検索すると出ます）


## 実際に確認するには？

https://www.salesforce.com/form/signup/prerelease-winter18.jsp
リンク先から Winter'18 プレリリース環境にサインアップできます。


## おわりに

背景色の変更以外は軽微なアップデートですが、SLDS を使っていると細かいところで自社のアプリのスタイルが崩れてしまいそうですし
使っていなくても変にこのスタイル変更の影響を受けている可能性があるので、プレリリース環境で一度確認しておいた方がよさそうですね。

また、より詳細な情報は 8/29 深夜に予定されている webinar を見るといいとのこと。
[Lightning Updates: Summer, Winter & Beyond | Salesforce Developers](https://developer.salesforce.com/events/webinars/summer-17-lightning-updates)
