from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

TASKS = [
    {'id': 1, 'title': 'Learn Flask', 'status': 'Completed', 'priority': 'High'},
    {'id': 2, 'title': 'Build To-Do App', 'status': 'In Progress', 'priority': 'Medium'},
    {'id': 3, 'title': 'Push to GitHub', 'status': 'Pending', 'priority': 'Low'},
]

def get_new_id():
    return max([t['id'] for t in TASKS]) + 1 if TASKS else 1

@app.route('/', methods=['GET', 'POST'])
def home():
    global TASKS

    # Add new task
    if request.method == 'POST':
        title = request.form['title']
        priority = request.form['priority']

        TASKS.append({
            'id': get_new_id(),
            'title': title,
            'status': 'Pending',
            'priority': priority
        })

        return redirect(url_for('home'))

    # Filter
    status = request.args.get('status')
    if status:
        tasks = [t for t in TASKS if t['status'] == status]
    else:
        tasks = TASKS

    return render_template('index.html', tasks=tasks)

@app.route('/task/<int:task_id>')
def task(task_id):
    selected_task = next((t for t in TASKS if t['id'] == task_id), None)
    return render_template('task.html', task=selected_task)

if __name__ == '__main__':
    app.run(debug=True)
