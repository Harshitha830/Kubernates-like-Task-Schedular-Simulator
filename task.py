# ------------------------------------------------------------
# Kubernetes-like Task Scheduler Simulator (User Input)
# This program simulates how Kubernetes schedules tasks (pods)
# to nodes based on available CPU and memory.
# ------------------------------------------------------------

class Node:

    def __init__(self, name, cpu, memory):
        self.name = name
        self.total_cpu = cpu
        self.total_memory = memory
        self.used_cpu = 0
        self.used_memory = 0
        self.tasks = []

    def can_run(self, task_cpu, task_memory):
        # Check if node has enough resources
        if (self.used_cpu + task_cpu <= self.total_cpu) and (self.used_memory + task_memory <= self.total_memory):
            return True
        return False

    def assign_task(self, task_name, task_cpu, task_memory):
        # Assign task to node
        self.used_cpu += task_cpu
        self.used_memory += task_memory
        self.tasks.append(task_name)


class Scheduler:

    def __init__(self, nodes):
        self.nodes = nodes

    def schedule_task(self, task_name, cpu, memory):

        for node in self.nodes:

            if node.can_run(cpu, memory):
                node.assign_task(task_name, cpu, memory)
                print("Task", task_name, "scheduled on", node.name)
                return

        print("Task", task_name, "could NOT be scheduled (Not enough resources)")


# ------------------------------------------------------------
# Step 1: Create Nodes
# ------------------------------------------------------------

nodes = []

num_nodes = int(input("Enter number of nodes in cluster: "))

for i in range(num_nodes):

    print("\nEnter details for Node", i+1)

    name = input("Node name: ")
    cpu = int(input("Total CPU: "))
    memory = int(input("Total Memory: "))

    nodes.append(Node(name, cpu, memory))


scheduler = Scheduler(nodes)


# ------------------------------------------------------------
# Step 2: Schedule Tasks
# ------------------------------------------------------------

num_tasks = int(input("\nEnter number of tasks to schedule: "))

for i in range(num_tasks):

    print("\nEnter details for Task", i+1)

    task_name = input("Task name: ")
    cpu = int(input("CPU required: "))
    memory = int(input("Memory required: "))

    scheduler.schedule_task(task_name, cpu, memory)


# ------------------------------------------------------------
# Step 3: Display Cluster Status
# ------------------------------------------------------------

print("\n----- Cluster Status -----")

for node in nodes:

    print("\nNode:", node.name)
    print("CPU Used:", node.used_cpu, "/", node.total_cpu)
    print("Memory Used:", node.used_memory, "/", node.total_memory)
    print("Tasks Running:", node.tasks)