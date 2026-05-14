colors = ["Red","Blue","Green"]
#states = ["WA","NT","SA","Q","NSW","V"]
states = ["A","B","C","D"]
#neighbours = {"WA":["NT","SA"],"NT":["WA","SA","Q"],"SA":["WA","NT","Q","NSW","V"], "Q":["NT","SA","NSW"], "NSW":["Q","SA","V"],"V":["NSW","SA"]}
neighbours = {"A":["B","D","C"], "B":["A","D"], "D":["B","A","C"], "C":["A","D"]}
colors_of_states={}

def promising(state,color):
	for neighbour in neighbours.get(state):
		color_of_neighbour = colors_of_states.get(neighbour)
		if color_of_neighbour == color:
			return False
	return True

def get_color_for_state(state):
	for color in colors:
		if promising(state,color):
			return color

def main():
	for state in states:
		colors_of_states[state] = get_color_for_state(state)
	print(colors_of_states)

main()