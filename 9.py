left = list()
right = list()
players = 465
scores = [0 for x in range(players)]
turno = 0

#use one more than the highest marble for the range
for i in range(7194001):
	if i < 2:
		left.append(i)
	elif i % 23 == 0:
		for j in range(7):
			if len(left) > 0:
				right.append(left.pop())
			else:
				left = right
				left.reverse()
				right = [left.pop()]
		scores[turno] = scores[turno] + left.pop() + i
		left.append(right.pop())
		turno += 1
		if turno == players:
			turno = 0
	elif len(right) > 0:
		left.append(right.pop())
		left.append(i)
	else:
		right = left
		right.reverse()
		left = [right.pop(), i]
print max(scores)
