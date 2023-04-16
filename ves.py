from PIL import Image
import random

def hex2dec(cislo):
  vysledok = 0
  cislo = cislo.replace("\n", "")
  for index in range(len(cislo)):
      cifra = cislo[(index+1)*(-1)].upper()   #tu len prerobim vsetky male pismenka na VELKE
      if ord("A") <= ord(cifra) <= ord("F"):
          cifra = ord(cifra) - 65 + 10
      else:
          cifra = int(cifra)
      vysledok += cifra*16**index
      
  return vysledok

def hexColor(color):
  r = hex2dec(color[1:3])
  g = hex2dec(color[3:5])
  b = hex2dec(color[5:])

  return(r, g, b)

def filled_rectangle(im, Ax, Ay, rwidth, rheight, color):
  for x in range(Ax, Ax + rwidth):
    for y in range(Ay, Ay + rheight):
        im.putpixel((x, y), color)

def linePixels(A, B):
  pixels = []
  if A[0] == B[0]:
    if A[1] > B[1]:
        A,B=B,A
    for y in range(A[1], B[1] + 1):
      pixels.append((A[0], y))
  elif A[1] == B[1]:
    if A[0] > B[0]:
        A,B=B,A
    for x in range(A[0], B[0] + 1):
      pixels.append((x, A[1]))
  else:
    if A[0] > B[0]:
        A,B=B,A
    dx = B[0] - A[0]
    dy = B[1] - A[1]
    if abs(dy/dx) > 1:
      for y in range(min(A[1], B[1]), max(A[1], B[1]) + 1):
        x = int((y - A[1] + (dy/dx) * A[0]) * (dx/dy))
        pixels.append((x, y))
    else:
      for x in range(min(A[0], B[0]), max(A[0], B[0]) + 1):
        y = int((B[1] - A[1])/(B[0] - A[0]) * (x - A[0]) + A[1])
        pixels.append((x, y))
  return pixels


def line(im, A, B, color):
  if A[0] == B[0]:
    if A[1] > B[1]:
        A,B=B,A
    for y in range(A[1], B[1] + 1):
      im.putpixel((A[0], y), color)
  elif A[1] == B[1]:
    if A[0] > B[0]:
        A,B=B,A
    for x in range(A[0], B[0] + 1):
      im.putpixel((x, A[1]), color)
  else:
    if A[0] > B[0]:
        A,B=B,A
    dx = B[0] - A[0]
    dy = B[1] - A[1]
    if abs(dy/dx) > 1:
      for y in range(min(A[1], B[1]), max(A[1], B[1]) + 1):
        x = int((y - A[1] + (dy/dx) * A[0]) * (dx/dy))
        im.putpixel((x, y), color)
    else:
      for x in range(min(A[0], B[0]), max(A[0], B[0]) + 1):
        y = int((B[1] - A[1])/(B[0] - A[0]) * (x - A[0]) + A[1])
        im.putpixel((x, y), color)

def filled_circle(im, Sx, Sy,  r, color):
  S = [int(Sx), int(Sy)]
  #nakreslim do obrazku im kruh so stredom v bode S a s polomer r a s farbou color
  for x in range(0, int(r/2**(1/2)) + 1):
    y = int((r**2 - x**2)**(1/2))
    if 0 < x + int(Sx) < int(im.width) and 0 < int(y) + int(Sy) < int(im.height):
      line(im, (x + S[0], y + S[1]), (x + S[0], -y + S[1]), color)
      line(im, (y + S[0], x + S[1]), (y + S[0], -x + S[1]), color)
      line(im, (-x + S[0], -y + S[1]), (-x + S[0], y + S[1]), color)
      line(im, (-y + S[0], x + S[1]), (-y + S[0], -x + S[1]), color)

def thick_line(im, Ax, Ay, Bx, By, thickness, color):
  A = (Ax, Ay)
  B = (Bx, By)
  pixels = linePixels(A, B)
  for Sx, Sy in pixels:
    filled_circle(im, Sx, Sy, thickness/2, color)

def triangle(im, Ax, Ay, Bx, By, Cx, Cy, thickness, color):
    thick_line(im, Ax, Ay, Bx, By, thickness, color)
    thick_line(im, Ax, Ay, Cx, Cy, thickness, color)
    thick_line(im, Bx, By, Cx, Cy, thickness, color)

def rectangle(im, Ax, Ay, width, height, thickness, color):
    thick_line(im, Ax, Ay, (Ax + width), Ay, thickness, color)
    thick_line(im, Ax, Ay, Ax, (Ay + height), thickness, color)
    thick_line(im, (Ax + width), Ay, (Ax + width), (Ay + height), thickness, color)
    thick_line(im, Ax, (Ay + height), (Ax + width), (Ay + height), thickness, color)

def circle(im, Sx, Sy, r,thickness, color):
  S = [int(Sx), int(Sy)]

  #nakresli do obrazku im kruznicu so stredom v bode S a polomer r farbou color
  for x in range(0, int(r/2**(1/2)) + 1 ):
    y = int((r**2 - x**2)**(1/2))
    if 0 < x + int(Sx) < int(im.width) and 0 < int(y) + int(Sy) < int(im.height):
      im.putpixel((x + S[0], y + S[1]), color)
      im.putpixel((y + S[0], x + S[1]), color)
      im.putpixel((y + S[0], -x + S[1]), color)
      im.putpixel((x + S[0], -y + S[1]), color)
      im.putpixel((-x + S[0], -y + S[1]), color)
      im.putpixel((-y + S[0], -x + S[1]), color)
      im.putpixel((-y + S[0], x + S[1]), color)
      im.putpixel((-x + S[0], y + S[1]), color)

def getY(point):
  return point[1]

def filled_triangle(im, Ax, Ay, Bx, By, Cx, Cy, color):
  A = (Ax, Ay)
  B = (Bx, By)
  C = (Cx, Cy)
  #Nakrelis do obrazku im trojuhlnik s bodmi ABC a farbou color
  V = sorted([A, B, C], key=getY)
  left = linePixels(V[0], V[1]) + linePixels(V[1], V[2])
  right = linePixels(V[0], V[2])
    
  Xmax = max(A[0], B[0], C[0])
  Xmin = min(A[0], B[0], C[0])
  if V[1][0] == Xmax:
    left, right = right, left

  for y in range(getY(V[0]), getY(V[2]) + 1):
    x1 = Xmax
    for X in left:
      if X[1] == y and X[0] < x1:
        x1 = X[0]
    
    x2 = Xmin
    for X in right:
      if X[1] == y and X[0] > x2:
        x2 = X[0]
    
    if x2 < 0:
      continue
    if x2 > im.width:
      x2 = im.width - 1
    if x1 < 0:
      x1 = 0

    line(im, (x1, y), (x2, y), color)

def get_color(lines):
  color = (255, 255, 255)
  for line in lines:
    words = line.split(" ")
    if len(words) == 2 and words[0] == "CLEAR":
      color = hexColor(words[1])
  return color

def render_ves(ves):

    first_line = ves[0]
    first_line = first_line.split(" ")
    width = int(first_line[2])
    height = int(first_line[3])

    obr = Image.new('RGB', (width, height), get_color(first_line))
    func_dict = {
        "CLEAR": get_color,
        "LINE": thick_line,
        "TRIANGLE": triangle,
        "FILL_TRIANGLE": filled_triangle,
        "RECT": rectangle,
        "FILL_RECT": filled_rectangle,
        "CIRCLE": circle,
        "FILL_CIRCLE": filled_circle
      }
    
    lst = []
    line_count = 0
    for x in ves:
        words = x.split(" ")
        lst.append(words[0])
        try:
            if words[0] in func_dict.keys():
                if words[0] != "VES" and words[0] != "CLEAR":
                    try:
                        func_dict[words[0]](obr, *[round(float(i)) for i in words[1:-1]], hexColor(words[-1]))
                    except TypeError:
                        print(f"Wrong number of arguments on line {line_count} - {x}")
                    line_count += 1
                elif words[0] == "CLEAR":
                    filled_rectangle(obr, 0, 0, width, height, hexColor(words[1]))
            elif "VES" not in lst:
                print("Wrong format, please enter valid format: VES version width height")
                return
            elif words[0] == "\n":
                line_count += 1
                pass
            else:
                print(f"Syntax error on line {line_count}: Unknown command {words[0]}")
                line_count += 1
        except IndexError:
            continue

    return obr

