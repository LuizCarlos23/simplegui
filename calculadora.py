import PySimpleGUI as sg

layout = [
  [ sg.B("C", size=[3, 2], font="3"), sg.T("0", font=[16,16], size=(32,1), key='-RESULT-')], # Resultado
  [ sg.B("7", size=[3, 3], font="3"),  sg.B("8", size=[3, 3], font="3"), sg.B("9", size=[3, 3], font="3"), sg.B("/", size=[3, 3], font="3")], # 7 8 9 /
  [ sg.B("4", size=[3, 3], font="3"),  sg.B("5", size=[3, 3], font="3"), sg.B("6", size=[3, 3], font="3"), sg.B("x", size=[3, 3], font="3") ], # 4 5 6 x
  [ sg.B("1", size=[3, 3], font="3"),  sg.B("2", size=[3, 3], font="3"), sg.B("3", size=[3, 3], font="3"), sg.B("-", size=[3, 3], font="3")  ], # 1 2 3 -
  [ sg.B("0", size=[3, 3], font="3"),  sg.B(".", size=[3, 3], font="3"), sg.B("=", size=[3, 3], font="+"), sg.B("+", size=[3, 3], font="3")], # 0 . = +
]

window = sg.Window("Calculadora", layout, size=[300, 380])

valueA = ""
valueB = ""
operation = ""
resultFinal = "undefined"


def operationsFunctions(op, valueA, valueB):
  if (valueA == "") : valueA = resultFinal
  print("resultFinal", resultFinal)
  print("valueA", valueA)
  print("valueB", valueB)


  values = [float(valueA), float(valueB)]
  result = 0

  print(values)

  if (op == "somar"):
    result = values[0] + values[1]
  elif (op == "sub"):
    result = values[0] - values[1]
  elif (op == "mult"):
    result = values[0] * values[1]
  elif (op == "div"):
    result = values[0] / values[1]
  window["-RESULT-"].update(result)
  return str(result)

while True:
  event, windowValue = window.read()
  if (event == sg.WINDOW_CLOSED or event == 'Quit'):
    break

  if ( event.isnumeric() or event == "."):
    if (operation == ""):
      valueA += event
      window["-RESULT-"].update(valueA)
    else:
      valueB += event
      window["-RESULT-"].update(valueB)
  elif ( event == "+" ) : operation = "somar"
  elif ( event == "-" ) : operation = "sub"
  elif ( event == "x" ) : operation = "mult"
  elif ( event == "/" ) : operation = "div"
  elif ( event == "=" and operation != "" ) : 
    resultFinal = operationsFunctions(operation, valueA, valueB)
    valueA = ""
    valueB = ""
    operation = ""
  elif ( event == "C" ):
    if (operation == ""):
      valueA = valueA[:-1]
      window["-RESULT-"].update(valueA)
    else:
      valueB = valueB[:-1]
      window["-RESULT-"].update(valueB)


window.close()