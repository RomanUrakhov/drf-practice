import React from "react";
import { useParams } from "react-router-dom";

const TodoItem = ({ todo }) => {
  return (
    <tr>
      <td>{todo.id}</td>
      <td>{todo.todo_name}</td>
      <td>{todo.author.login}</td>
    </tr>
  );
};

const ProjectTodoList = ({ todos }) => {
  const { id } = useParams();
  const filteredTodos = todos.filter((todo) => String(todo.project.id) === id);
  console.log(filteredTodos);
  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Author</th>
        </tr>
      </thead>
      <tbody>
        {filteredTodos.map((todo) => <TodoItem key={todo.id} todo={todo} />)}
      </tbody>
    </table>
  );
};

export default ProjectTodoList;
