# xss-pattern
this tool is influence gf pattern by tomnomnom but this is only focus for xss.

it filter out all urls if any url follow the pattern or the parameter are found in urls

ex: 
 cat domains.txt | waybackurls | python xss-pattern.py 
 
 
 
ex :
 python xss-pattern.py  google-param.txt > result.txt
