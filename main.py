with open("input.txt", "r", encoding="utf-8") as input_file:
    height_width_matrix = [int(x) for x in input_file.readline().strip().split(",")]
    start_vertex = [int(x) for x in input_file.readline().strip().split(",")]
    color_to_change = input_file.readline().strip()[1:-1]
    matrix_for_painting = []
    for _ in range(height_width_matrix[0]):
        row = input_file.readline().strip()
        row = [text.strip()[1:-1] for text in row.replace('[', '').replace('],', '').replace(']', '').split(',')]
        matrix_for_painting.append(row)


def get_from_side(pos_y, pos_x, visit_list, height_width, full_matrix, start_color, visited):
    if 0 <= pos_y < height_width[0] and 0 <= pos_x < height_width[1] and full_matrix[pos_y][pos_x] == start_color \
            and [pos_y, pos_x] not in visited:
        visit_list.append([pos_y, pos_x])
    return visit_list


def flood_fill(start_point: list[int, int], matrix: list[list[str]], new_color: str, height_width: list[int, int]):
    waypoints = [start_point]
    visited_points = []
    start_color = matrix[start_point[0]][start_point[1]]
    for point in waypoints:
        visited_points.append(point)
        matrix[point[0]][point[1]] = new_color
        waypoints = get_from_side(point[0], point[1] + 1, waypoints, height_width, matrix, start_color, visited_points)
        waypoints = get_from_side(point[0], point[1] - 1, waypoints, height_width, matrix, start_color, visited_points)
        waypoints = get_from_side(point[0] + 1, point[1], waypoints, height_width, matrix, start_color, visited_points)
        waypoints = get_from_side(point[0] - 1, point[1], waypoints, height_width, matrix, start_color, visited_points)
    return matrix


new_matrix = flood_fill(start_vertex, matrix_for_painting, color_to_change, height_width_matrix)

with open("output.txt", "w") as output_file:
    for row in new_matrix:
        output_file.write(str(row) + "\n")
