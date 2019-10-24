import numpy as np
def only_ones(list):
  for i in list:
    if i > 1:
      return False
  return True
def vector_tester(vector, size):
  print(np.reshape(vector,tuple(reversed(size))))
def init_rect(size, field):
  if size[0] <= field[0] and size[1] <= field[1]:
    area = field[0]*field[1]
    hor_step = field[0]-size[0]+1
    vert_step = field[1] - size[1]+1
    init_matr = np.zeros(((hor_step) * (vert_step),area))
    template = (([1] * size[0] + [0]*(field[0]-size[0]))*size[1])
    i=0
    for j in range(vert_step):
      for k in range(hor_step):
        k = ([0]*field[0])*j + [0]*k + template[:len(template)-(field[0]-size[0])] #template for iteration
        init_matr[i] = k + [0]*(area-len(k))
        i += 1
    resulted_matr1 =init_matr
  #same code for rotated rectangles
  if size != tuple(reversed(size)):
    size = tuple(reversed(size))
    if size[0] <= field[0] and size[1] <= field[1]:
      area = field[0]*field[1]
      hor_step = field[0]-size[0]+1
      vert_step = field[1] - size[1]+1
      init_matr = np.zeros(((hor_step) * (vert_step),area))
      template = (([1] * size[0] + [0]*(field[0]-size[0]))*size[1])
      i=0
      for j in range(vert_step):
        for k in range(hor_step):
          k = ([0]*field[0])*j + [0]*k + template[:len(template)-(field[0]-size[0])] #template for iteration
          init_matr[i] = k + [0]*(area-len(k))
          i += 1

      resulted_matr2 = init_matr
  if "resulted_matr1" in locals() and "resulted_matr2" in locals():
    return np.vstack((resulted_matr1,resulted_matr2))
  if "resulted_matr1" in locals():
    return resulted_matr1
  if "resulted_matr2" in locals():
    return resulted_matr2
  else:
    return False

def init_L(size,field):
  if size[0] <= field[0] and size[1] <= field[1]:
    area = field[0]*field[1]
    hor_step = field[0]-size[0]+1
    vert_step = field[1] - size[1]+1
    init_matr = np.zeros(((hor_step) * (vert_step),area))
    template = [1]*size[0] + [0]*(field[0]-size[0])  + ([1]+[0]*(field[0]-1))*(size[1]-2) +[1]
    i=0
    for j in range(vert_step):
      for k in range(hor_step):
        k = ([0]*field[0])*j + [0]*k + template #template for iteration
        init_matr[i] = k + [0]*(area-len(k))
        i += 1
    resulted_matr1 = np.vstack((init_matr,[(np.rot90(np.reshape(x,field),2)).ravel() for x in init_matr]))
  if size[1] <= field[0] and size[0] <= field[1]:
    area = field[0]*field[1]
    hor_step = field[0]-size[1]+1
    vert_step = field[1] - size[0]+1
    init_matr = np.zeros(((hor_step) * (vert_step),area))
    template = [1]*size[1] + ([0]*(field[0]-1)+[1])*(size[0]-1)
    print(template)
    i=0
    for j in range(vert_step):
      for k in range(hor_step):
        k = ([0]*field[0])*j + [0]*k + template #template for iteration
        init_matr[i] = k + [0]*(area-len(k))
        i += 1
    resulted_matr2 = np.vstack((init_matr,[(np.rot90(np.reshape(x,field),2)).ravel() for x in init_matr]))
  
  if "resulted_matr1" in locals() and "resulted_matr2" in locals():
    return np.vstack((resulted_matr1,resulted_matr2))
  if "resulted_matr1" in locals():
    return resulted_matr1
  if "resulted_matr2" in locals():
    return resulted_matr2
  else:
    return False
def vect(list1,list2):
  new_vect = np.zeros((list1.shape[0] * list2.shape[0],list1.shape[1]))
  k = 0
  for i in list1:
    for j in list2:
      tmp = i + j
      if only_ones(tmp):
        new_vect[k] = tmp
        k+=1
  return new_vect[:k]
import ast
def main():
  print("Input tuple with rectangle size (wide,height)")
  size = ast.literal_eval(input())
  print("Input tuples list with rectangles [((wide,height),count)]")
  rectangles = ast.literal_eval(input())
  figures_rects = []
  if len(rectangles)!=0:
    for i in rectangles:
      for k in range(i[1]):
        figures_rects.append(i[0])
  
  print("Input tuples list with L-ominos [((left,right),count)]")
  l_ominos = ast.literal_eval(input())
  tmp = False
  figures_l = []
  if len(l_ominos) != 0:
    for i in l_ominos:
      for k in range(i[1]):
        figures_l.append(i[0])
  if len(figures_rects)>0:
  
    tmp = init_rect(figures_rects[0], size) #initiate with first figure
    for i in figures_rects[1:]:
      if type(tmp) != bool:
        tmp = vect(tmp,init_rect(i, size))
      else:
        return False
  k = 0
  if len(figures_rects)==0 and len(figures_l) > 1:
    tmp = init_L(figures_l[0],size)
    k = 1
  if len(figures_l)>1:
    for i in figures_l[k:]:
      if type(tmp) != bool:
        tmp = vect(tmp,init_L(i,size))
      else:
        return False
  if len(figures_l) == 0 and len(figures_rects) == 0:
    return True
  if type(tmp) != bool:
    vector_tester(tmp[0],size)
    return True
  else:
    return False
    
print(main())    