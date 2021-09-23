from UniversalSqlBuilder import UniversalSqlBuilder, SqlLoader


print(UniversalSqlBuilder.table("employee")
      .select("id,name")
      .select(",department")
      .where("city=", "delhi")
      .where("order_id=("+UniversalSqlBuilder.table("emp_orders as temp").select("temp.id").orderBy("temp.id", "desc").get()+")")
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
