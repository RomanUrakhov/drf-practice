import { useLocation } from "react-router-dom";

const NotFound404 = () => {
  const location = useLocation();
  return (
    <div>
      <h1>Страница по адресу '{location.pathname}' не найдена</h1>
    </div>
  );
};

export default NotFound404;
