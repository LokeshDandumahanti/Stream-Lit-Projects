import streamlit as st

# Title of the app
st.title("To-Do List")

# Text input to enter tasks
task = st.text_input("Enter your Task", '')

# Button to add tasks
if st.button("Add Task"):
    if task:
        st.session_state["task_list"].append(task)

# Initialize the task list if it doesn't exist
if "task_list" not in st.session_state:
    st.session_state["task_list"] = []

# Display the task list
for i, t in enumerate(st.session_state["task_list"]):
    st.write(f"{i + 1}. {t}")

# Checkbox to mark tasks as complete and remove them
tasks_to_remove = [i for i in range(len(st.session_state["task_list"])) if st.checkbox(f"Complete {i + 1}. {st.session_state['task_list'][i]}")]
for i in sorted(tasks_to_remove, reverse=True):
    st.session_state["task_list"].pop(i)
