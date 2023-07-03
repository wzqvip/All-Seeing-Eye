import React from 'react';
import { AppBar, Tabs, Tab } from '@material-ui/core';
import { useLocation, useNavigate, Routes, Route } from 'react-router-dom';
import Record from './Record';
import Predict from './Predict';
import Goal from './Goal';

const Home = () => {
  let { pathname } = useLocation();
  const navigate = useNavigate();
  const changeRoute = (event, newValue) => {
    navigate(newValue);
  };

  return (
    <div>
      <AppBar position="static">
        <Tabs value={pathname} onChange={changeRoute}>
          <Tab label="Record" value="/home/record" />
          <Tab label="Predict" value="/home/predict" />
          <Tab label="Goal" value="/home/goal" />
        </Tabs>
      </AppBar>
      <Routes>
        <Route path="/record" element={<Record />} />
        <Route path="/predict" element={<Predict />} />
        <Route path="/goal" element={<Goal />} />
      </Routes>
    </div>
  );
};

export default Home;
