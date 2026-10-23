---
name: cn-12306-train-tickets
description: 查国内某天某条线路的高铁/普速车次、余票和票价：12306 无需登录的两个接口怎么用，站名代码怎么对。查车次票价时读。
sites: kyfw.12306.cn
topics: 高铁 火车 车次 票价 余票 12306
verified: 2026-10-23
---
# 12306 车次与票价查询（不用登录）

两次实测可用（2026-10-22、2026-10-23，上海→杭州、京沪方向）。车次、余票、票价以 12306 为准；本页只讲怎么读，不记价格。

## 步骤
1. 先 GET `https://kyfw.12306.cn/otn/leftTicket/init` 取 cookie，带上 Referer 也设成这个地址。
2. 用探针接口问当前该用哪个：请求 `/otn/leftTicket/queryZ?leftTicketDTO.train_date=<日期>&leftTicketDTO.from_station=<城市代码>&leftTicketDTO.to_station=<城市代码>&purpose_codes=ADULT`，它不返回车次，只回一个 JSON，里面的 `c_url`（见过 `leftTicket/queryG`）才是当前的车次列表接口。接口名会变，不要写死。
3. 车次列表：把上面的 c_url 拼成 `https://kyfw.12306.cn/otn/<c_url>?...`（同样四个参数）。返回 `data.result` 是每行一串用 `|` 分开的字段。
4. `data.map` 是车站代码→站名的对照表，用它把代码翻成中文站名。

## 车次行怎么解
按 `|` 切开后（0 开始数）：2=train_no、3=车次、6=出发站代码、7=到达站代码、8=开车时间、9=到站时间、10=历时、12=余票信息（编码串）、16=出发站序号 from_station_no、17=到达站序号 to_station_no。

同一趟车会出现多行（不同出发站、不同到达站各一行）；from_station 参数传的是城市代码（如 SHH=上海、HZH=杭州），所以一次能拿到该城市所有站（上海虹桥 AOH、上海 SHH、上海南 SNH、上海西 SXH、上海松江 IMH）。

## 票价
`https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no=<第2字段>&from_station_no=<第16字段>&to_station_no=<第17字段>&seat_types=OM9P&train_date=<日期>`
返回 `data` 里的键：O=二等座、M=一等座、A9=商务座、P=特等座、WZ=无座。序号必须跟这一行对上，否则算的是别的区间。
票价是分车次的（同一线路不同车次公布票价不同，有的还打折），所以逐趟查，别按一两趟推整条线。

## 边界
- 查询不用登录；**订票必须本人 12306 账号，不要代登录，交给本人**。
- 具体余票会变，报出去的时候说明以当时查询为准。
