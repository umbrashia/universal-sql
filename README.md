# Universal SQL Builder
SQL framework ORM independent, it helps you build sql query in python<br/>
What ever you using Hive, HBase, Spark* SQL, Django & FLASK etc so you can gernate simple SQL query<br/>
Its return raw sql query string this can be use in any Framework<br/>

<br/><h3>Installation</h3>
Step 1: pip install universal-sql-builder<br/>
Step 2: <code>from UniversalSqlBuilder import UniversalSqlBuilder</code><br/>
Step 3: Flow the examples....


<!--New Section **************************-->
<br/><h4>Select</h4>
<br/>
<code>
UniversalSqlBuilder.table("employee").select("id,name").select(",department").get()
</code>



<!--New Section **************************-->
<br/><h4>Where</h4>
You can use key and value based parameters : where("city=", "ABC")<br>
Or you can use raw where query : 
where("col=(select id from users)")
<br/>
<code>
UniversalSqlBuilder.table("employee").select("id,name").select(",department").where("ram=(select id from users)").where("city=", "delhi").get()
</code>

<!--New Section **************************-->
<br/><h4>OrWhere and WhereBetween</h4>
If you want data according min and max  use : <br/>
<code>
whereBetween("age",[200,300]) </code>
<code>
UniversalSqlBuilder.table("employee").select("id,name").whereBetween("age",[200,300]).get()
</code><br/>
Using OR with where :<br>
<code>
UniversalSqlBuilder.table("employee").select("id,name").orWhere("seller=",'100').get()
</code>


<!--New Section **************************-->
<br/><h4>GroupBy, OrderBy amd Limit
</h4>
Use of group by : groupBy("name")

<br><code>UniversalSqlBuilder.table("employee").select("id,name").groupBy("name").get()</code>

Use order by : orderBy("ID","desc") 

<br><code>UniversalSqlBuilder.table("employee").select("id,name").orderBy("ID","desc").get()</code>

use with limit : limit(10,20)

<br><code>UniversalSqlBuilder.table("employee").select("id,name").limit(10,20).get()</code>


<!--New Section **************************-->
<br/><h4>Join ('FULL OUTER', 'INNER', 'LEFT', 'RIGHT', 'JOIN')</h4><br/>
Default : <code>join("users","users.id=employee.emp_id")</code><br/>

FULL OUTER : <code>join("users","users.id=employee.emp_id","FULL OUTER")</code><br/>

INNER : <code>join("users","users.id=employee.emp_id","INNER")</code><br/>

LEFT : <code>join("users","users.id=employee.emp_id","LEFT")</code><br/>

RIGHT : <code>join("users","users.id=employee.emp_id","RIGHT")</code><br/>

JOIN : <code>join("users","users.id=employee.emp_id","JOIN")</code><br/>


<!--New Section **************************-->
<br/><h4>Having & OrHaving</h4>
Using OR with Having :<br>
<code>
UniversalSqlBuilder.table("employee").select("id,name").orHaving("seller=",'100').get()
</code><br><br/>
You can use key and value based parameters : having("city=", "ABC")<br>
Or you can use raw where query : having("col=(select id from users)")<br/>
<br/>
<code>
UniversalSqlBuilder.table("employee").select("id,name").select(",department").having("id=(select id from users)").having("city=", "delhi").get()
</code>

<!--New Section **************************-->
<br/><h4>Making Advance Query</h4>
Using OR with Having :<br>
<code>
print(UniversalSqlBuilder.table("employee")
      .select("id,name")
      .select(",department")
      .where("city=", "delhi")
      .where("order_id=("+UniversalSqlBuilder.table("orders as temp").select("temp.id").orderBy("temp.id", "desc").get()+")")
      .orWhere("seller=", '100')
      .orWhere("brand=", 'rock')
      .having("city=", "delhi")
      .orHaving("seller=", '100')
      .orHaving("brand=", 'rock')
      .whereBetween("age", [200, 300])
      .join("users", "users.id=employee.emp_id", "left")
      .join("cars", "cars.id=employee.emp_id")
      .groupBy("name")
      .orderBy("ID", "desc")
      .limit(10, 20).get())
</code><br><br>
SELECT 
    id, name, department
FROM
    employee
        LEFT JOIN
    users ON users.id = employee.emp_id
        INNER JOIN
    cars ON cars.id = employee.emp_id
WHERE
    city = 'delhi'
        AND order_id = (SELECT 
            temp.id
        FROM
            orders AS temp
        ORDER BY temp.id DESC)
        AND age >= 200
        AND age <= 300
        AND (seller = '100' OR brand = 'rock')
GROUP BY name
HAVING city = 'delhi'
    AND (seller = '100' OR brand = 'rock')
ORDER BY ID DESC
LIMIT 20 , 10
<br/>




<!--New Section **************************
<br/><h4>____________</h4>
---------------------------------------------
<br/>
<code>
print(UniversalSqlBuilder.table("employee")
     .select("id,name")
     .select(",department")
     .where("ram=(select id from users)")
     .where("city=", "delhi")
     .orWhere("seller=",'100')
     .orWhere("brand=",'rock')
     .whereBetween("age",[200,300])
     .join("users","users.id=employee.emp_id","left")
     .join("cars","cars.id=employee.emp_id")
     .groupBy("name")
     .orderBy("ID","desc")
     .limit(10,20).get())
</code>-->