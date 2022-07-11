const ProjectItem = ({ project }) => {
  return (
    <tr>
      <td>{project.name}</td>
      <td>{project.repo_link}</td>
    </tr>
  );
};

const ProjectList = ({ projects }) => {
  const projectItemList = projects.map((project) => (
    <ProjectItem key={project.url} project={project} />
  ));
  return (
    <table>
      <thead>
        <tr>
          <th>Project name</th>
          <th>Link</th>
        </tr>
      </thead>
      <tbody>{projectItemList}</tbody>
    </table>
  );
};

export default ProjectList;
