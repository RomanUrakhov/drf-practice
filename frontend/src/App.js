import React from "react";
import { BrowserRouter, Route, Routes, Navigate, Link } from "react-router-dom";
import "./App.css";
import axios from "axios";
import UserList from "./components/User";
import ProjectList from "./components/Project";
import ProjectTodoList from "./components/ProjectTodos";
import TodoList from "./components/Todo";
import NotFound404 from "./components/Error";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      users: [],
      todos: [],
      projects: [],
    };
  }

  componentDidMount() {
    const getUsersRequest = axios.get("http://127.0.0.1:8000/user/");
    const getProjectsRequest = axios.get("http://127.0.0.1:8000/project/");
    const getTodoRequest = axios.get("http://127.0.0.1:8000/todo/");
    axios
      .all([getUsersRequest, getProjectsRequest, getTodoRequest])
      .then(
        axios.spread((...responses) => {
          const usersResponse = responses[0];
          const projectsResponse = responses[1];
          const todosResponse = responses[2];

          this.setState({
            users: usersResponse.data.results,
            projects: projectsResponse.data.results,
            todos: todosResponse.data.results,
          });
        })
      )
      .catch((errors) => console.log(errors));
  }

  render() {
    return (
        <div>
          <BrowserRouter>
            <nav>
              <ul>
                <li>
                  <Link to="/">Projects</Link>
                </li>
                <li>
                  <Link to="users">Users</Link>
                </li>
                <li>
                  <Link to="todos">Todos</Link>
                </li>
              </ul>
            </nav>
            <Routes>
              <Route
                exact
                path="/users"
                element={<UserList users={this.state.users} />}
              />
              <Route
                path="/"
                element={<ProjectList projects={this.state.projects} />}
              />
              <Route
                path="/todos"
                element={<TodoList todos={this.state.todos} />}
              />
              <Route
                  path=":id"
                  element={<ProjectTodoList todos={this.state.todos} />}
                />
              <Route path="/projects" element={<Navigate to="/" replace />} />
              <Route path="*" element={<NotFound404 />} />
            </Routes>
          </BrowserRouter>
        </div>
    );
  }
}

export default App;
