a
     S?`?	  ?                   @   s?   d dl Z e ?d? e ?d? e ?e jdkr.dnd? d dlZd dl Z d dlZe?d?Ze?d?Zeej	? e
d	?Zeej	v r~ne?  e ?e jdkr?dnd? d
ZdZdZeed ? dd? Ze?  dS )?    Nzpkg install requestszpkg install random?nt?cls?clearz!https://pastebin.com/raw/R6Cvh21Yz!https://pastebin.com/raw/XhuMr4EXz
[+]Pasword Bnwsa : z[1;31mz[1;32mz[1;33ma  
       _                             ______    _ _               
      | |                           |  ____|  | | |              
      | | _____   _____  _ __ ___   | |__ ___ | | | _____      __
  _   | |/ _ \ \ / / _ \| '_ ` _ \  |  __/ _ \| | |/ _ \ \ /\ / /
 | |__| |  __/\ V / (_) | | | | | | | | | (_) | | | (_) \ V  V / 
  \____/ \___| \_/ \___/|_| |_| |_| |_|  \___/|_|_|\___/ \_/\_/  
                                                                 
                                                                 
c                     s?   t d?} td? d? d?? fdd?td?D ??}|? d?}d}d	d
ddddddddddddddd?}d|| ddddd?}tj|||d?}ttd  ? ttd! ? d S )"Nz[+]Username :? Zqwertyuiopasdfghjklzxcvbnmc                 3   s   | ]}t ?? ?V  qd S )N)?randomZchoice)?.0?i??list? ?:C:\Users\AHMED\Desktop\New-folder(5)\Followers-by-jev0m.py?	<genexpr>"   ?    zFolowers.<locals>.<genexpr>?   z
@gmail.comz1https://core.poprey.com/api/create_test_order.phpz!application/json, text/plain, */*zgzip, deflate, brzen-US,en;q=0.9,ar;q=0.8Z105z!application/x-www-form-urlencoded?1zhttps://poprey.comzhttps://poprey.com/z@"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"z?0?emptyZcorsz	same-sitezsMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36ZnullZen)Zacceptzaccept-encodingzaccept-languagezcontent-lengthzcontent-typeZdnt?originZrefererz	sec-ch-uazsec-ch-ua-mobilezsec-fetch-destzsec-fetch-modezsec-fetch-sitez
user-agentzx-auth-tokenzx-target-langZ	FollowersZ	InstagramZ10Znormal)Zservice?email?username?systemZplanZtariffZcsrf)?headers?datau   Request sent ✅. zC[!]In case you don't receive your followers, try it at a later time)?input?print?join?range?requestsZpost?G?Y)r   Zemlr   Zurlr   r   Zreqr   r	   r   ?Folowers   sD    
??	r   )?osr   ?namer   r   ?get?g?sr   ?textr   Zaskv?exit?Rr   r   r   r   r   r   r   ?<module>   s(   






%