import React from 'react';
import { Route, Navigate } from 'react-router-dom';

const PrivateRoute = ({ element: Element, ...rest }) => {
  const isAuthenticated = Boolean(localStorage.getItem('token'));

  return (
    <Route
      {...rest}
      element={isAuthenticated ? Element : <Navigate to="/login" />}
    />
  );
};

export default PrivateRoute;
