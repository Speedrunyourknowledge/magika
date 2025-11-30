interface Task {
    id: number;
    title: string;
    completed: boolean;
    completedAt?: Date; // Optional property
}

class TaskManager {
    private tasks: Task[] = [];

    addTask(title: string): void {
        const newTask: Task = {
            id: this.tasks.length + 1,
            title: title,
            completed: false
        };
        this.tasks.push(newTask);
    }

    completeTask(id: number): void {
        const task = this.tasks.find(t => t.id === id);
        if (task) {
            task.completed = true;
            task.completedAt = new Date();
            console.log(`Task '${task.title}' marked as done.`);
        }
    }

    listTasks(): Task[] {
        return this.tasks;
    }
}

const manager = new TaskManager();
manager.addTask("Learn TypeScript");
manager.completeTask(1);