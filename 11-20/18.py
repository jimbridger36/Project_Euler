ans = 1074
from testtools import pbl

# could make it a digraph and use dijkstra or could do this back tracking approach
# backtracking is simplest so why not


with open('18.txt', 'r') as data: # '18.txt' used to contain the triangle
	rows = int(data.readline())
	triangle = []

	for row in range(rows):
		triangle.append(data.readline().split())
		for column in range(row+1):
			triangle[row][column] = int(triangle[row][column])
valuearr = [i*[0] for i in range(1,rows+1)]

for column in range(rows):
	valuearr[rows-1][column] = triangle[rows-1][column]

for row in range(rows-2,-1,-1):
	for column in range(row+1):
		valuearr[row][column] = triangle[row][column] + max(valuearr[row+1][column],valuearr[row+1][column+1])

print(valuearr[0][0])





