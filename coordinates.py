import pygame
#import boardgame
"""
def movement(a):
   l1 = [[300,35], [410, 35],[520,35],[630, 35],[740,35],[850, 35], [960, 35], [1070,35], [1180,35], [1290,35],
         [350, 95],[460,95], [570,95],[680,95], [790, 95],[1100, 95],[1210, 95],[1320, 95],[1430, 95],[1540, 95],
         [400, 155], [510,155], [620,155], [730, 155], [840, 155], [950, 155], [1060, 155], [1170,155], [1280,155], [1390,155],
         [450, 215], [560,215], [670,215], [780,215], [890,215], [1000, 215], [1110,215], [1220, 215], [1330, 215], [1440, 215],
         [500, 275], [610,275], [720,275], [830, 275], [940, 275], [1050, 275], [1160, 275], [1270, 275], [1380, 275], [1490, 275],
         [550, 335], [660,335], [770,335], [880,335], [990,335], [1100,335], [1210,335], [1320,335], [1430,335], [1540,335],
         [600, 395], [710,395], [820,395], [990,395], [1100,395], [1210,395], [1320, 395], [1430,395], [1540, 395], [1650, 395],
         [650, 465], [760,465], [870,465], [980, 465], [1090, 465], [1200, 465], [1310, 465], [1420, 465], [1530, 465], [1640, 465],
         [700, 525 ], [810, 525 ], [920, 525 ], [1030, 525 ], [1140, 525 ], [1250, 525 ], [1350, 525 ], [1470, 525 ], [1580, 525 ], [1690, 525 ],
         [750, 585 ], [860, 585 ], [970, 585 ], [1080, 585 ], [1190, 585 ], [1300, 585 ], [1410, 585 ], [1520, 585 ], [1630, 585 ], [1740, 585 ],
   ]
   l2 = l1[a]
   x = l2[0] - 25
   y = l2[1] - 25
   #return x, y
"""
def movement(a):
   l1 = [[293, 615],
         [390, 615], [450, 615], [510, 615], [570, 615], [630, 615], [690, 615], [750, 615], [810, 615], [870, 615],
         [930, 615],
         [930, 560], [870, 560], [810, 560], [750, 560], [690, 560], [630, 560], [570, 560], [510, 560], [450, 560],
         [390, 560],
         [390, 488], [450, 488], [510, 488], [570, 488], [630, 488], [690, 488], [750, 488], [810, 488], [870, 488],
         [930, 488],
         [930, 430], [870, 430], [810, 430], [750, 430], [690, 430], [630, 430], [570, 430], [510, 430], [450, 430],
         [390, 430],
         [390, 369], [450, 369], [510, 369], [570, 369], [630, 369], [690, 369], [750, 369], [810, 369], [870, 369],
         [930, 369],
         [930, 312], [870, 312], [810, 312], [750, 312], [690, 312], [630, 312], [570, 312], [510, 312], [450, 312],
         [390, 312],
         [390, 251], [450, 251], [510, 251], [570, 251], [630, 251], [690, 251], [750, 251], [810, 251], [870, 251],
         [930, 251],
         [930, 190], [870, 190], [810, 190], [750, 190], [690, 190], [630, 190], [570, 190], [510, 190], [450, 190],
         [390, 190],
         [390, 130], [450, 130], [510, 130], [570, 130], [630, 130], [690, 130], [750, 130], [810, 130], [870, 130],
         [930, 130],
         [930, 70], [870, 70], [810, 70], [750, 70], [690, 70], [630, 70], [570, 70], [510, 70], [450, 70], [390, 70]]
   l2 = l1[a]
   x = l2[0] - 25
   y = l2[1] - 25
   return x, y
