create trigger audit_log after insert on employees_test
begin
    insert into audit(emp_no, NAME) values(NEW.id, NEW.NAME);
end


链接：https://www.nowcoder.com/questionTerminal/7e920bb2e1e74c4e83750f5c16033e2e?f=discussion
来源：牛客网

构造触发器时注意以下几点：
1、用 CREATE TRIGGER 语句构造触发器，用 BEFORE或AFTER 来指定在执行后面的SQL语句之前或之后来触发TRIGGER
2、触发器执行的内容写出 BEGIN与END 之间
3、可以使用 NEW与OLD 关键字访问触发后或触发前的employees_test表单记录
可参考：http://www.runoob.com/sqlite/sqlite-trigger.html


为 INSERT INTO audit (EMP_NO, NAME) VALUES (NEW.ID, NEW.NAME);
这里的 NEW.ID 是 触发器执行后，audit_log 表中 ID 字段的值，要将其插入到 audit 表的 EMP_NO 字段中。
