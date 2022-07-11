const UserItem = ({ user }) => {
  return (
    <tr>
      <td>{user.login}</td>
    </tr>
  );
};

const UserList = ({ users }) => {
  const userItemList = users.map((user) => (
    <UserItem key={user.url} user={user} />
  ));
  return (
    <table>
      <thead>
        <tr>
          <th>Login</th>
        </tr>
      </thead>
      <tbody>{userItemList}</tbody>
    </table>
  );
};

export default UserList;
