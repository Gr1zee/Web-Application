import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css'; // Подключаем Tailwind CSS
import 'antd/dist/reset.css'; // Сброс стилей Ant Design

// Для React Router (если используется)
import { BrowserRouter } from 'react-router-dom';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter> {/* Только если нужен роутинг */}
      <App />
    </BrowserRouter>
  </React.StrictMode>
);