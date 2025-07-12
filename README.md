# Kaggle M5 沃尔玛销售数据分层时间序列预测

<a name="09Hs6"></a>
## 1. 摘要
> 

**The goal:** We have been challenged to **predict sales data** provided by the retail giant [Walmart](https://en.wikipedia.org/wiki/Walmart) **28 days** into the future.<br />**The data:** We are mainly working with a 13,683,901 rows × 13 cols data.**<br />**The result: **We are currently ranking 240/3685(Top 9%), which is in the bronze medal zone.
> 完整摘要：[Abstract.doc](https://www.yuque.com/attachments/yuque/0/2020/doc/1301375/1591925660871-bc82fdf0-faa7-4fed-9bad-09501d2179e9.doc?_lake_card=%7B%22uid%22%3A%221591925659835-0%22%2C%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2020%2Fdoc%2F1301375%2F1591925660871-bc82fdf0-faa7-4fed-9bad-09501d2179e9.doc%22%2C%22name%22%3A%22Abstract.doc%22%2C%22size%22%3A25600%2C%22type%22%3A%22application%2Fwps-writer%22%2C%22ext%22%3A%22doc%22%2C%22progress%22%3A%7B%22percent%22%3A99%7D%2C%22status%22%3A%22done%22%2C%22percent%22%3A0%2C%22id%22%3A%22wtgmR%22%2C%22card%22%3A%22file%22%7D)



<a name="V9PaS"></a>
## 2. 数据描述
<a name="HBdGc"></a>
### 2.1 原始数据
> 数据一共有三个csv文件，涵盖了沃尔玛在2011-2016销售的信息

<a name="9xY1v"></a>
#### 2.1.1 销售分层时间序列数据[sales_train_validation.csv](https://www.yuque.com/attachments/yuque/0/2020/csv/1301375/1591865950245-6199f8b5-2410-4e74-af6a-6595664c1028.csv?_lake_card=%7B%22uid%22%3A%221589416747457-0%22%2C%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2020%2Fcsv%2F1301375%2F1591865950245-6199f8b5-2410-4e74-af6a-6595664c1028.csv%22%2C%22name%22%3A%22sales_train_validation.csv%22%2C%22size%22%3A120007726%2C%22type%22%3A%22text%2Fcsv%22%2C%22ext%22%3A%22csv%22%2C%22progress%22%3A%7B%22percent%22%3A99%7D%2C%22status%22%3A%22done%22%2C%22percent%22%3A0%2C%22id%22%3A%22Sikm7%22%2C%22card%22%3A%22file%22%7D)
![image.png](https://cdn.nlark.com/yuque/0/2020/png/1301375/1589416254603-000c44de-62c2-4092-8ac9-2b6a7e19c746.png#align=left&display=inline&height=155&margin=%5Bobject%20Object%5D&name=image.png&originHeight=310&originWidth=2206&size=85159&status=done&style=none&width=1103)<br /> The main data were obtained in 10 Walmart stores from the 3 US states of California (CA), Texas (TX), and Wisconsin (WI).
> Note: the test set (28 days we are challenged to predict) is not included

- **“Hierarchical” information:**** **The data split comprises 3049 individual products from 3 categories and 7 departments, sold in 10 stores in 3 states, thus can be aggregated on 4 different levels: item level, department level, product category level, and state level(or combined levels).
- Time Series data: 42,840 hierarchical sales time series, 1 column for each of the 1941 days from 2011-01-29 and 2016-05-22.



<a name="e7lW9"></a>
#### 2.1.2 商品价格信息[sell_prices.csv](https://www.yuque.com/attachments/yuque/0/2020/csv/1301375/1591865950363-a9033ef6-a6dc-40a6-b18d-2d96157a86d5.csv?_lake_card=%7B%22uid%22%3A%221589417174191-0%22%2C%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2020%2Fcsv%2F1301375%2F1591865950363-a9033ef6-a6dc-40a6-b18d-2d96157a86d5.csv%22%2C%22name%22%3A%22sell_prices.csv%22%2C%22size%22%3A203395785%2C%22type%22%3A%22text%2Fcsv%22%2C%22ext%22%3A%22csv%22%2C%22progress%22%3A%7B%22percent%22%3A99%7D%2C%22status%22%3A%22done%22%2C%22percent%22%3A0%2C%22id%22%3A%22c6MuY%22%2C%22refSrc%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2020%2Fcsv%2F1301375%2F1591865950363-a9033ef6-a6dc-40a6-b18d-2d96157a86d5.csv%22%2C%22card%22%3A%22file%22%7D)
![image.png](https://cdn.nlark.com/yuque/0/2020/png/1301375/1589417683717-0b8636a5-4bbe-4c27-9fb5-ba786350f256.png#align=left&display=inline&height=131&margin=%5Bobject%20Object%5D&name=image.png&originHeight=340&originWidth=686&size=37853&status=done&style=none&width=264)

- Weekly average prices:  The store and item IDs together with the sales price of the item as a weekly average.
> Note: the test set (28 days we are challenged to predict) is  included in this csv



<a name="JYZY5"></a>
#### 2.1.3 节假日信息[calendar.csv](https://www.yuque.com/attachments/yuque/0/2020/csv/1301375/1591865950495-ac5a9220-2bbc-4b75-9e0a-9047a58a14e0.csv?_lake_card=%7B%22uid%22%3A%221589417260172-0%22%2C%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2020%2Fcsv%2F1301375%2F1591865950495-ac5a9220-2bbc-4b75-9e0a-9047a58a14e0.csv%22%2C%22name%22%3A%22calendar.csv%22%2C%22size%22%3A103469%2C%22type%22%3A%22text%2Fcsv%22%2C%22ext%22%3A%22csv%22%2C%22progress%22%3A%7B%22percent%22%3A99%7D%2C%22status%22%3A%22done%22%2C%22percent%22%3A0%2C%22id%22%3A%229MFP1%22%2C%22card%22%3A%22file%22%7D)
![image.png](https://cdn.nlark.com/yuque/0/2020/png/1301375/1589417889842-0263f271-b36a-43e3-92a6-df97456eb40f.png#align=left&display=inline&height=304&margin=%5Bobject%20Object%5D&name=image.png&originHeight=608&originWidth=1986&size=118303&status=done&style=none&width=993)<br />Dates together with related features like day-of-the week, month, year, and special holidays

- Event days: Religious, sports or cultural event days like SuperBowl.
- SNAP days:  whether the stores in each state allowed purchases with [SNAP food stamps](https://www.benefits.gov/benefit/361).



<a name="rJT1L"></a>
### 2.2 数据的时间分布
The sales information in 3 .csv files following reaches back from Jan 2011 to June 2016, as well as prices and events calendar provided additionally.<br />The validation set is provided but the evaluation set is unknown (teams will be ranked based on RMSE scores in predicting evaluation set.)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/1301375/1589442024077-629edf28-e193-43a9-a015-54f4cf5e2af2.png#align=left&display=inline&height=281&margin=%5Bobject%20Object%5D&name=image.png&originHeight=600&originWidth=1082&size=73314&status=done&style=none&width=507)
<a name="GUsbW"></a>
## 3. 数据可视化
We draw many plots to find the patterns of data. The following 3 mindmaps are all conclusions we found in above-mentioned 3 files. To keep this report brief, we will only cover ground overview in this parts. And the next "Feature Engineering" parts we present the EDA directly related to each topics.

<a name="LZ0DS"></a>
### 3.1 汇总层面
> 交互式版本可以打开： [EDA-TS-1.html](https://www.yuque.com/attachments/yuque/0/2020/html/1301375/1591865950596-69f60d33-b545-41ac-8a84-1a672f076ec0.html?_lake_card=%7B%22uid%22%3A%221589425852490-0%22%2C%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2020%2Fhtml%2F1301375%2F1591865950596-69f60d33-b545-41ac-8a84-1a672f076ec0.html%22%2C%22name%22%3A%22EDA-TS-1.html%22%2C%22size%22%3A4815618%2C%22type%22%3A%22text%2Fhtml%22%2C%22ext%22%3A%22html%22%2C%22progress%22%3A%7B%22percent%22%3A99%7D%2C%22status%22%3A%22done%22%2C%22percent%22%3A0%2C%22id%22%3A%22gq4Dt%22%2C%22card%22%3A%22file%22%7D)

- **Aggregating to 1 time series:**

![image.png](https://cdn.nlark.com/yuque/0/2020/png/1301375/1589425500839-05cec5d4-7f5d-4fce-87e9-d59bde3e6d57.png#align=left&display=inline&height=250&margin=%5Bobject%20Object%5D&name=image.png&originHeight=832&originWidth=1540&size=401778&status=done&style=none&width=463)

   - Sales are generally going up, the most recent sales(2015~2016) appear to grow a bit faster.
   - Some yearly seasonality and strong weekly seasonality.
   - A dip at Christmas, which [the day of the year](https://www.countryliving.com/shopping/a23899891/walmart-christmas-hours/)  the stores are closed.
- **Explanation of features with 7days rolling:**

**![image.png](https://cdn.nlark.com/yuque/0/2020/png/1301375/1589443971790-05add44d-920d-4819-8887-a231762b9264.png#align=left&display=inline&height=275&margin=%5Bobject%20Object%5D&name=image.png&originHeight=582&originWidth=1208&size=83459&status=done&style=none&width=571)**

   - The weekly pattern is strong, with Sat and Sun standing out prominently.
   - The months of Nov and Dec show clear dips, while the summer months May, Jun, and Jul suggest a milder secondary dip.
- **Explanation of features 3~37:**
   - However, we use the lag started from 28 instead of 1, because it will appear "rolling predictions" problem that make the later models unstable in forecasting.



<a name="tWkWk"></a>
### 3.2 分层层面
<a name="5gVvT"></a>
#### 3.2.1 时间序列分到第一层：Sales per State:
> 下图的交互式版本：:[EDA-TS-2.html](https://www.yuque.com/attachments/yuque/0/2020/html/1301375/1591865951130-90976827-e710-4736-864b-109c5a10206d.html?_lake_card=%7B%22uid%22%3A%221589426278334-0%22%2C%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2020%2Fhtml%2F1301375%2F1591865951130-90976827-e710-4736-864b-109c5a10206d.html%22%2C%22name%22%3A%22EDA-TS-2.html%22%2C%22size%22%3A4703440%2C%22type%22%3A%22text%2Fhtml%22%2C%22ext%22%3A%22html%22%2C%22progress%22%3A%7B%22percent%22%3A99%7D%2C%22status%22%3A%22done%22%2C%22percent%22%3A0%2C%22id%22%3A%22qYsxS%22%2C%22refSrc%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2020%2Fhtml%2F1301375%2F1591865951130-90976827-e710-4736-864b-109c5a10206d.html%22%2C%22card%22%3A%22file%22%7D) 

![image.png](https://cdn.nlark.com/yuque/0/2020/png/1301375/1589426131961-5866acbb-53b3-41b4-ad33-63df7817f975.png#align=left&display=inline&height=250&margin=%5Bobject%20Object%5D&name=image.png&originHeight=832&originWidth=1540&size=262729&status=done&style=none&width=463)

   - California (CA) sells more items in general(maybe because it contains 3 stores in data)
   - Wisconsin (WI) was slowly catching up to Texas (TX) and eventually surpassed in the last months.
<a name="jpewh"></a>
#### 3.2.2 时间序列分到第二层：Sales per stores:
**![image.png](https://cdn.nlark.com/yuque/0/2020/png/1301375/1589429484299-75ebadaa-f7ad-47a1-8850-0893de7317ab.png#align=left&display=inline&height=250&margin=%5Bobject%20Object%5D&name=image.png&originHeight=826&originWidth=1534&size=182506&status=done&style=none&width=464)

   - The CA stores are relatively well separated in store volume. 
      - “CA_2”, which declines to the “CA_4” level in 2015, recover and jump up to “CA_1” sales later.
   - TX stores are quite close together in sales
   - The WI stores “WI_1” and “WI_2” show a curious jump in 2012, while “WI_3” shows a long dip.
- **第二层+第三层综合分层可视化：**

![image.png](https://cdn.nlark.com/yuque/0/2020/png/1301375/1589445331729-09b0d73e-482c-427d-8ca6-f2c2347ae521.png#align=left&display=inline&height=269&margin=%5Bobject%20Object%5D&name=image.png&originHeight=920&originWidth=1632&size=137327&status=done&style=none&width=478)

   - “FOODS_3” is clearly driving the majority of “FOODS” category sales.
   - “HOUSEHOLD_1” is also outselling “HOUSEHOLD_2”.
   - “HOBBIES_1” has higher  sales  than “HOBBIES_2”, but both are not growing over time.
<a name="Lu7Yv"></a>
#### 3.2.3 时间序列分到第三层：Sales per Category(Explain Features 6~7):
![image.png](https://cdn.nlark.com/yuque/0/2020/png/1301375/1589428660440-b5a1c01c-e8be-4283-8690-925103861597.png#align=left&display=inline&height=250&margin=%5Bobject%20Object%5D&name=image.png&originHeight=832&originWidth=1540&size=267917&status=done&style=none&width=463)

   - “Foods” are the most common category in terms of sales, followed by “Household” which is still quite a bit above “Hobbies”.
   - However, the number of “Household” rows is closer to the number of “Foods” rows than the corresponding sales figures, indicating that more “Foods” units are sold than “Household” ones.
<a name="7VEYb"></a>
#### 3.2.4 时间序列分到第四层：Sales per items
> 这部分的数据展示比较复杂，所以我也画了一个交互式的图表：[原始数据可视化表盘.html](https://www.yuque.com/attachments/yuque/0/2020/html/1301375/1591867686159-dfcb0d9d-b404-4ae1-a835-b36a63606004.html?_lake_card=%7B%22uid%22%3A%221591867609805-0%22%2C%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2020%2Fhtml%2F1301375%2F1591867686159-dfcb0d9d-b404-4ae1-a835-b36a63606004.html%22%2C%22name%22%3A%22%E5%8E%9F%E5%A7%8B%E6%95%B0%E6%8D%AE%E5%8F%AF%E8%A7%86%E5%8C%96%E8%A1%A8%E7%9B%98.html%22%2C%22size%22%3A19503553%2C%22type%22%3A%22text%2Fhtml%22%2C%22ext%22%3A%22html%22%2C%22progress%22%3A%7B%22percent%22%3A99%7D%2C%22status%22%3A%22done%22%2C%22percent%22%3A0%2C%22id%22%3A%22HcEiF%22%2C%22card%22%3A%22file%22%7D)

![image.png](https://cdn.nlark.com/yuque/0/2020/png/1301375/1591867583376-65735197-fb19-4bc1-9016-15362ab104a9.png#align=left&display=inline&height=481&margin=%5Bobject%20Object%5D&name=image.png&originHeight=962&originWidth=2794&size=441102&status=done&style=none&width=1397)

<a name="du12W"></a>
#### 3.2.5 时间序列中加入价格信息:`Sales.csv`+`Price.csv`
![image.png](https://cdn.nlark.com/yuque/0/2020/png/1301375/1589432912400-707d8428-ed49-4c0f-97e5-fcf838da6951.png#align=left&display=inline&height=275&margin=%5Bobject%20Object%5D&name=image.png&originHeight=832&originWidth=1540&size=252160&status=done&style=none&width=509)

   - First of all, the distributions are almost identical between the 3 states. 
      - Only some minute differences in the “FOODS” category
   - Also, there are notable differences between the categories: FOODs are on average cheaper than HOUSEHOLD items. And HOBBIES items span a wider range of prices than the other two; even suggesting a second peak at lower prices.
<a name="ZoB4k"></a>
#### 3.2.6 时间序列中加入节假日信息: `Sales.csv`+`Calendar``.csv`

   - **Events effect on sales in different category:**

**![image.png](https://cdn.nlark.com/yuque/0/2020/png/1301375/1589433925333-7990e12a-5c12-42ef-bee3-5b6134df4bd1.png#align=left&display=inline&height=290&margin=%5Bobject%20Object%5D&name=image.png&originHeight=1018&originWidth=1852&size=608306&status=done&style=none&width=528)**

      - For HOBBIES, normal days have slightly large sales(also larger above-average portion)
      - FOODS sales are notably higher during “Sporting” events.
      - In general, “National” and “Religious” events both lead to relative decline in sales volume. 
   - **Events effect on sales in different ****State:**

**![image.png](https://cdn.nlark.com/yuque/0/2020/png/1301375/1589435380025-4d0d3dd5-29d3-4e83-9633-666efd1fe824.png#align=left&display=inline&height=298&margin=%5Bobject%20Object%5D&name=image.png&originHeight=920&originWidth=1632&size=475581&status=done&style=none&width=528)**

      - Special events slightly outsell non-event days in TX before 2014.
      - For WI, “National” events have a strong negative impact on sales numbers.
      - In contrast, “Religious” events have the smallest, but still negative impact in WI.
      - “Sporting” events have a positive influence in each state.
   - **SNAP days effect on sales in different ****State:**

**![image.png](https://cdn.nlark.com/yuque/0/2020/png/1301375/1589434958998-84f1ed78-4bba-47e1-806e-9455798d8c29.png#align=left&display=inline&height=224&margin=%5Bobject%20Object%5D&name=image.png&originHeight=894&originWidth=2112&size=723709&status=done&style=none&width=528)**

      - The SNAP days have clearly higher sales in every state. 
      - The largest difference to non-SNAP days is present for WI
<a name="NcLJf"></a>
### 3.3 数据表盘和模型应用的用户界面
为了后期能更好的展示数据、并且在模型训练完之后可以实现输入新数据，给出预测的功能，我简单的绘制了一个web，但是时间太紧张了数据后端还没有接好，希望在以后的课程里有机会完善这部分。
> [user interface of data dashboard.zip](https://www.yuque.com/attachments/yuque/0/2020/zip/1301375/1591867773806-29de7e50-95c3-439d-8047-16945d9e9868.zip?_lake_card=%7B%22uid%22%3A%221591867749252-0%22%2C%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2020%2Fzip%2F1301375%2F1591867773806-29de7e50-95c3-439d-8047-16945d9e9868.zip%22%2C%22name%22%3A%22user+interface+of+data+dashboard.zip%22%2C%22size%22%3A5720627%2C%22type%22%3A%22application%2Fzip%22%2C%22ext%22%3A%22zip%22%2C%22progress%22%3A%7B%22percent%22%3A99%7D%2C%22status%22%3A%22done%22%2C%22percent%22%3A0%2C%22id%22%3A%22o8hge%22%2C%22card%22%3A%22file%22%7D)（还不完善）

![image.png](https://cdn.nlark.com/yuque/0/2020/png/1301375/1589450981939-3ac0622a-f167-482a-82c9-a326be14d6fd.png#align=left&display=inline&height=394&margin=%5Bobject%20Object%5D&name=image.png&originHeight=1502&originWidth=2844&size=1712622&status=done&style=none&width=746)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/1301375/1589588781752-76ba29ae-2f09-4a66-9aa0-117ce54508d9.png#align=left&display=inline&height=1001&margin=%5Bobject%20Object%5D&name=image.png&originHeight=2002&originWidth=3840&size=1844886&status=done&style=none&width=1920)
<a name="7IJb0"></a>
## 4. 结论
在数据可视化过程中，发现了不少结论，为了方便后面的特征工程构建以及筛选时的策略构建，我汇总了三份思维导图（分别对应第二部分的3.2.1～3.2.3、3.2.4、3.2.5)：
![](https://cdn.nlark.com/yuque/0/2020/png/1301375/1602431064282-2663aa87-020a-4c06-8303-a00a34df8f27.png)![](https://cdn.nlark.com/yuque/0/2020/png/1301375/1602431063867-75978bc5-a90f-4eda-83b7-d246149f9f9c.png)

![](https://cdn.nlark.com/yuque/0/2020/png/1301375/1602431063886-2fc9fabc-6c8a-4a37-9419-b833abaeed99.png)<a name="odZSG"></a>
### 

<br />

<a name="iw2bA"></a>
## 5. 比赛地址


