# Video Game Sales

#### By Kyle Chutjian and Thomas Eckert



## Introduction
The dataset we chose was video game sales. This dataset contains 11 columns: Rank, Name, Platform, Year, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, and Global_Sales. There are 16,598 entries, with many possible data outputs we can choose from. We are currently only using the top 100 entries, shown in our sample.csv file on GitHub. We separated this dataset into 5 tables: Genre, Game. Sales. Publisher, and Platform.


## Models
#### Entity-Relation Diagram

<img src="milestone 1-ER diagram.jpg" tag="ER-Diagram">

#### Relational-Model Diagram

<img src="milestone 1-RM diagram.jpg">


## Tables

#### Game Table

| Rank | Name | Platform_Id | Year | Genre_Id | Publisher_Id | NA_Sales | EU_Sales | JP_Sales | Other_Sales | Global_Sales |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Wii Sports | 1 | 2006 | 1 | 1 | 41 | 29 | 4 | 8 | 83 |
|    2 | Super Mario Bros.                            |           2 | 1985 |        2 |            1 |       29 |        4 |        7 |           1 |           40 |
|    3 | Mario Kart Wii                               |           1 | 2008 |        3 |            1 |       16 |       13 |        4 |           3 |           36 |
|    4 | Wii Sports Resort                            |           1 | 2009 |        1 |            1 |       16 |       11 |        3 |           3 |           33 |
|    5 | Pokemon Red/Pokemon Blue                     |           5 | 1996 |        5 |            1 |       11 |        9 |       10 |           1 |           31 |
|    6 | Tetris                                       |           5 | 1989 |        6 |            1 |       23 |        2 |        4 |           1 |           30 |
|    7 | New Super Mario Bros.                        |           7 | 2006 |        2 |            1 |       11 |        9 |        7 |           3 |           30 |
|    8 | Wii Play                                     |           1 | 2006 |        8 |            1 |       14 |        9 |        3 |           3 |           29 |
|    9 | New Super Mario Bros. Wii                    |           1 | 2009 |        2 |            1 |       15 |        7 |        5 |           2 |           29 |
|   10 | Duck Hunt                                    |           2 | 1984 |       10 |            1 |       27 |        1 |        0 |           0 |           28 |


#### Genre Table

| Genre_Id | Genre_Name |
| --- | --- |
|        1 | Sports       |
|        2 | Platform     |
|        3 | Racing       |
|        4 | Sports       |
|        5 | Role-Playing |
|        6 | Puzzle       |
|        7 | Platform     |
|        8 | Misc         |
|        9 | Platform     |
|       10 | Shooter      |

#### Publisher Table

| Publisher_Id | Publisher_Name |
| --- | --- |
|            1 | Nintendo                    |
|            2 | Nintendo                    |
|            3 | Nintendo                    |
|            4 | Nintendo                    |
|            5 | Nintendo                    |
|            6 | Nintendo                    |
|            7 | Nintendo                    |
|            8 | Nintendo                    |
|            9 | Nintendo                    |
|           10 | Nintendo                    |

#### Platform Table

| Platform_Id | Platform_Name |
| --- | --- |
|           1 | Wii           |
|           2 | NES           |
|           3 | Wii           |
|           4 | Wii           |
|           5 | GB            |
|           6 | GB            |
|           7 | DS            |
|           8 | Wii           |
|           9 | Wii           |
|          10 | NES           |



## Graphs
<img src="graph1.jpg">
<img src="graph2.jpg">
<img src="graph3.jpg">
<img src="graph4.jpg">
<img src="graph5.jpg">



## GitHub Link
https://github.com/KyleChutjian/VideoGameSales