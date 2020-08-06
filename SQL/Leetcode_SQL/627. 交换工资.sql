######方法1 case when语句
update salary
set sex = case sex 
          when 'm' then 'f'
          else 'm' end
          
######方法2 if语句
update salary
set sex = if(sex='f','m','f')

