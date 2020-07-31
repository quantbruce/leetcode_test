select (length('10,A,B')-length(replace('10,A,B', ',', '')))/length(',') as cnt

最后除以子串的操作，得到子串出现的次数，试想一下子串若不是一个逗号，而是两个逗号，就知道除以子串长度的意义了。



