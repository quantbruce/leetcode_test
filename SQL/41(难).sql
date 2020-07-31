create trigger audit_log after insert on employees_test
begin
    insert into audit(emp_no, NAME) values(NEW.id, NEW.NAME);
end

