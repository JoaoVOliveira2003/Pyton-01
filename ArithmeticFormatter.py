def arithmetic_arranger(problems, answer=False):
  if len(problems) > 5:
      return "Error: Too many problems."

  first_operand = []
  second_operand = []
  operator = []

  for problem in problems:
      pieces = problem.split()
      first_operand.append(pieces[0])
      operator.append(pieces[1])
      second_operand.append(pieces[2])

  if "*" in operator or "/" in operator:
      return "Error: Operator must be '+' or '-'."

  for i in range(len(first_operand)):
      if not (first_operand[i].isdigit() and second_operand[i].isdigit()):
          return "Error: Numbers must only contain digits."

  for i in range(len(first_operand)):
      if len(first_operand[i]) > 4 or len(second_operand[i]) > 4:
          return "Error: Numbers cannot be more than four digits."

  first_line = []
  second_line = []
  third_line = []
  fourth_line = []

  for i in range(len(first_operand)):
      if len(first_operand[i]) > len(second_operand[i]):
          first_line.append(" "*2 + first_operand[i])
      else:
          first_line.append(" "*(len(second_operand[i]) - len(first_operand[i]) + 2) + first_operand[i])

  for i in range(len(second_operand)):
      if len(second_operand[i]) > len(first_operand[i]):
          second_line.append(operator[i] + " " + second_operand[i])
      else:
          second_line.append(operator[i] + " "*(len(first_operand[i]) - len(second_operand[i]) + 1) + second_operand[i])

  for i in range(len(first_operand)):
      third_line.append("-"*(max(len(first_operand[i]), len(second_operand[i])) + 2))

  if answer:
      for i in range(len(first_operand)):
          if operator[i] == "+":
              ans = str(int(first_operand[i]) + int(second_operand[i]))
          else:
              ans = str(int(first_operand[i]) - int(second_operand[i]))

          if len(ans) > max(len(first_operand[i]), len(second_operand[i])):
              fourth_line.append(" " + ans)
          else:
              fourth_line.append(" "*(max(len(first_operand[i]), len(second_operand[i])) - len(ans) + 2) + ans)
      arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line) + "\n" + "    ".join(fourth_line)
  else:
      arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line)
  return arranged_problems

print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))