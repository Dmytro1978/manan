def anti_vowel(str1):
    outStr=""
    vowelStr="aeiou"
    for v in str1:
    	if str.lower(v) in vowelStr:
    		continue
    	else:
    		outStr += v
    return outStr
print anti_vowel("Congratulation!")
