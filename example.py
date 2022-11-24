from thefuzz import fuzz, process

s1 ="#59 shiva krupa 3rd b cross basavasamithi layout tindlue vidyaranyapura bangalore"
s2 = "59 basavasamithi  tindlu vidayaranya pura"

print(fuzz.ratio(s1,s2))
print(fuzz.partial_ratio(s1,s2))
print(fuzz.token_sort_ratio(s1,s2))
print(fuzz.token_set_ratio(s1,s2))