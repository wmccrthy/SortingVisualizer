# from heapq import merge
import pygame as pg
import random
import sys

pg.init()
window_width = 1200
arr_width = 1000
window_height = 800
window = pg.display.set_mode((window_width, window_height))

font = pg.font.SysFont('chalkboardse', 20)
ins = pg.font.SysFont('chalkboardse', 15)
header = font.render("Sorting Visualizer", True, (0,0,0))
instruc = ins.render("s for selectionSort, b for bubbleSort, m for mergeSort, r to randomize array", True, (0,0,0))


def displayText(window, text1, text2):
    window.blit(text1, (window_width/2-text1.get_width()/2, 5))
    window.blit(text2, (window_width/2-text2.get_width()/2, 35))


# initalize array of size 100, values set randomly in range (0, window_height)
def drawArray(a, swapped):
    # randcolor = (random.randint(0, 250), random.randint(0, 250), random.randint(0, 250))
    for val in range(0, len(a)):
        if val not in swapped:
            drawBar((0,0,0), val, a)
        else:
            # pg.draw.rect(window, (250, 250,250), (val*window_width/len(a) , window_height-a[val], window_width/len(a)-1, a[val]))
            drawBar((0, 0, 250), val, a)
# drawing array: each element drawn as rectangle w height = a[i], width = window_width / len(a) (x cord at y cord at window_height (bottom of screen))

def drawBar(color, index, a):
    pg.draw.rect(window, color, (index*arr_width/len(a)+100, window_height-a[index]-50, arr_width/len(a)-2, a[index]))



def createArr():
    a = []
    for i in range(0, 100):
        a.append(random.randint(50, window_height-200))
    return a


clock = pg.time.Clock()

def bubbleSort(a):
    for i in range(0, len(a)):
        for j in range(0, len(a)- i - 1):
            swapped = []
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped.append(j+1)
                swapped.append(j) 
                clock.tick(244)
                window.fill((250,250,250))
                displayText(window, header, instruc)
                drawArray(a, swapped)
                pg.display.flip()


def selectionSort(a):
    for i in range(0, len(a)-1):
        minimum = a[i]
        minInd = i
        swapped = []
        for j in range(i, len(a)):
            if a[j] < minimum:
                minimum = a[j]
                minInd = j
        temp = a[i]
        a[i] = minimum
        a[minInd] = temp
        swapped.append(i)
        swapped.append(minInd)
        clock.tick(30)
        window.fill((250,250,250))
        displayText(window, header, instruc)
        drawArray(a, swapped)
        pg.display.flip()


def merge(arr, start, mid, end):
    
    start2 = mid + 1
  
    # If the direct merge is already sorted
    if (arr[mid] <= arr[start2]):
        return
  
    # Two pointers to maintain start
    # of both arrays to merge
    while (start <= mid and start2 <= end):
        
        # If element at start ind is already in sorted position 

        if (arr[start] <= arr[start2]):
            start += 1

        else:
            value = arr[start2]
            index = start2
            # Shift all the elements between the start of L array and R array by 1, to accomodate for swap of starting values 

            while (index != start):
                
                # pause functionality test 
                # for event in pg.event.get():
                #     if event.type == pg.KEYDOWN:
                #         if event.key == pg.K_p:
                #             return


                swapped = []
                arr[index] = arr[index - 1]
                index -= 1
                swapped.append(index)
                swapped.append(index-1)

                # run faster when arrays being merged are larger 
                if abs(start - end) > 25:
                    clock.tick(144)
                else:
                    clock.tick(60)

                window.fill((250,250,250))
                displayText(window, header, instruc)
                drawArray(arr, swapped)
                pg.display.flip()
                # display the relevant shift visually
            
            swapped.append(start)
            window.fill((250,250,250))
            displayText(window, header, instruc)
            drawArray(arr, swapped)
            pg.display.flip()
            # display the swap of starting values visually 
            arr[start] = value
            
            # update trackers 
            start += 1
            mid += 1
            start2 += 1
           
    
def mergeSort(arr, l, r):
    if (l < r):

        m = (l + r) // 2
        
        # trying to implement pause 
        # for event in pg.event.get():
        #     if event.type == pg.KEYDOWN:
        #         if event.key == pg.K_p:
        #             return

         # Sort halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)

        merge(arr, l, m, r)

# def mergeSort(a, orig):
#     if len(a) <= 1:
#         return
#     swapped = []
#     clock.tick(60)
#     window.fill((0,0,0))
#     drawArray(orig, swapped)
#     pg.display.flip()
#     mid = int(len(a)/2)
#     L = a[:mid]
#     R = a[mid:]
#     mergeSort(R, orig)
#     mergeSort(L, orig)
#     i =  k = 0
#     j = 0
#     while i < len(L) and j < len(R):
#         swapped = []
#         if L[i] <= R[j]:
#             swapped.append(i)
#             a[k] = L[i]
#             orig[k] = L[i]
            
#             i += 1
    
#         else:
#             swapped.append(j)
#             a[k] = R[j]
#             orig[k] = R[j]
#             j += 1
        
#         swapped.append(k)
#         clock.tick(60)
#         window.fill((0,0,0))
#         drawArray(orig, swapped)
#         pg.display.flip()
#         k += 1
 
#     swapped = []
#     while i < len(L):
#         swapped.append(i)
#         swapped.append(k)
#         a[k] = L[i]
#         orig[k] = L[i]
#         clock.tick(60)
#         window.fill((0,0,0))
#         drawArray(orig, swapped)
#         pg.display.flip()
#         i += 1
#         k += 1
        
 
#     while j < len(R):
#         swapped.append(i)
#         swapped.append(k)
#         a[k] = R[j]
#         orig[k] = R[j]
#         clock.tick(60)
#         window.fill((0,0,0))
#         drawArray(orig, swapped)
#         pg.display.flip()
#         j += 1
#         k += 1
        



        
def main():
 
 arrayTest = createArr()
 while True:
    window.fill((250,250,250))
    pg.font.init()
    displayText(window, header, instruc)
    swapped = []
    drawArray(arrayTest, swapped)
    pg.display.flip()
    for event in pg.event.get():
              if event.type == pg.QUIT:
                  pg.quit()
                  sys.exit()
              elif event.type == pg.KEYDOWN:
                  if event.key == pg.K_r:
                      arrayTest = createArr()
                  if event.key == pg.K_b:
                      bubbleSort(arrayTest)
                  if event.key == pg.K_m:
                      mergeSort(arrayTest, 0, len(arrayTest)-1)
                  if event.key == pg.K_s:
                      selectionSort(arrayTest)
              


main()