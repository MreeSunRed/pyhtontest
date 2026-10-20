# Python 练习：文本分析与数据抓取

两个独立的 Python 小练习：中文文本词频统计，以及从国家统计局接口抓取数据并可视化。

## 目录

```
pyhtontest/
├── 1/                  # 三国演义人物出场统计
└── 2/                  # 国家统计局房价数据抓取与绘图
```

## 1/ 三国演义人物统计

用 `jieba` 对《三国演义》全文分词，结合人物名单统计出场次数，并绘制柱状图。

- `main.py` —— 主程序
- `三国演义.txt` —— 语料
- `人物.txt` —— 人物名单（以「、」分隔）
- `人物2.txt` —— jieba 自定义词典，避免人名被切碎

流程：读取全文 → `jieba.lcut` 分词 → 用人物名构建 `pandas.Series` → 计数排序 → 取前 10 画柱状图。

```bash
cd 1
python main.py
```

依赖：`pandas`、`numpy`、`jieba`、`matplotlib`

## 2/ 房价数据抓取与绘图

从国家统计局数据接口获取北京、上海、天津 2014–2022 年的商品房销售额，绘制折线图并保存为 SVG。

- `main.py` —— 请求接口、解析 JSON、绘图，输出 `房价销售情况.svg`
- `test.py` —— BeautifulSoup 选择器练习，抓取本地静态页面
- `房价销售情况.svg` —— 已生成的示例输出

```bash
cd 2
python main.py
```

依赖：`requests`、`beautifulsoup4`、`numpy`、`matplotlib`

## 说明

- 统计局接口 URL 中的 `k1` 是时间戳参数，接口结构或参数变更后脚本可能失效；年份范围也写死为 2014–2022。
- 图表使用 `SimHei` 显示中文，Windows 自带；其他系统需换成已安装的中文字体。
- 仓库名 `pyhtontest` 是 `pythontest` 的拼写错误，不影响使用，介意可以改名。
