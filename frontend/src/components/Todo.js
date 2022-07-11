const TodoItem = ({ todo }) => {
  return (
    <tr>
      <td>{todo.todo_name}</td>
      <td>{todo.author}</td>
      <td>{todo.updated_date}</td>
    </tr>
  );
};

const TodoList = ({ todos }) => {
  const todoItemList = todos.map((todo) => (
    <TodoItem key={todo.url} todo={todo} />
  ));
  return (
    <table>
      <thead>
        <tr>
          <th>Todo</th>
          <th>Author</th>
          <th>Last update</th>
        </tr>
      </thead>
      <tbody>{todoItemList}</tbody>
    </table>
  );
};

export default TodoList;
