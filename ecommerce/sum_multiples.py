# class Multiples:
#     def sum_multiples(self, limit, first_number, second_number):
#         # x = int(input("Enter the first number: "))
#         # y = int(input("Enter the second number: "))
#         num1_limit = limit // first_number
#         num2_limit = limit // second_number
#         # output_x, output_y, output_x1, output_y1 = 0
#         output_x = 0
#         output_x1 = 0
#         output_y1 = 0
#         output_y = 0
#         for item in range(0, num1_limit):
#             output_x += first_number
#             output_x1 += output_x
#         # print(output_x1)
#         for item in range(0, num2_limit):
#             output_y += second_number
#             output_y1 += output_y
#         # print(output_y1)
#         result = output_x1 + output_y1
#         # print(result)
#         return result
#
#
# # sum1 = Multiples()
# # exe2 = sum1.sum_multiples(20, 5, 3)
# # print(exe2)

x, y = 3, 5
output = 0
for i in range(1, 20 + 1):
    if i % x == 0 or i % y == 0:
        output += i
        print(i)
print(output)
