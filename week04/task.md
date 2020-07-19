| sql                                                          | pandas                                         |
| ------------------------------------------------------------ | ---------------------------------------------- |
| SELECT * FROM data;                                          | print(data);                                   |
| SELECT * FROM data LIMIT 10;                                 | data.head(10)                                  |
| SELECT id FROM data;                                         | data.loc[id:id,]                               |
| SELECT COUNT(id) FROM data;                                  | data['id'].count()                             |
| SELECT * FROM data WHERE id<1000 AND age>30;                 | data[(data['id']<1000)&(data[age]>30)]         |
| SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;  | table1.groupby('id')['order_id'].count()       |
| SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id; | pd.merge(table1, table2, on='id', how='inner') |
| SELECT * FROM table1 UNION SELECT * FROM table2;             | pd.concat([table1, table2])                    |
| DELETE FROM table1 WHERE id=10;                              | table1[table1['id'] != 10]                     |
| ALTER TABLE table1 DROP COLUMN column_name;                  | table1.drop( 'column_name' ,axis = 1)          |
