# Wasm Component Model における、`borrow` された `resource` の規約を破る例

下記の[Fukuoka.wasm #1](https://fukuokawasm.connpass.com/event/407733/)や、[JSConf JP 2026 の発表](https://jsconf.jp/2026/ja/talks/yuji-yamamoto)で触れたサンプルコードです。

- [Component Model の borrow 契約を破ってみる](https://the.igreque.info/slides/2026-11-12-fukuoka.wasm)
- [JS･WasmにもあるRustのアレ - コンポーネント間でやりとりするオブジェクトを管理する](https://the.igreque.info/slides/2026-11-22-ownership)

## ビルド・実行方法

```bash
git clone https://github.com/igrep/wasm-component-example/
cd wasm-component-example/resource
pnpm install
bash build.sh
node processor-host.js
```
