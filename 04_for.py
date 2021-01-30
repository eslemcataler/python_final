string="Eslem"

for i in string:
    print(i)

for i in range(1,11,2):
    print(i)

#       *
#     *****
#   *********
# *************

for k in range(1,14,4):
    print("{:^15}".format(k*"*"))