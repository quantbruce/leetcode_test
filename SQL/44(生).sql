#######方法1 
replace into titles_test 
values('5', '10005', 'Senior Engineer', '1986-06-26', '9999-01-01');


######方法2
update titles_test
set emp_no = replace(emp_no, 10001, 10005) # 用了replace
where id = 5

#####方法3
