# Given an object/dictionary with keys and values that consist of both strings and integers, 
# design an algorithm to calculate and return the sum of all of the numeric values.
# For example, given the following object/dictionary as input:
# {
#   "cat": "bob",
#   "dog": 23,
#   19: 18,
#   90: "fish"
# }
# Your algorithm should return 41, the sum of the values 23 and 18.
# You may use whatever programming language you’d like.
# Verbalize your thought process as much as possible before writing any code. 
# Run through the UPER problem solving framework while going through your thought process.

dict_interview = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}

# use  for loop to go over each value in the dictionary:
#     somehow figure out how to compare the values to see if they are an int 
#     then take the ints, add them together 
#         return the sum

# print(dir(dict_interview))
counter = 0
for v in dict_interview.values():
    if type(v) == int:
        counter += v
print(counter)

