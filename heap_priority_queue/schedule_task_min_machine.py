import heapq
# https://www.educative.io/courses/grokking-coding-interview-patterns-python/solution-schedule-tasks-on-minimum-machines

def tasks(tasks_list):
    optimal_machines = 0
    machines_available = []
    heapq.heapify(tasks_list)

    while tasks_list:  
        task = heapq.heappop(tasks_list)

        if machines_available and task[0] >= machines_available[0][0]:
            machine_in_use = heapq.heappop(machines_available)

            machine_in_use = (task[1], machine_in_use[1])

        else:
            optimal_machines += 1
            machine_in_use = (task[1], optimal_machines)

        heapq.heappush(machines_available, machine_in_use)

    return optimal_machines


# driver code
def main():

    input_tasks_list = [[(1, 1), (5, 5), (8, 8), (4, 4),
                        (6, 6), (10, 10), (7, 7)],
                        [(1, 7), (1, 7), (1, 7),
                        (1, 7), (1, 7), (1, 7)],
                        [(1, 7), (8, 13), (5, 6), (10, 14), (6, 7)],
                        [(1, 3), (3, 5), (5, 9), (9, 12),
                        (12, 13), (13, 16), (16, 17)],
                        [(12, 13), (13, 15), (17, 20),
                        (13, 14), (19, 21), (18, 20)]]

    for i in range(len(input_tasks_list)):
        print(i + 1, ".\t Tasks = ", input_tasks_list[i], sep="")

        print("\t Optimal number of machines = ",
              tasks(input_tasks_list[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()
