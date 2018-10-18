# expr = input().lower().split()
#
# # expr = (15.5, "mile", "in", "km")
#
# CONV_TABLE = (("mile", 1609),
#               ("yard", 0.9144),
#               ("foot", 0.3048),
#               ("inch", 0.0254),
#               ("km", 1000),
#               ("m", 1.0),
#               ("cm", 0.01),
#               ("mm", 0.001))
#
# expr_value = float(expr[0])
# from_value = expr[1]
# to_value = expr[3]
# meters = float(0)
#
#
# for ed, curs in CONV_TABLE:
#     if from_value == ed:
#         meters = expr_value * float(curs)
#
#
#
# for ed, curs in CONV_TABLE:
#     if to_value == ed:
#         meters = meters / float(curs)
#
#
#
#
# print("{:.2e}".format(meters))

eta, inp = dict(mile=1609, yard=0.9144, foot=0.3048, m=1.0,
                inch=0.0254, km=1000, cm=0.01, mm=0.001), input().split()
print(eta, inp)

x = float(inp[0]) * eta[inp[1]] / eta[inp[3]]
print('{:.2e}'.format(x))
