from sys import stdin
__author__ = "Henrik Høiness"

def max_value(widths, heights, values, paper_width, paper_height, part_solutions):

    #Part solution = {(height,width) : value, ...}

    #Minste lengde/bredde med verdi:
    min_size = min(min(widths),min(heights))

    #Verdier som er mindre enn alle sedlene er ikke verdt noe
    for x in range(min_size):
        for y in range(max(paper_height,paper_width)):
            if (max(x,y),min(x,y)) not in part_solutions:
                part_solutions[(max(x,y),min(x,y))] = 0

    #Legger til verdiene til sedlene
    for i in range(len(widths)):
        if (max(widths[i],heights[i]),min(widths[i],heights[i])) not in part_solutions:
            part_solutions[(max(widths[i],heights[i]),min(widths[i],heights[i]))] = values[i]

        elif (max(widths[i],heights[i]),min(widths[i],heights[i])) in part_solutions:
            part_solutions[(max(widths[i],heights[i]),min(widths[i],heights[i]))] = max(part_solutions[(max(widths[i],heights[i]),min(widths[i],heights[i]))],values[i])



    #Kutter opp i alle mulige deler og legger inn i part_solutions:
    for width in range(paper_width+1):
        for height in range(paper_height+1):
            maxi = max(width,height)
            mini = min(width,height)

            if (maxi,mini) not in part_solutions:
                temp_value = 0

            elif part_solutions[(maxi,mini)] == 0:
                continue

            else:
                temp_value = part_solutions[(maxi,mini)]

            for v_cut in range(1,width):
                if temp_value < part_solutions[(max(v_cut,height),min(v_cut,height))] + part_solutions[(max(width-v_cut,height),min(width-v_cut,height))]:
                    temp_value = part_solutions[(max(v_cut,height),min(v_cut,height))] + part_solutions[(max(width-v_cut,height),min(width-v_cut,height))]

            for h_cut in range(1,height):
                if temp_value < part_solutions[(max(width,h_cut),min(width,h_cut))] + part_solutions[(max(width,height-h_cut),min(width,height-h_cut))]:
                    temp_value = part_solutions[(max(width,h_cut),min(width,h_cut))] + part_solutions[(max(width,height-h_cut),min(width,height-h_cut))]

            part_solutions[(maxi,mini)] = temp_value

    return part_solutions[max(paper_height,paper_width),min(paper_height,paper_width)]


def main():
    widths = []
    heights = []
    values = []

    for triple in stdin.readline().split():
        dim_value = triple.split(':', 1)
        dim = dim_value[0].split('x', 1)
        width = int(dim[0][1:])
        height = int(dim[1][:-1])
        value = int(dim_value[1])
        widths.append(int(width))
        heights.append(int(height))
        values.append(int(value))
    for line in stdin:
        paper_width, paper_height = [int(x) for x in line.split('x', 1)]
        print((max_value(widths, heights, values, paper_width, paper_height,{})))


if __name__ == "__main__":
    main()
